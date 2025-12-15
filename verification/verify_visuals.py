
from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local server
        page.goto("http://localhost:5173")

        # Wait for content to load
        page.wait_for_timeout(2000)

        # Check logo background (can't easily verify transparency via code without screenshot, so screenshot is key)
        # We will take a screenshot of the top section including nav
        page.screenshot(path="verification/verification_nav.png", clip={"x":0, "y":0, "width": 1280, "height": 300})

        # Scroll to products to see the card
        # Products are further down, triggers on scroll
        page.evaluate("window.scrollTo(0, 1500)")
        page.wait_for_timeout(1000)

        # Take screenshot of a product card
        # The cards have class .hero-panel-card
        card = page.locator(".hero-panel-card").first
        if card.is_visible():
            # Taking a screenshot of the viewport to see context and transparency
            page.screenshot(path="verification/verification_card_green.png")
        else:
            print("Card not visible")
            page.screenshot(path="verification/verification_failed.png")

        browser.close()

if __name__ == "__main__":
    run()
