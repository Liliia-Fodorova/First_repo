import sys

print("Hello, Python!")
print(sys.argv)  





import requests

print("Библиотека requests работает!")
print(requests.__version__)


response = requests.get("https://jsonplaceholder.typicode.com/users/1")



print(response.status_code)
print(response.json())

user = response.json()

print(f"Name:{user["name"]}")
print(f"Email:{user["email"]}")
print(f"City:{user["address"]["city"]}")
print(f"Company:{user["company"]['name']}")


city = user["address"]["city"]

if city == "Gwenborough":
    print("Correct city")
else:
    print("Another city")    