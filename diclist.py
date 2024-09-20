from collections import defaultdict
from typing import Any

levels = ['unique_contract_id', 'snapshot_type', 'asof_time']
all_columns = ['business_date', 'asof_date', 'asof_time', 'asof_date_time', 'snapshot_type', 'payload', 'value',
               'unique_contract_id']
table_data = [
    [20131218, 20131218, 100, 20131218170000, 'EOD', {'value': 10, 'unique_contract_id': 9100373, 'value_creation_timestamp': '1715944943000'}, 100, 9100373],
    [20131220, 20131218, 110, 20131218170000, 'EOD', {'value': 10, 'unique_contract_id': 9100373, 'value_creation_timestamp': '1715944943000'}, 100, 9100373],
    [20131218, 20131218, 120, 20131218170000, 'EOD', {'value': 20, 'unique_contract_id': 1005288, 'value_creation_timestamp': '1715944943000'}, 200, 1005288],
    [20131218, 20131218, 130, 20131217231000, 'SOD', {'value': 30, 'unique_contract_id': 9100373, 'value_creation_timestamp': '1715944943000'}, 300, 9100373],
    [20131218, 20131218, 140, 20131217231000, 'SOD', {'value': 40, 'unique_contract_id': 1005288, 'value_creation_timestamp': '1715944205000'}, 400, 1005288],
    [20131218, 20131218, 150, 20131217231000, 'SOD', {'value': 50, 'unique_contract_id': 9100373, 'value_creation_timestamp': '1715944943000'}, 500, 9100373],
    [20131218, 20131218, 140, 20131217231000, 'SOD', {'value': 60, 'unique_contract_id': 1005288, 'value_creation_timestamp': '1715944205000'}, 600, 1005288]
              ]


class GetEntityTable:
    def __init__(self, d):
        self.__dict__ = d


final = defaultdict(dict)
for row in table_data:
    lvs = []
    for level in levels:
        lvs.append(row[all_columns.index(level)])
    d = dict(zip(all_columns, row))
    res_line = {}
    curr = res_line
    for lv in lvs[1:-1]:
        curr[lv] = {}
        curr = curr[lv]
        pass
    curr[lvs[-1]] = GetEntityTable(d)
    final[lvs[0]].update(res_line)
    print(f"{lvs[0]}, {res_line}")
    pass
pass

# class Dictlist(dict):
#     def __setitem__(self, key, value):
#         try:
#             self[key]
#         except KeyError:
#             super(Dictlist, self).__setitem__(key, [])
#         self[key].append(value)
#


# d = Dictlist()
# d['test'] = 'A'
# d['test'] = "BB"
# d['test'] = "CC"
# print(d)
# pass
