try:
    from playwright.sync_api import sync_playwright
except ImportError as exc:
    raise ImportError(
        "playwright is not installed. Install it with 'pip install playwright' and run 'playwright install' before using this script."
    ) from exc

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://sujoygarai.in")
    print(page.title())
    browser.close()