import requests
data = requests.get("https://opentdb.com/api.php", params={"amount": 10, "type": "boolean"})
question_data = data.json()["results"]

