from playwright.sync_api import sync_playwright

def locators():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.amazon.in')

        title=page.title()
        path_url=page.url

        print('The title is:',title)
        print('The url is:',path_url)

        s1=page.get_by_placeholder('Search Amazon.in')
        s1.fill('Shoes')
        s2=page.locator("div[role='button']").first.click()
        print(s1)
        print(s2)

        input('press enter button to close........')
        


if __name__=='__main__':
    locators()