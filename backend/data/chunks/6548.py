def test_invoke_list():
    """Test invoke --list"""
    return_code = subprocess.call("invoke --list", shell=True)

    assert return_code == 0