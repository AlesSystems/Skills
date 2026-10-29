import {createRequire} from 'node:module';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import {mkdir} from 'node:fs/promises';
const require=createRequire(import.meta.url);
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
try {
 const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
 page.on('pageerror',error=>{throw error});
 await mkdir('public',{recursive:true});
 for(const screen of ['overview','ownership','readiness']){
  await page.goto(pathToFileURL(resolve('fixture.html')).href+'?screen='+screen);
  await page.waitForSelector('html[data-ready="true"]');
  await page.evaluate(()=>document.fonts.ready);
  await page.screenshot({path:`public/${screen}.png`});
 }
}finally{await browser.close()}
console.log('Captured three rendered fixture states at 1920×1080.');
