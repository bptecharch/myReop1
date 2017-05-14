#import requests
import json

my_records = [
       {"type": "A", "value": "AAhouse_for_sale"},
        {"type": "B", "value": "BBapt_for_lease"},
        {"type": "C", "value": "CChouse_short_sale"},
        {"type": "D", "value": "DDtemp_rent"}
]

for record in my_records:
	try:
		#requests.post("http://127.0.0.1:5000/bptech/project/streams", json = record)
		print record
	except Exception as e:
		print("Exception thrown when post to REST api: %s", e)