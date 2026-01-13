import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.text)


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    print("Success:", response.json())
elif response.status_code == 404:
    print("Wrong URL")
elif response.status_code == 401:
    print("Unauthorized – check API key")
elif response.status_code >= 500:
    print("Server error – try again later")
else:
    print("Unexpected status:", response.status_code)

API_KEY = "YOUR_API_KEY"
CITY = "London"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
print(response.status_code)
print(response.json())

