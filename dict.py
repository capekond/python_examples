# from collections import defaultdict
#
# d = {"date": 12525, "day": "Friday", "hour": 2, "minute": 3, "second": 4}
#
# class dt:
#     def __init__(self, d):
#         self.__dict__ = d
#
# ddt = dt(d)
#
# print(ddt)
# print(ddt.date)
# print(ddt.day)
#
# entity_table_fields = {"_": ["business_date", "asof_date", "asof_time",
#                                         "asof_date_time", "snapshot_type", "payload"],
#                            "future_contract": ["value", "unique_contract_id"],
#                            "future_contract_price": ["product_id", "contract_type", "product_symbol", "contract_status",
#                                                      "expiration_date", "contract_mnemonic", "contract_frequency",
#                                                      "unique_contract_id"]
#                            }
#
# print(entity_table_fields["_"])
# print(",".join(entity_table_fields["_"]))
#
# old_dict = {'unique_contract_id': 1001152, 'value': 0.0, 'value_creation_timestamp': '1715944205000'}
# your_keys = ['unique_contract_id', 'value_creation_timestamp']
#
# dict_you_want = {key: old_dict[key] for key in your_keys}
# print(dict_you_want)
#
# dict_you_want = {key: old_dict[key] for key in entity_table_fields["future_contract"]}
# print(dict_you_want)
#
# row = (20131218, 20131218, 700, 20131217231000, 'SOD', {'unique_contract_id': 1001152, 'value': 0.0, 'value_creation_timestamp': '1715944205000'})
# print(row[-1])
#
# type_name = "future_contract"
# dict_you_want = {key: row[-1][key] for key in entity_table_fields["future_contract"]}
# print(dict_you_want)
#
# res =  defaultdict(dict)
# res['aa']['bb'] = "a"
# print(res)
# print(res['aa']['bb'])


nested_dict = {}
levels = ['first_level_key', 'second_level_key', 'third_level_key']

current_dict = nested_dict
for level in levels:
    current_dict[level] = {}
    current_dict = current_dict[level]

current_dict['final_key'] = 'HODNOTA'
print(nested_dict)
print(nested_dict['first_level_key']['second_level_key']['third_level_key']['final_key'])
print(levels[:-1])
print(levels[-1])


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


d = Dictlist()
d['test'] = 1
d['test'] = 2
d['test'] = 3

print(d)