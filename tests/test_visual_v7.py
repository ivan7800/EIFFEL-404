from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
css=(root/'styles.css').read_text(encoding='utf-8')
js=(root/'app.js').read_text(encoding='utf-8')
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for width,height in [(1440,900),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
  page.set_content(html,wait_until='domcontentloaded')
  page.add_style_tag(content=css)
  page.add_script_tag(content=js)
  page.wait_for_timeout(650)
  info=page.evaluate('''() => { const c=document.querySelector('#scene'); const ctx=c.getContext('2d');let a=ctx.getImageData(Math.floor(c.width*.7),Math.floor(c.height*.35),1,1).data;return {canvas:[c.width,c.height], css:[c.getBoundingClientRect().width,c.getBoundingClientRect().height], pixel:[...a], rendered:c.width>300&&c.height>300} }''')
  assert info['rendered'],info
  assert not errors,errors
  page.screenshot(path=str(root/'tests'/f'captura_{width}.png'))
  print(f'{width}x{height}: renderizado, canvas {info["canvas"]}, pixel {info["pixel"]}, errores JS {len(errors)}')
  page.close()
 browser.close()
