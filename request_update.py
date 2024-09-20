from json import loads, dumps
from jsonpath_ng import parse


def request_update(file_name, parameters: dict):
    f = open(file_name, "r")
    js = loads(f.read())
    for xp, vl in parameters.items():
        js_path = parse(xp)
        js_path.find(js)
        js_path.update_or_create(js, vl)
    f.close()
    return js


def request_updates(file_name, xpath, value):
    f = open(file_name, "r")
    js = loads(f.read())
    js_path = parse(xpath)
    js_path.find(js)
    js_path.update_or_create(js, value)
    print(dumps(js, indent=2))
    f.close()

import json

params: dict = {"$.serviceRequest.snapshotContext.snapshotType": "SNAPSHOT_TYPE_SOD",
          "$.serviceRequest.snapshotContext.snapshot_time": "1387374400000"}
fn = "/home/ln304/PycharmExt/playHome/finx/finx_instruments_pricing.request"

import json
# with open("/home/ln304/saved_dictionary.json", "w") as fp:
#     json.dump(params, fp)

with open("/home/ln304/saved_dictionary.json", "r") as fp:
    person_dict = json.load(fp)

print(person_dict)

print("="*20)
import pickle

with open('/home/ln304/saved_dictionary.pkl', 'wb') as f:
    pickle.dump(params, f)

with open('/home/ln304/saved_dictionary.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)


# result = request_update(fn, params)
# print(dumps(result, indent=2))
