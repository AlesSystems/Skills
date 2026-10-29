import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {fps,scenes,totalFrames,musicVolume} from '../src/timeline.mjs';
assert(totalFrames/fps>=30 && totalFrames/fps<=60,'30–60 second edit');
assert.equal(musicVolume(0),0);assert.equal(musicVolume(totalFrames-1),0);assert.equal(musicVolume(45),0.24);assert.equal(musicVolume(totalFrames-91),0.24);
for(const scene of scenes){
 assert(Number.isInteger(scene.duration)&&scene.duration>36,'positive duration with room for fades');
 assert(scene.headline?.trim(),'scene headline');
 if(scene.focus){const {left,top,width,height}=scene.focus;assert([left,top,width,height].every(Number.isFinite),'finite focus rectangle');assert(left>=0 && top>=0 && width>0 && height>0 && left+width<=1720 && top+height<=690,'focus fits screenshot region')}
 if(scene.image){assert(scene.duration-36>=5*fps,'five-second reading hold');assert(!scene.image.includes('..') && /^[\w-]+\.png$/.test(scene.image),'local PNG');const png=readFileSync('public/'+scene.image);assert.equal(png.subarray(1,4).toString(),'PNG');assert.equal(png.readUInt32BE(16),1920);assert.equal(png.readUInt32BE(20),1080);}
}
assert(existsSync('public/close-up.mp3'),'licensed local production music');
const notes=readFileSync('public/music-license.md','utf8');
for(const text of ['Michael Ramir C.','2026-10-01','https://mixkit.co/license/modal/musicFree/','https://mixkit.co/terms/'])assert(notes.includes(text),'music provenance');
assert(notes.includes(createHash('sha256').update(readFileSync('public/close-up.mp3')).digest('hex')),'music hash');
if(process.argv[2]==='--source'){console.log('Source and asset preflight passed.');process.exit(0)}
const video=process.argv[2]||'out/frame-demo.mp4';
const probe=JSON.parse(execFileSync('ffprobe',['-v','error','-show_streams','-show_format','-of','json',video]));
const v=probe.streams.find(stream=>stream.codec_type==='video'),a=probe.streams.find(stream=>stream.codec_type==='audio');
assert.equal(v.codec_name,'h264');assert.equal(v.width,1920);assert.equal(v.height,1080);assert.equal(v.avg_frame_rate,`${fps}/1`);assert.equal(v.pix_fmt,'yuv420p');assert.equal(a?.codec_name,'aac');assert(Math.abs(Number(probe.format.duration)-totalFrames/fps)<=1/fps,'timeline matches media');
execFileSync('ffmpeg',['-v','error','-i',video,'-f','null','-'],{stdio:'pipe'});
assert(Number.isInteger(a.channels)&&a.channels>0,'audio channel count');
const pcm=execFileSync('ffmpeg',['-v','error','-i',video,'-map','0:a:0','-vn','-ar','48000','-f','f32le','-'],{maxBuffer:30*1024*1024});
const samples=new Float32Array(pcm.buffer,pcm.byteOffset,pcm.length/4);
const samplesPerSecond=48000*a.channels;
const rms=(start,end)=>{let sum=0;for(let i=start;i<end;i++)sum+=samples[i]**2;return Math.sqrt(sum/(end-start))};
let peak=0;for(const sample of samples)peak=Math.max(peak,Math.abs(sample));
const body=rms(Math.floor(samples.length*0.15),Math.floor(samples.length*0.85)),start=rms(0,samplesPerSecond/10),end=rms(samples.length-samplesPerSecond/10,samples.length);
assert(body>0.005,'audible music signal');assert(peak<0.99,'unclipped audio');assert(start<body/3 && end<body/3,'faded endpoints');
let offset=0;
const representatives=scenes.map(scene=>{const frame=offset+Math.floor(scene.duration/2);offset+=scene.duration;return frame});
const boundaries=[];offset=0;for(const scene of scenes.slice(0,-1)){offset+=scene.duration;boundaries.push(offset-1,offset,offset+1)}
for(const [name,frames,columns] of [['contact-sheet',representatives,3],['boundary-sheet',boundaries,3]]){
 const select=frames.map(frame=>`eq(n,${frame})`).join('+');
 execFileSync('ffmpeg',['-y','-v','error','-i',video,'-vf',`select='${select}',scale=640:360,tile=${columns}x${Math.ceil(frames.length/columns)}`,'-frames:v','1',`out/${name}.jpg`]);
}
execFileSync('ffmpeg',['-y','-v','error','-ss','20.5','-i',video,'-frames:v','1','out/extracted-preview.png']);
console.log(`PASS ${totalFrames/fps}s, 1920×1080, ${fps}fps, H.264/yuv420p + AAC, full decode. Audio RMS=${body.toFixed(4)}, peak=${peak.toFixed(4)}, endpoints=${start.toFixed(4)}/${end.toFixed(4)}.`);
