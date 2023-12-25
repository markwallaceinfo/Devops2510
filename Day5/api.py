import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=3"

payload = {}
headers= {
  "apikey": "AxM8XOA8zjDv0FDDm8I9HeGAwdGsFdqi"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(status_code)
# print(result)
# print(result['result'])


