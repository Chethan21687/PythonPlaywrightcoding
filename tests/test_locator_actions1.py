#Code for locator actions 
from playwright.sync_api import sync_playwright


def locator_actions():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.google.com/',wait_until='domcontentloaded')
        title=page.title()
        print('The Title is:',title)
        website_url=page.url
        print('The url is:',website_url)

        #locator
        page.locator('.gLFyf').fill('Playwright')
        page.locator('.gLFyf').press('Enter')
        print('Playwright Entered and Searched')
        input('Press Enter to close the browser...........')

if __name__=='__main__':
    locator_actions()
        
        




