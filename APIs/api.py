import pandas as pd
import requests 
import json

response = requests.get("http://api.open-notify.org/astros")

print(response.status_code)
print(response.json())

