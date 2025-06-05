from playwright.sync_api import sync_playwright

def test_edit_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.fill('input[name="username"]', 'Admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button[type="submit"]')
        page.wait_for_timeout(3000)

        page.click('text=Admin')
        page.fill('input[placeholder="Username"]', 'deekshith_test')
        page.click('button:has-text("Search")')
        page.wait_for_timeout(2000)

        page.click('i.bi-pencil-fill')  # Click edit icon
        page.wait_for_timeout(2000)

        # Example edit: change status to Disabled
        page.locator('div[role="listbox"]').nth(2).click()
        page.locator('div[role="listbox"] >> text=Disabled').click()
        page.click('button:has-text("Save")')
        page.wait_for_timeout(2000)

        browser.close()
