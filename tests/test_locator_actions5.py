from playwright.sync_api import sync_playwright,expect

def locator_action5():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=10000, args=["--start-fullscreen"])
        page=browser.new_page(viewport={'width':1920,'height':1080})
        page.goto('https://practicetestautomation.com/practice-test-login/')
        title=page.title()
        print('The title is:',title)
        automation_url=page.url
        print('The Automation_url is:',automation_url)
        
        #locator
        username_field=page.get_by_label('username')
        username_field.fill('student')
        print(f'Username: {username_field.input_value()}')
        password_field=page.get_by_label('password')
        password_field.fill('Password123')
        print(f'Password: {password_field.input_value()}')
        page.get_by_role('button',name='Submit').click()

        #Assertion
        expect(page).to_have_url('https://practicetestautomation.com/logged-in-successfully/')
        expect(page.locator('h1')).to_have_text('Logged In Successfully')
        expect(page.locator('.has-text-align-center.wp-block-paragraph')).to_have_text('Congratulations student. You successfully logged in!')

        page.get_by_role('link',name='Log out').click()

        expect(page).to_have_url('https://practicetestautomation.com/practice-test-login/')

        print('All sections are reached properly')

        browser.close()
    
if __name__=='__main__':
    locator_action5()