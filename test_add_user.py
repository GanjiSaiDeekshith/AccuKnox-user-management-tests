import time
from playwright.sync_api import sync_playwright

def test_add_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Login
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.fill('input[name="username"]', 'Admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button[type="submit"]')
        page.wait_for_timeout(3000)

        # Step 2: Go to Admin -> User Management
        page.click('text=Admin')
        page.wait_for_timeout(2000)
        page.click('text=Add')
        page.wait_for_timeout(2000)

        # Step 3: Fill the Add User form
        page.locator('input[placeholder="Type for hints..."]').click()
        page.locator('input[placeholder="Type for hints..."]').fill("Paul Collings")
        page.keyboard.press("Enter")

        page.locator('div[role="listbox"]').nth(1).click()  # Select User Role (Admin or ESS)
        page.locator('div[role="listbox"] >> text=Admin').click()

        page.locator('div[role="listbox"]').nth(2).click()  # Status
        page.locator('div[role="listbox"] >> text=Enabled').click()

        page.locator('input[name="username"]').fill("deekshith_test")
        page.locator('input[name="password"]').fill("Test@1234")
        page.locator('input[name="confirmPassword"]').fill("Test@1234")

        # Step 4: Click Save
