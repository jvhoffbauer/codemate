def test_Page():
    page = Page(title="Title", body="HelloWorld!")
    page_json = r'{"type":"page","title":"Title","body":"HelloWorld!"}'
    assert page.amis_json().replace(" ", "") == page_json
    assert page.amis_dict() == {"type": "page", "title": "Title", "body": "HelloWorld!"}
    assert page.amis_html().find(page_json)