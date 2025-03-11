import requests

BASE_URL = "http://localhost:8080/api/next_card_play"

# A helper function to send POST requests to the endpoint
def send_request(data):
    response = requests.post(BASE_URL, json=data)
    return response

# Test cases based on valid card values (3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14)

def test_case_1():
    data = [3, 5, 7]  # Current card: 3, remaining cards: [5, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 5  # The smallest number >= 3 is 5

def test_case_2():
    data = [4, 3, 6]  # Current card: 4, remaining cards: [6, 3]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 4 is 6

def test_case_3():
    data = [5, 5, 7, 12]  # Current card: 5, remaining cards: [5, 12, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 5  # The smallest number >= 5 is 5

def test_case_4():
    data = [7, 9, 11, 13]  # Current card: 7, remaining cards: [9, 11, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 9  # The smallest number >= 7 is 9

def test_case_5():
    data = [8, 7, 6, 12]  # Current card: 8, remaining cards: [7, 12, 6]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 12  # The smallest number >= 8 is 12

def test_case_6():
    data = [6, 7, 8, 9]  # Current card: 6, remaining cards: [7, 8, 9]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 7  # The smallest number >= 6 is 7

def test_case_7():
    data = [12, 13, 14]  # Current card: 12, remaining cards: [13, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 13  # The smallest number >= 12 is 13

def test_case_8():
    data = [11, 12, 13]  # Current card: 11, remaining cards: [12, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 12  # The smallest number >= 11 is 12

def test_case_9():
    data = [3, 4, 6, 7]  # Current card: 3, remaining cards: [4, 6, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 4  # The smallest number >= 3 is 4

def test_case_10():
    data = [9, 5, 7, 11]  # Current card: 9, remaining cards: [11, 7, 5]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 9 is 11
    
def test_case_11():
    data = [2,  3, 8, 11]  # Current card: 2, remaining cards: [2,  3, 8, 11]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 2 is 3 