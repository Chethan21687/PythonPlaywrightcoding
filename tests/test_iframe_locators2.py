from playwright.sync_api import sync_playwright,expect

def iframe_nestedlocators():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximize'])
        page=browser.new_page()
        page.goto('https://demoqa.com/nestedframes')
        frame_one=page.frame_locator('#frame1')
        print('The Parent Frame is:',frame_one)
        expect(frame_one.locator('body')).to_contain_text('Parent frame')
        print('Assertion for parent frame is passed')
        frame_two=frame_one.frame_locator('iframe')
        print('The child frame is:',frame_two)
        expect(frame_two.locator('body')).to_contain_text('Child Iframe')
        print('Assertion for child frame is passed')
        browser.close()

if __name__=='__main__':
    iframe_nestedlocators()

