from app import app # import app from app.py file


def test_home():# pytest only see files that starts with "test_" and in that, funtions that start with "test_" will be considered for unit test cases
    response = app.test_client().get("/")
    assert response.status_code ==200
    assert response.data == b"Hello World!"