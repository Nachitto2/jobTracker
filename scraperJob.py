from playwright.sync_api import sync_playwright
import re
import csv

def setupBrowser(p):
    browser = p.firefox.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    return browser, page

def buscarOfertas(page):
    url = "https://ar.computrabajo.com/"
    page.goto(url)
    page.fill("#prof-cat-search-input","tester")
    page.keyboard.press("Enter")
    page.wait_for_selector("article.box_offer")

def procesarTarjeta(tarjeta,i):
    try:
        titulo = tarjeta.locator(".js-o-link").inner_text()
        empresa = tarjeta.locator(".fc_base.t_ellipsis").inner_text()

        tarjetaTexto = tarjeta.inner_text()

        #Patron regex, agarra numeros, . y , que vengan despues del signo $
        patron = r"\$[\d\., ]+"

        resultado = re.search(patron,tarjetaTexto)

        if resultado:
            sueldo = resultado.group(0).strip()
        else:
            sueldo = "No especificado"
        return {
            "titulo": titulo,
            "empresa": empresa,
            "sueldo": sueldo
        }
    except Exception as e:
        print(f"Error en el elemento {i}:{e}")
        return None
        
def main():
    with sync_playwright() as p:
        
        browser, page = setupBrowser(p)

        buscarOfertas(page)

        
        tarjetas = page.locator("article.box_offer")
        cantidadOfertas = tarjetas.count()

        print(f"Se encontraron {cantidadOfertas} ofertas de trabajo")

        for i in range(cantidadOfertas):
            tarjetaActual = tarjetas.nth(i)
            datos = procesarTarjeta(tarjetaActual,i)

            print(datos)
        page.pause()

if __name__=="__main__":
    main()