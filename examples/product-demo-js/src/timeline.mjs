export const fps=30;
export const scenes=[
 {id:'intro',duration:150,headline:'Bring the next release\ninto focus.',caption:'Frame · release planning'},
 {id:'overview',duration:330,image:'overview.png',headline:'One plan for the whole team.',caption:'See the next milestone at a glance.'},
 {id:'ownership',duration:330,focus:{left:535,top:262,width:310,height:320},image:'ownership.png',headline:'Make ownership clear.',caption:'A name and a date for every workstream.'},
 {id:'readiness',duration:330,focus:{left:890,top:244,width:196,height:407},image:'readiness.png',headline:'Know what is ready.',caption:'See the final check before launch.'},
 {id:'end',duration:120,headline:'A calmer way\nto release.',caption:'Frame · fictional sample product'},
];
export const totalFrames=scenes.reduce((sum,scene)=>sum+scene.duration,0);
export const musicVolume=frame=>0.24*Math.max(0,Math.min(1,frame/45,(totalFrames-1-frame)/90));
