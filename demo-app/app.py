import requests

if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    
    if response.status_code == 200:
        print(response.json())
        