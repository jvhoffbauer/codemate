def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 960, "height": 1080})
    page = context.new_page()
    page.goto("http://localhost:8000/docs")
    page.get_by_text("GET/items/Read Items").click()
    page.get_by_role("button", name="Try it out").click()
    page.get_by_role("button", name="Execute").click()
    page.screenshot(
        path="docs/en/docs/img/tutorial/separate-openapi-schemas/image02.png"
    )

    # ---------------------
    context.close()
    browser.close()