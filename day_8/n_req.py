import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

response.status_code   # 200, 404, etc.
response.text          # Raw response
print(response.json())        # Parsed JSON

# get
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("Status Code:", response.status_code)
users = response.json()
print(response.json())
for user in users:
    print(user["id"], "-", user["name"], "-", user["email"])


#get a specific user posts
url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1
}
response = requests.get(url, params=params)
print("Final URL:", response.url)
print("Status Code:", response.status_code)
posts = response.json()
for post in posts[:3]:
    print(post["title"])

#post request
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My First Post",
    "body": "This is a real POST request example",
    "userId": 1
}
response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())

#post request - login simulation
url = "https://httpbin.org/post"
credentials = {
    "username": "admin",
    "password": "1234"
}
response = requests.post(url, json=credentials)
data = response.json()
print("Status Code:", response.status_code)
print("Sent JSON:")
print(data["json"])

#basic json parsing
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
data = response.json()   # Convert JSON → Python dict
print("User ID:", data["userId"])
print("Post ID:", data["id"])
print("Title:", data["title"])
print("Body:", data["body"])

#nested json parsing
data = {
    "name": "London",
    "main": {
        "temp": 18,
        "humidity": 75
    },
    "weather": [
        {
            "main": "Cloudy",
            "description": "overcast clouds"
        }
    ]
}
print("City:", data["name"])
print("Temperature:", data["main"]["temp"])
print("Humidity:", data["main"]["humidity"])
print("Condition:", data["weather"][0]["main"])
print("Description:", data["weather"][0]["description"])

#Real Weather API–Style Parsing
response = requests.get("https://httpbin.org/json")
data = response.json()
print(data["slideshow"]["title"])
for slide in data["slideshow"]["slides"]:
    print("-", slide["title"])

#looping thriugh json lists
url = "https://jsonplaceholder.typicode.com/users"
users = requests.get(url).json()
for user in users:
    print(user["name"], "-", user["email"])
