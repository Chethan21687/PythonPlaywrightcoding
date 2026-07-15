from playwright.sync_api import sync_playwright


def test_switch_windows():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000, args=['--start-maximize'])
        page = browser.new_page()
        page.goto('https://demoqa.com/browser-windows')
        with page.expect_popup() as popup_info:
            page.click('text=New Tab')

            new_page = popup_info.value

            new_page.wait_for_load_state()

            print(new_page.title())

            new_page.close()

            page.bring_to_front()


if __name__ == "__main__":
    test_switch_windows()