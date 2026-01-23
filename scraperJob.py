from playwright.sync_api import sync_playwright
import re
import csv

def setupBrowser():
    browser = playwright.firefox.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    return browser, page

with sync_playwright() as playwright:
    
    browser, page = setupBrowser()
    url = "https://ar.computrabajo.com/"
    page.goto(url)
    page.fill("#prof-cat-search-input","tester")
    page.keyboard.press("Enter")
    page.wait_for_selector("article.box_offer")
    
    tarjetas = page.locator("article.box_offer")
    cantidadOfertas = tarjetas.count()

    print(f"Se encontraron {cantidadOfertas} ofertas de trabajo")

    for i in range(cantidadOfertas):
        tarjetaActual = tarjetas.nth(i)
        try:
            titulo = tarjetaActual.locator(".js-o-link").inner_text()
            empresa = tarjetaActual.locator(".fc_base.t_ellipsis").inner_text()

            tarjetaTexto = tarjetaActual.inner_text()

            #Patron regex, agarra numeros, . y , que vengan despues del signo $
            patron = r"\$[\d\., ]+"

            resultado = re.search(patron,tarjetaTexto)

            if resultado:
                sueldo = resultado.group(0).strip()
            else:
                sueldo = "No especificado"
            
            

            print(f"{titulo},{empresa},{sueldo}")
        except Exception as e:
            print(f"Error en el elemento {i}:{e}")


"""
    trabajos = page.locator(".js-o-link")
    empresas = page.locator(".fc_base.t_ellipsis")
    sueldos = page.locator(".dIB.mr10")

    cantidadTrabajos = trabajos.count()

    print(f"Se encontraron {cantidadTrabajos} ofertas")

    for i in range(cantidadTrabajos):
        try:
            titulo = trabajos.nth(i).inner_text()
            empresa = empresas.nth(i).inner_text()
            sueldo = sueldos.nth(i).inner_text()
            print(f"{titulo},{empresa},{sueldo}")
            

        except Exception as e:
            print("Error en el elemento {i}:{e}")
    
    browser.close()
  

"""