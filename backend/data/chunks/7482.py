@pytest.fixture(scope="module")
def job_id() -> str:
    """
    测试定时任务用到的 job_id
    :return:
    """
    return "123"