from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    url = "https://ar.computrabajo.com/"
    page.goto(url)
    page.fill("#prof-cat-search-input","QA tester")
    page.keyboard.press("Enter")
    page.wait_for_selector(".js-o-link")
    
    trabajos = page.locator(".js-o-link")
    empresas = page.locator(".fc_base.t_ellipsis")
    sueldos = page.locator(".dIB mr10")

    cantidadTrabajos = trabajos.count()

    print(f"Se encontraron {cantidadTrabajos} ofertas")

    for i in range(5):
        try:
            titulo = trabajos.nth(i).inner_text()
            empresa = empresas.nth(i).inner_text()
            sueldo = sueldos.nth(i).inner_text()
            print(f"{titulo},{empresa},{sueldo}")
            

        except Exception as e:
            print("Error en el elemento {i}:{e}")
    
    browser.close()
  

