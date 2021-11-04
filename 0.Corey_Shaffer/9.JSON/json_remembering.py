
#####   JSON:
import json
people_string='''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@gmail.com","john.smith@work-place.com"],
            "has-license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-537-7514",
            "emails": null,
            "has-license": true
        }
    ]
}
'''
    #String to Python && Python to String
data = json.loads(people_string)
#print(data)

for person in data['people']:
    del person['phone']
new_string = json.dumps(data,indent=2,sort_keys=True)
#print(new_string)

    #Python to JSON && JSON to Python
data = json.loads(people_string)
with open('data.json','w') as json_file:
    json.dump(data,json_file, indent =4,sort_keys=True)

with open('data.json','r',encoding="utf8") as json_file:
    data=json.load(json_file)
#print(data)