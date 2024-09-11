import requests


area = int(input("Enter the area: "))

url = f"http://127.0.0.1:8000/predict/{area}"


response = requests.get(url)

print(response.json())
