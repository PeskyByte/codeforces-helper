import requests as rq
import json

URL = "https://codeforces.com/api/"
user = "PeskyByte"

def makeRequest(method, params):
    req = rq.get(URL + method, params = params)
    return req.json()

def handleResponse(response):
    print("*************************")
    for field in response['result'][0]:
        print(field, response['result'][0][field], sep = ": ")
    print("*************************")
    
def userInfo():
    choice = input("""
1- User info.
2- User submissions.
q- exit
""")
    
    params = {
        'handles': user,
    }
    response = None
    if choice == '1':
        response = makeRequest('user.info', params)
    elif choice == '2':
        params['from'] = '1'
        response = makeRequest('user.status', params)
    elif choice == 'q':
        return
    else:
        print("Bad input.")
        return
    if(response['status'] == 'OK'):
        handleResponse(response)
    else:
        print(response['status'])

#############################
def config():
    choice = conifgMenu()
    if choice == 'q':
        return
    elif choice == '1':
        pass
    elif choice == '2':
        print(user)
    else:
        print("Bad input.")
        return

def conifgMenu() -> str:
    prompt = input("""
1- set username
2- current username
q- exit
""")
    return prompt

def menu() -> str:
    prompt = input("""
1- get user info
c- config
q- exit
""")
    return prompt
#############################
if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == 'q':
            break
        elif choice == 'c':
            config()
        elif choice == '1':
            userInfo()
        else:
            print('Bad input.')