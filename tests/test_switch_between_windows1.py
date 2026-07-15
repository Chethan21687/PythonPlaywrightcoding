from playwright.sync_api import sync_playwright

def test_switch_between_windows_one():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximize'])
        page=browser.new_page()
        page.goto('https://qaplayground.dev/')
        page.locator("img[src='/img/new-tab.png']").click()
            
        with page.expect_popup() as popup_info:
            page.get_by_role('link',name='Open New Tab').click()

        new_page=popup_info.value

        new_page.wait_for_load_state()

        current_path=new_page.url

        print('The current url is:',current_path)

        new_page.close()

        page.bring_to_front()
    

if __name__ == "__main__":
    test_switch_between_windows_one()




