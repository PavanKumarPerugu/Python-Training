import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200
print(response.json())

url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "API", "body": "Learning", "userId": 1}
response = requests.post(url, json=data)
print(response.status_code)  # 201
print(response.json())

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 or 204

response = requests.get("http://github.com")
print(response.status_code)   # 200
print(response.history)       # Shows redirects

response = requests.get("https://api.openweathermap.org/data/2.5/weather")
print(response.status_code)  # 400

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=London&appid=WRONG_KEY"
)
print(response.status_code)  # 401

response = requests.get("https://jsonplaceholder.typicode.com/invalid")
print(response.status_code)  # 404

response = requests.put("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)  # 405


urls = {
    200: "https://httpbin.org/status/200",
    400: "https://httpbin.org/status/400",
    401: "https://httpbin.org/status/401",
    403: "https://httpbin.org/status/403",
    404: "https://httpbin.org/status/404",
    405: "https://httpbin.org/status/405",
    429: "https://httpbin.org/status/429",
    500: "https://httpbin.org/status/500",
}

for code, url in urls.items():
    try:
        response = requests.get(url, timeout=5)
        print(f"Expected {code}, got {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Expected {code}, request failed:", e)


response = requests.get("https://httpstat.us/429")
print(response.status_code)  # 429


response = requests.get("https://httpstat.us/403")
print(response.status_code)  # 403


