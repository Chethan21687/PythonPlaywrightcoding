#In DemoQA Website enter all the details and assert the added data

from playwright.sync_api import sync_playwright,expect

def locator_actions4():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000)
        page=browser.new_page()
        page.goto('https://demoqa.com/text-box')
        page.get_by_placeholder('Full Name').fill('Tom')
        page.get_by_placeholder('name@example.com').fill('Tom@example.com')
        page.get_by_placeholder('Current Address').fill('Rose Hills')
        page.locator('#permanentAddress').fill('Rose Hills')
        page.get_by_role('button',name='Submit').click()

        static_name=page.get_by_text('Name:')
        static_employee_email=page.get_by_text('Email:')
        static_current_address=page.get_by_text('Current Address :')
        static_permanent_address=page.get_by_text('Permananet Address :')

        #Assertion
        expect(static_name).to_have_text('Name:Tom')
        expect(static_employee_email).to_have_text('Email:Tom@example.com')
        expect(static_current_address).to_have_text('Current Address :Rose Hills')
        expect(static_permanent_address).to_have_text('Permananet Address :Rose Hills')
        print('All the static text are visible')

        browser.close()

if __name__=='__main__':
    locator_actions4()
