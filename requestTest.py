import requests

url = 'https://storage.googleapis.com/tf-datasets/titanic/eval.csv'
try:
    response = requests.get(url, timeout=10)
    print("Status Code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)
