#Browser Opening with 2 tabs for different websites

from playwright.sync_api import sync_playwright

def two_websites():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page1=browser.new_page()
        page2=browser.new_page()

        page1.goto('https://www.google.com/',wait_until='domcontentloaded',timeout=10000)
        page2.goto('https://www.amazon.com/',wait_until='domcontentloaded',timeout=10000)

        print('Tab1:',page1.title())
        if bool(page1.title()):
         print('Google page is displayed')
        
        print('Tab2:',page2.title())

        input('Press Enter to close browser...')
        browser.close()

if __name__=="__main__":
    two_websites()
