def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 960, "height": 1080})
    page = context.new_page()
    page.goto("http://localhost:8000/docs")
    page.get_by_role("button", name="Item", exact=True).click()
    page.set_viewport_size({"width": 960, "height": 700})
    page.screenshot(
        path="docs/en/docs/img/tutorial/separate-openapi-schemas/image05.png"
    )

    # ---------------------
    context.close()
    browser.close()