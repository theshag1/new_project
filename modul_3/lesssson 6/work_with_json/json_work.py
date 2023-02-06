import json

compiturs = [
    {
        'name': 'asus',
        'id': 1,
        'Aolor': 'bed'
    }
    ,
    {
        'name': 'lenova',
        'id': 2,
        'color': 'black'
    }
]
arr = json.dumps(compiturs, indent=4)  # json.dumps( ) oqib oladi

with open('compitur.json', 'w') as f:
    json.dump(compiturs, f, sort_keys=True)  # json.dump() yukledi misol faylga yozadi

with open('compitur.json') as f:
    a = json.load(f)  # ochilgan fayldi  oqib beradi load()


