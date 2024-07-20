from playwright.sync_api import sync_playwright
import os

cwd = os.path.dirname(os.path.realpath(__file__))
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{cwd}/README.html")
    page.pdf(path="README.pdf")
    browser.close()