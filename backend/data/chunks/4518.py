def test_app():
    test_main.test_create_existing_item()
    test_main.test_create_item()
    test_main.test_create_item_bad_token()
    test_main.test_read_inexistent_item()
    test_main.test_read_item()
    test_main.test_read_item_bad_token()