from playwright.sync_api import sync_playwright,expect

def iframe_locators4():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximize'])
        page=browser.new_page()
        # Nested frameset page
        page.goto('https://testpages.eviltester.com/pages/embedded-pages/frames/')
        page.wait_for_load_state('domcontentloaded')
        # "Nested Frames Example Top" lives inside the frame named "top"
        top_frame = page.frame_locator('frame[name="top"]')
        expect(top_frame.locator('body')).to_contain_text('Nested Frames Example Top')
        print('The control has came to Frames example screen')
        browser.close()

if __name__=='__main__':
   iframe_locators4()  
