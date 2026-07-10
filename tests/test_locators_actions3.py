from playwright.sync_api import sync_playwright,expect

def locators_action3():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://practicetestautomation.com/practice-test-login/')

        #locators
        page.get_by_label('Username').fill('student')
        page.get_by_label('Password').fill('Moni@8080')
        page.get_by_role('button',name='Submit').click()
        Logout_button=page.get_by_role('link',name='Log out')

        #Assertion
        validation_message=page.locator('#error')
        expect(validation_message).to_have_text('Your password is invalid!')
        print('Error Message is displayed')
        expect(page).to_have_url('https://practicetestautomation.com/practice-test-login/')
        print('Login Url is seen')
        expect(Logout_button).not_to_be_visible()
        print('Log off button not visible')


if __name__=='__main__':
    locators_action3()































