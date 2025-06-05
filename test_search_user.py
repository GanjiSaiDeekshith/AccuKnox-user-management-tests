from playwright.sync_api import sync_playwright

def test_search_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.fill('input[name="username"]', 'Admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button[type="submit"]')
        page.wait_for_timeout(3000)

        page.click('text=Admin')
        page.wait_for_timeout(2000)

        # Search user
        page.locator('input[placeholder="Username"]').fill("deekshith_test")
        page.click('button:has-text("Search")')
        page.wait_for_timeout(2000)

        browser.close()
