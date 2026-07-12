#iframe locators

from playwright.sync_api import sync_playwright

def iframe_launch():
    with sync_playwright() as p:
     browser=p.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximized'])
     page=browser.new_page(viewport={'width':1920,'height':1080})
     page.goto('https://demoqa.com/frames')
     page.wait_for_load_state('networkidle')
     website_url=page.url
     print('The url is',website_url)
     editor_one=page.frame_locator('#frame1').locator('#sampleHeading')
     editor_one.wait_for(state='visible')
     print((editor_one).inner_text())

     editor_two=page.frame_locator('#frame2').locator('#sampleHeading')
     editor_two.wait_for(state='visible')
     print((editor_two).inner_text())
     browser.close()

if __name__=='__main__':
   iframe_launch()  

