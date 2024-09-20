import datetime
import json
import pprint

version = 20
snap_time = "0011122"
business_date = datetime.datetime.now()
iids_set = set()
products_set = {'Hello', 101, -2, 'Bye'}
req_dict = {'version': version, 'business_date': business_date, 'snap_time': snap_time, 'instrument_ids': iids_set,
            'product_ids': products_set}
print(req_dict)
pp = pprint.PrettyPrinter(indent=4, width=1)
pp.pprint(req_dict)
js = '{"glossary": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {    "GlossEntry": {"ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML", "Abbrev": "ISO8879:1986", "GlossDef": {"para": "A meta-markup language", "GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}'
# js = {"glossary": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {    "GlossEntry": {"ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML", "Abbrev": "ISO8879:1986", "GlossDef": {"para": "A meta-markup language", "GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}
try:
    parsed = json.loads(js)
except (TypeError):
    print("js is dictionary with double quote")
    parsed = js

print(json.dumps(parsed, indent=4))