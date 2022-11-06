import json
#file = open("items.json")
items = json.loads(open("checkoutdetails.json").read())
#creds_json = json.loads(open("credentials.json").read())
print(items)
print(items[0]["firstname"])