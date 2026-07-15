from playwright.sync_api import sync_playwright,expect

def test_switch__windows_url():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximized'])
        page=browser.new_page()
        page.goto('https://demoqa.com/browser-windows')

        with page.expect_popup() as popup_info:
            page.get_by_role('button',name='New Tab').click()

        new_page=popup_info.value

        new_page.wait_for_load_state()

        current_path=new_page.url

        expect(new_page).to_have_url('https://demoqa.com/sample')

        print('The Current Path is:',current_path)

        expect(new_page.locator('h1')).to_have_text('This is a sample page')

        new_page.close()

        expect(page).to_have_url('https://demoqa.com/browser-windows')

        with page.expect_popup() as popup_info:
            page.get_by_role('button',name='New Window',exact=True).click()

        new_page=popup_info.value

        new_page.wait_for_load_state()

        current_window_url=new_page.url

        print('The Current window url is:',current_window_url)

        expect(new_page).to_have_url('https://demoqa.com/sample')

        expect(new_page.locator('h1')).to_have_text('This is a sample page')

        new_page.close()

        browser.close()
