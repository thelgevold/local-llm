import requests

BASE_URL = "http://localhost:8080/api/next_card_play"

# A helper function to send POST requests to the endpoint
def send_request(data):
    response = requests.post(BASE_URL, json=data)
    return response

def test_case_1():
    data = [7, 2, 3, 5]  # Current card: 7, remaining cards: [2, 3, 5]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 2

def test_case_1():
    data = [7, 10, 3, 5]  # Current card: 7, remaining cards: [10, 3, 5]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 10  

def test_case_1():
    data = [7, 10, 2, 5]  # Current card: 7, remaining cards: [10, 2, 5]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 2      