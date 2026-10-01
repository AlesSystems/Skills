import React from 'react';
import {AbsoluteFill,Audio,Composition,Img,Sequence,interpolate,registerRoot,staticFile,useCurrentFrame} from 'remotion';
import {fps,scenes,totalFrames,musicVolume} from './timeline.mjs';
const ink='#202a30',blue='#3268dc';
function Scene({scene}){
 const frame=useCurrentFrame();
 const opacity=interpolate(frame,[0,18,scene.duration-18,scene.duration-1],[0,1,1,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const lift=interpolate(frame,[0,24],[18,0],{extrapolateRight:'clamp'});
 const focus=scene.focus;
 const focusOpacity=interpolate(frame,[70,100],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const zoom=interpolate(frame,[30,100],[1,1.025],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 return <AbsoluteFill style={{opacity,transform:`translateY(${lift}px)`}}>{scene.image?<>
 <div style={{position:'absolute',top:100,left:100,fontSize:58,fontWeight:550,letterSpacing:-2}}>{scene.headline}</div>
 <div style={{position:'absolute',top:188,left:103,fontSize:28,color:'#67727a'}}>{scene.caption}</div>
 <div style={{position:'absolute',top:276,left:100,width:1720,height:690,borderRadius:20,overflow:'hidden',border:'1px solid #d6d9d3',boxShadow:'0 20px 45px #25344512',background:'#fff'}}>
 <div style={{position:'absolute',inset:0,transform:`scale(${zoom})`}}>
 <Img src={staticFile(scene.image)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:'center 52%'}}/>
 {focus&&<div style={{position:'absolute',...focus,border:'2px solid #3268dc80',borderRadius:14,opacity:focusOpacity}}/>}
 </div>
 </div></>:<>
 <div style={{position:'absolute',left:140,top:225,fontSize:32,color:blue,fontWeight:600,letterSpacing:-1}}>frame <span style={{color:'#8292ac',fontWeight:400,marginLeft:25,fontSize:24}}>RELEASE PLANNING</span></div>
 <div style={{position:'absolute',left:135,top:325,fontSize:112,lineHeight:1.08,letterSpacing:-5,fontWeight:550,whiteSpace:'pre-line'}}>{scene.headline}</div>
 <div style={{position:'absolute',left:140,top:665,fontSize:32,color:'#65717b'}}>{scene.caption}</div>
 <div style={{position:'absolute',right:180,top:360,width:280,height:280,border:'2px solid #c4d2ec',borderRadius:45,transform:`rotate(${interpolate(frame,[0,100],[-6,0],{extrapolateRight:'clamp'})}deg)`}}><div style={{position:'absolute',inset:50,borderRadius:25,background:blue}}/><div style={{position:'absolute',inset:105,borderRadius:12,background:'#f7f5ef'}}/></div>
 </>}</AbsoluteFill>;
}
function FrameDemo(){
 let offset=0;
 return <AbsoluteFill style={{background:'#f7f5ef',color:ink,fontFamily:'Arial, sans-serif'}}>
 {scenes.map(scene=>{const from=offset;offset+=scene.duration;return <Sequence key={scene.id} from={from} durationInFrames={scene.duration}><Scene scene={scene}/></Sequence>})}
 <div style={{position:'absolute',left:102,top:43,fontSize:23,color:'#6b747b'}}>FRAME / PRODUCT WALKTHROUGH</div>
 <div style={{position:'absolute',right:100,top:36,padding:'9px 17px',border:'1px solid #d3d8d9',borderRadius:25,fontSize:23,color:'#5c6974'}}>Sample product</div>
 <Audio src={staticFile('close-up.mp3')} volume={musicVolume}/>
 </AbsoluteFill>;
}
registerRoot(()=> <Composition id="FrameDemo" component={FrameDemo} durationInFrames={totalFrames} fps={fps} width={1920} height={1080}/>);
