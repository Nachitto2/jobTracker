from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    url = "https://ar.computrabajo.com/"
    page.goto(url)
    page.fill("#prof-cat-search-input","QA tester")
    page.click("#search-button")
    
    trabajos = page.locator(".js-o-link")

    for i in range(5):
        print(trabajos.nth(i).inner_text())
    
    browser.close()
  

