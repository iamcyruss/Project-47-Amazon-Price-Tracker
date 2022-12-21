import requests


amazon_response = requests.get("http://www.example.com/",
                               headers={
                                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                   "Accept-Language": "en-US,en;q=0.9"
                               })
print(amazon_response.text)
