from pathlib import Path
from playwright.sync_api import sync_playwright
import subprocess,time
root=Path(__file__).resolve().parents[1]
server=subprocess.Popen(['python','-m','http.server','8765','--bind','127.0.0.1'],cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
 time.sleep(.8)
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
  page=browser.new_page(viewport={'width':1440,'height':900});errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
  try:
   page.goto('http://127.0.0.1:8765/',wait_until='domcontentloaded',timeout=12000)
   page.wait_for_timeout(3000)
   print('status:',page.locator('#engineStatus').inner_text(),'canvas:',page.locator('#webgl-scene').count(),'errors:',errors)
   page.screenshot(path=str(root/'tests'/'captura_webgl.png'))
  except Exception as e:print('BROWSER_UNAVAILABLE:',str(e)[:300])
  browser.close()
finally: server.terminate();server.wait()
