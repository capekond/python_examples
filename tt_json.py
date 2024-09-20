import json
js = {
  "9100373": {
    "SOD": {
      "0700": "Future_1"
    },
    "EOD": {
      "2200": "Future_2"
    },
    "LIVE": {
      "0800": "Future_3",
      "1000": "Future_4"
    }
  }
}

nested_dict = {}
nested_dict['dictA'] = {}
nested_dict['dictA']['key_1'] = 'value_1'
nested_dict['dictA']['key_2'] = 'value_2'
nested_dict2 = { 'dictA': {'key_1': 'value_1', 'key_2': 'value_2'}}
pass

nested_dict = {}
keys_hierarchy = ['first_level_key1', 'second_level_key1', 'third_level_key1']
current_dict = nested_dict

for key in keys_hierarchy:
  current_dict = current_dict.setdefault(key, {})

current_dict['final_key'] = 'final_value'

# Example
print(nested_dict['first_level_key1']['second_level_key1']
      ['third_level_key1']['final_key'])

s = [1,2,4,8]
print(s[:-1])
print(s[-1])