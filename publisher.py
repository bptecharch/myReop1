import requests
import json

my_records = [
       {"type": "Sales", "value": "house_for_sale"},
        {"type": "Lease", "value": "apt_for_lease"},
        {"type": "ShortSales", "value": "house_short_sale"},
        {"type": "TempRent", "value": "temp_rent"}
]

#note
#made some more changes
for record in my_records:
	try:
		requests.post("http://127.0.0.1:5000/bptech/project/streams", json = record)
	except Exception as e:
		print("Exception thrown when post to REST api: %s", e)