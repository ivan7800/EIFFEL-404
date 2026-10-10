from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
 page=browser.new_page(viewport={'width':1440,'height':900});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:print('CONSOLE',m.type,m.text[:250]))
 html=(root/'index.html').read_text().replace('<script defer src="boot-local.js"></script>','')
 page.set_content(html,wait_until='domcontentloaded')
 b64=base64.b64encode((root/'assets/eiffel_404.glb').read_bytes()).decode()
 page.evaluate('''(b64)=>{window.fetch=async()=>({ok:true,arrayBuffer:async()=>Uint8Array.from(atob(b64),x=>x.charCodeAt(0)).buffer});}''',b64)
 page.add_script_tag(content=(root/'offline-webgl.js').read_text())
 page.wait_for_timeout(1700)
 print('status',page.locator('#engineStatus').inner_text());print('webgl',page.locator('#webgl-scene').count(),'errors',errors)
 if page.locator('#webgl-scene').count():
  print('dimensions',page.locator('#webgl-scene').evaluate('(e)=>[e.width,e.height]'))
  page.locator('#nightBtn').click();print('night',page.locator('#nightBtn').get_attribute('class'))
  page.locator('[data-level="2"]').click();print('altitude',page.locator('#altitude').inner_text())
  page.screenshot(path=str(root/'tests'/'captura_webgl_inyectado.png'))
 browser.close()
