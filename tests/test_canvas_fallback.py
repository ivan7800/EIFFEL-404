from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
js=(root/'app.js').read_text(encoding='utf-8')
css=(root/'styles.css').read_text(encoding='utf-8')
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1300,'height':900})
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.set_content(html)
    page.add_style_tag(content=css)
    page.add_script_tag(content=js)
    cases=[]
    def check(name, action, predicate):
        action()
        result=bool(predicate())
        cases.append((name,result))
        assert result,name
    check('nivel 1',lambda:page.locator('[data-level="1"]').click(),lambda:page.locator('#altitude').inner_text()=='057 M')
    check('nivel 2',lambda:page.locator('[data-level="2"]').click(),lambda:page.locator('#altitude').inner_text()=='116 M')
    check('cima',lambda:page.locator('[data-level="3"]').click(),lambda:page.locator('#altitude').inner_text()=='276 M')
    check('dia',lambda:page.locator('#dayBtn').click(),lambda:'active' in page.locator('#dayBtn').get_attribute('class'))
    check('noche',lambda:page.locator('#nightBtn').click(),lambda:'active' in page.locator('#nightBtn').get_attribute('class'))
    check('giro auto',lambda:page.locator('#spinBtn').click(),lambda:'active' in page.locator('#spinBtn').get_attribute('class'))
    check('reiniciar',lambda:page.locator('#resetBtn').click(),lambda:page.locator('#altitude').inner_text()=='000 M' and 'active' not in page.locator('#spinBtn').get_attribute('class'))
    check('explorar',lambda:page.locator('#exploreBtn').click(),lambda:page.locator('#altitude').inner_text()=='057 M')
    check('recorrido',lambda:page.locator('#tourBtn').click(),lambda:'active' in page.locator('#spinBtn').get_attribute('class'))
    check('ayuda abrir',lambda:page.locator('#helpBtn').click(),lambda:page.locator('#helpModal').is_visible())
    check('ayuda cerrar',lambda:page.locator('#closeHelp').click(),lambda:not page.locator('#helpModal').is_visible())
    check('ayuda entender',lambda:(page.locator('#helpBtn').click(),page.locator('#modalStart').click()),lambda:not page.locator('#helpModal').is_visible())
    print('PRUEBAS',len(cases),'OK',sum(ok for _,ok in cases),'ERRORES JS',errors)
    for name,ok in cases: print(('PASS' if ok else 'FAIL'),name)
    assert not errors,errors
    browser.close()
