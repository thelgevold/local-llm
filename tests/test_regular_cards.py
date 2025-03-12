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

def test_case_12():
    data = [3, 5, 7]  # Current card: 3, remaining cards: [5, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 5  # The smallest number >= 3 is 5

def test_case_13():
    data = [4, 6, 7, 9]  # Current card: 4, remaining cards: [6, 7, 9]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 4 is 6

def test_case_14():
    data = [5, 6, 7, 8, 9]  # Current card: 5, remaining cards: [6, 7, 8, 9]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 5 is 6

def test_case_15():
    data = [7, 5, 6, 8, 9, 10]  # Current card: 7, remaining cards: [5, 6, 8, 9, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 8  # The smallest number >= 7 is 8

def test_case_16():
    data = [10, 11, 12, 13]  # Current card: 10, remaining cards: [11, 12, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 10 is 11

def test_case_17():
    data = [14, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Current card: 14, remaining cards: [5, 6, 7, 8, 9, 10, 11, 12, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 10  # The smallest number >= 14 is 14

def test_case_18():
    data = [2, 4, 5, 7, 8, 9]  # Current card: 2, remaining cards: [4, 5, 7, 8, 9]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 4  # The smallest number >= 2 is 4

def test_case_19():
    data = [8, 6, 7, 9, 10]  # Current card: 8, remaining cards: [6, 7, 9, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 9  # The smallest number >= 8 is 9

def test_case_20():
    data = [9, 4, 5, 6, 7, 8, 10, 11, 12]  # Current card: 9, remaining cards: [4, 5, 6, 7, 8, 10, 11, 12]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 9 is 11

def test_case_21():
    data = [6, 2, 3, 4, 5, 7, 8]  # Current card: 6, remaining cards: [2, 3, 4, 5, 7, 8]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 7  # The smallest number >= 6 is 7

def test_case_22():
    data = [1, 3, 4, 6, 7]  # Current card: 1, remaining cards: [3, 4, 6, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 1 is 3

def test_case_23():
    data = [5, 6, 8, 10]  # Current card: 5, remaining cards: [6, 8, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 5 is 6

def test_case_24():
    data = [11, 3, 4, 6, 7, 8]  # Current card: 11, remaining cards: [3, 4, 6, 7, 8]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 0  # The smallest number >= 11 is 11

def test_case_25():
    data = [9, 5, 7, 8, 10]  # Current card: 9, remaining cards: [5, 7, 8, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 10  # The smallest number >= 9 is 9    
def test_case_26():
    data = [5, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # Current card: 5, remaining cards: [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 5 is 6

def test_case_27():
    data = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]  # Current card: 12, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 13  # The smallest number >= 12 is 13

def test_case_28():
    data = [7, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # Current card: 7, remaining cards: [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 8  # The smallest number >= 7 is 8

def test_case_29():
    data = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]  # Current card: 14, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 15  # The smallest number >= 14 is 15

def test_case_30():
    data = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Current card: 20, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 20  # The smallest number >= 20 is 20

def test_case_31():
    data = [3, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]  # Current card: 3, remaining cards: [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 3 is 5

def test_case_32():
    data = [8, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]  # Current card: 8, remaining cards: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 8  # The smallest number >= 8 is 8

def test_case_33():
    data = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Current card: 11, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 11 is 11

def test_case_34():
    data = [13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]  # Current card: 13, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 14  # The smallest number >= 13 is 14

def test_case_35():
    data = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # Current card: 15, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 15  # The smallest number >= 15 is 15

def test_case_36():
    data = [6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Current card: 6, remaining cards: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 6 is 6

def test_case_37():
    data = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Current card: 19, remaining cards: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 12  # The smallest number >= 12 is 12

def test_case_38():
    data = [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Current card: 2, remaining cards: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 2 is 3

def test_case_39():
    data = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Current card: 10, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 10 is 10

def test_case_40():
    data = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Current card: 5, remaining cards: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 5  # The smallest number >= 5 is 5

def test_case_41():
    data = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Current card: 4, remaining cards: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 4  # The smallest number >= 18 is 18

def test_case_42():
    data = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # Current card: 4, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 4  # The smallest number >= 4 is 4

def test_case_43():
    data = [9, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Current card: 9, remaining cards: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 9  # The smallest number >= 9 is 9    
def test_case_44():
    data = [5, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Current card: 5, remaining cards: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 5  # The smallest number >= 5 is 5

def test_case_45():
    data = [6, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12]  # Current card: 6, remaining cards: [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 6 is 6

def test_case_46():
    data = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12]  # Current card: 10, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 10 is 10

def test_case_47():
    data = [3, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]  # Current card: 3, remaining cards: [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 3 is 3

def test_case_48():
    data = [8, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]  # Current card: 8, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 8  # The smallest number >= 8 is 8

def test_case_49():
    data = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 15, 16]  # Current card: 15, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 15, 16]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 15  # The smallest number >= 15 is 15

def test_case_50():
    data = [2, 1, 2, 2, 3, 4, 5, 6, 7]  # Current card: 2, remaining cards: [1, 2, 2, 3, 4, 5, 6, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 2 is 2

def test_case_51():
    data = [9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]  # Current card: 9, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 9  # The smallest number >= 9 is 9

def test_case_52():
    data = [7, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]  # Current card: 7, remaining cards: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 7  # The smallest number >= 7 is 7

def test_case_53():
    data = [4, 1, 2, 3, 4, 4, 5, 6, 7, 8]  # Current card: 4, remaining cards: [1, 2, 3, 4, 4, 5, 6, 7, 8]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 4  # The smallest number >= 4 is 4

def test_case_54():
    data = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 12, 13]  # Current card: 12, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 12, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 12  # The smallest number >= 12 is 12

def test_case_55():
    data = [5, 5, 5, 1, 2, 3, 4, 5, 6, 7, 8]  # Current card: 5, remaining cards: [5, 5, 1, 2, 3, 4, 5, 6, 7, 8]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 5  # The smallest number >= 5 is 5

def test_case_56():
    data = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11]  # Current card: 10, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 10 is 10

def test_case_57():
    data = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 14]  # Current card: 14, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 14  # The smallest number >= 14 is 14

def test_case_58():
    data = [6, 1, 2, 3, 4, 5, 6, 6, 6, 7]  # Current card: 6, remaining cards: [1, 2, 3, 4, 5, 6, 6, 6, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 6  # The smallest number >= 6 is 6

def test_case_59():
    data = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]  # Current card: 11, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 11  # The smallest number >= 11 is 11

def test_case_60():
    data = [2, 1, 2, 2, 3, 4, 5, 5, 6, 7]  # Current card: 2, remaining cards: [1, 2, 2, 3, 4, 5, 5, 6, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 3  # The smallest number >= 2 is 2

def test_case_61():
    data = [13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 13]  # Current card: 13, remaining cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 13]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 13  # The smallest number >= 13 is 13

def test_case_62():
    data = [1, 1, 1, 2, 3, 4, 5, 6, 7]  # Current card: 1, remaining cards: [1, 1, 2, 3, 4, 5, 6, 7]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 1  # The smallest number >= 1 is 1

def test_case_63():
    data = [9, 3, 4, 5, 6, 7, 8, 9, 9, 10]  # Current card: 9, remaining cards: [3, 4, 5, 6, 7, 8, 9, 9, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 9  # The smallest number >= 9 is 9

def test_case_64():
    data = [7, 3, 4, 5, 6, 7, 7, 8, 9, 10]  # Current card: 7, remaining cards: [3, 4, 5, 6, 7, 7, 8, 9, 10]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 7  # The smallest number >= 7 is 7

def test_case_65():
    data = [7, 3, 4, 5, 6, 12, 12, 13, 13, 13, 14, 14, 14]  # Current card: 7, remaining cards: [3, 4, 5, 6, 12, 12, 13, 13, 13, 14, 14, 14]
    response = send_request(data)
    assert response.status_code == 200
    assert response.json() == 12  # The smallest number >= 7 is 12