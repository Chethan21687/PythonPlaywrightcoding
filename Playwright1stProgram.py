# Browser opening script

from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.in/',wait_until='domcontentloaded')
        title = page.title()
        path = page.url
        print('The title is:',title)
        print('The Url is:',path)
        browser.close()     

if __name__ == "__main__":
    main()