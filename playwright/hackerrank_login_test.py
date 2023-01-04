from playwright.sync_api import sync_playwright

# URL
URL = "https://www.hackerrank.com/auth/login"
Dashboard = "https://www.hackerrank.com/dashboard"

# Login Xpaths

EMAILIDTEXTBOX = '//*[@id="input-1"]'
EMAILID = "pulicalsreekanth@gmail.com"
PASSWORDTEXTBOX = '//*[@id="input-2"]'
PASSWORD = "Sreekanth@789"
SUBMITBUTTON = '//*[@id="tab-1-content-1"]/div[1]/form/div[4]/button/div/span'
LOGIN = '//*[@id="content"]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[2]/button'

# VERIFY LOGINss

PROFILE = '//*[@id="content"]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[5]/div/div/span'
logout = '//*[@id="content"]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[5]/div/div[2]/ul/li[10]/button'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3 * 1000)
    page = browser.new_page()

    # hacker rank webpage
    page.goto(URL)

    # enter credentials
    page.fill(EMAILIDTEXTBOX, EMAILID)
    page.fill(PASSWORDTEXTBOX, PASSWORD)

    # login

    page.click(SUBMITBUTTON)
    page.wait_for_url(Dashboard)

    #logout
    page.click(PROFILE)
    page.click(logout)

    page.wait_for_selector(LOGIN)
    page.click(LOGIN)

    #closing browser

    page.close()
    browser.close()
