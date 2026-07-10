#Code Generation for Application based on locators and actions

from playwright.sync_api import sync_playwright,expect

def locator_actions2():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://practicetestautomation.com/practice-test-login/')
        title=page.title()
        print('The title is:',title)
        login_test_url=page.url
        print('Url is:',login_test_url)
        
        #locators
        page.locator('#username').fill('student')
        page.locator('#password').fill('Password123')
        page.locator('#submit').click()

        success_message=page.locator('.post-header')
       
        
        expect(success_message).to_have_text('Logged In Successfully')
        page.get_by_text('Log out').click()
        input('To close the Browser press enter button')

if __name__=='__main__':
    locator_actions2()

