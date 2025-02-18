from pytestllm.main import login, signup

def test_login():
    assert login("admin", "admin") == True
    assert login("wrong", "wrong") == False
    assert login("admin", "wrong") == False
    assert login("wrong", "admin") == False