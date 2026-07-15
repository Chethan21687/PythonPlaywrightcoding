from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximize'])
    page=browser.new_page()
    page.goto('https://demoqa.com/nestedframes')
    parent=page.frame_locator('#frame1')
    text=parent.locator('body').inner_text()
    print(text)
    
