from playwright.sync_api import sync_playwright,expect

def iframe_locators3():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximize'])
        page=browser.new_page()
        page.goto('https://qaplayground.dev/apps/iframe/')
        first_iframe=page.frame_locator('#frame1')
        print('The first_frame is:',first_iframe)
        expect(first_iframe.locator('legend')).to_contain_text('First Level Iframe')
        second_iframe=first_iframe.frame_locator('#frame2')
        print('The second frame is:',second_iframe)
        expect(second_iframe.locator('legend')).to_contain_text('Second Level Iframe')
        second_iframe.get_by_role('link',name='Click Me').click()
        expect(second_iframe.locator('#msg')).to_contain_text('Button Clicked')

        browser.close()
    

if __name__=='__main__':
    iframe_locators3()