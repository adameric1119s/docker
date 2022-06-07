import requests
import json

url = "http://localhost:8081/users"

payload = json.dumps({
  "ime": "Adam",
  "prezime": "Eric",
  "smer": "IT",
  "predmeti": [
    {
      "ime": "Razvoj infrastrukture i servisa u oblaku",
      "espb": 8
    },
    {
      "ime": "Istorija racunarstva",
      "espb": 6
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
