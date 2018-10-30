import json
data=json.load(open("cutresult.json","r"))
data=set(data)
print(data)