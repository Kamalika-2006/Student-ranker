import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url, timeout = 5)
   
    if res.status_code == 200:
         response = res.json()
    elif res.status_code == 400:
        print("Bad Request")
    elif res.status_code == 404:
        print("Not Found")
    elif res.status_code == 500:
        print("server error")
except requests.exceptions.ConnectionError:
    print("connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException as e:   #this prints the error that occurs during the request
    print(f"Error: {e}")

print(
    f"{'Name':<20}"
    f"{'Email':<20}"
)
print("-"*48)
for i,resp in enumerate(response):
    if i == 5:
        break
    print(
        f"{resp['name']:<20}"
        f"{resp['email']:<20}"
    )
