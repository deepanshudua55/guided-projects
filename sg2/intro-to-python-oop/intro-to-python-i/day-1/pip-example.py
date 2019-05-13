# import doesn't work without pip
# import requests <-- for everything
from requests import get  # <-- just one module

url = "https://icanhazdadjoke.com/"

res = get(url, headers={"Accept": "application/json"})

res = res.json()

print(res['joke'])
