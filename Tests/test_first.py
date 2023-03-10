import requests
from src.enums.global_enus import GlobalErrorMessages

def test_Post_reqests():

    """Post"""

    json = {
        "username": "admin",
        "password": "password123"
    }
    r = requests.post('https://restful-booker.herokuapp.com/auth', json)
    print(f"\n{r.url}")
    token = ''
    token = r.json().get('token')
    print(f"Token:{token}")
    print(f"Status_code:{r.status_code}")
    assert r.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(token) == 15, GlobalErrorMessages.WRONG_TOKEN.value

def test_check_2():

    """Проверка, что 1! = 1"""

    assert 1!=2, "Числа равны друг другу"