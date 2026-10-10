from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':900},accept_downloads=True)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 html=(root/'index.html').read_text().replace('<script defer src="boot-local.js"></script>','')
 page.set_content(html)
 glbs={name:base64.b64encode((root/'assets'/f'{name}.glb').read_bytes()).decode() for name in ['eiffel_404','paris_city','paris_parks']}
 page.evaluate('''(glbs)=>{
  const real=HTMLCanvasElement.prototype.getContext;
  const gl=new Proxy({}, {get(o,k){if(k==='isContextLost')return()=>false;if(k==='getShaderParameter'||k==='getProgramParameter')return()=>true;if(k==='getAttribLocation')return()=>0;if(k==='getUniformLocation')return()=>1;if(k==='createShader'||k==='createProgram'||k==='createBuffer')return()=>({});if(k==='getShaderInfoLog'||k==='getProgramInfoLog')return()=>'';if(typeof k==='string'&&k===k.toUpperCase())return 1;return()=>{};}});
  HTMLCanvasElement.prototype.getContext=function(type,...args){return type==='webgl'||type==='experimental-webgl'?gl:real.call(this,type,...args)};
  window.fetch=async(url)=>({ok:true,arrayBuffer:async()=>Uint8Array.from(atob(glbs[url.split('/').pop().replace('.glb','')]),c=>c.charCodeAt(0)).buffer});
 }''',glbs)
 page.add_script_tag(content=(root/'offline-webgl.js').read_text());page.wait_for_timeout(600)
 assert page.locator('#engineStatus').inner_text().startswith('3D WEBGL'),page.locator('#engineStatus').inner_text()
 for id in ['sunsetBtn','fogBtn','sparkBtn','cinemaBtn']:
  assert not page.locator('#'+id).is_disabled(),id
  page.locator('#'+id).click()
  assert 'active' in page.locator('#'+id).get_attribute('class'),id
 page.locator('#exposureSlider').evaluate("el=>{el.value='1.80';el.dispatchEvent(new Event('input',{bubbles:true}))}")
 assert page.locator('#exposureValue').inner_text()=='1.80'
 page.locator('#photoModeBtn').click()
 assert not page.locator('#photoToolbar').is_hidden()
 page.locator('#photoExitBtn').click()
 assert page.locator('#photoToolbar').is_hidden()
 page.locator('#resetBtn').click()
 assert 'active' not in page.locator('#fogBtn').get_attribute('class')
 assert page.locator('#exposureValue').inner_text()=='1.25'
 assert page.locator('#soundBtn').is_disabled()
 assert not errors,errors
 print('PASS: arranque simulado, ocaso, bruma, destellos, cinema, exposición, modo foto, salir, reiniciar y sonido desactivado; 0 errores JS')
 b.close()
