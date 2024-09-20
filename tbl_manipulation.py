
class Tbl:
    columns = list()
    values = list(list())

t = Tbl()

t.values = [['01HTHKQYZV6RA7GMCKMJD7VE96', 'future_contract_price', 1, 20230101, 20230101, 820, None, 'LIVE',
             {'value': 2398.74, 'unique_contract_id': 100001, 'value_creation_timestamp': 1672531200000}, 2398.74,
             100001,
             1672531200000],
            ['01HTHKQYYBFBHHQ74DFRNGP3J3', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 1408.91, 'unique_contract_id': 100001, 'value_creation_timestamp': 1672531200000},
             1408.91, 100001, 1672531200000],
            ['01HTHKQYZPCX2YRSJEFHAF2ETM', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 5968.53, 'unique_contract_id': 100002, 'value_creation_timestamp': 1672531200000}, 5968.53,
             100002,
             1672531200000],
            ['01HTHKQYZPRSW4FHQZW131S7MC', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 8885.98, 'unique_contract_id': 190002, 'value_creation_timestamp': 1672531200000},
             8885.98, 190002, 1672531200000],
            ['01HTHKQYZPSN43E0KRHV61T2DA', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 8412.35, 'unique_contract_id': 100003, 'value_creation_timestamp': 1672531200000}, 8412.35,
             100003,
             1672531200000],
            ['01HTHKQYZPJHC13N5H5ZS4DPRA', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 8008.75, 'unique_contract_id': 100004, 'value_creation_timestamp': 1672531200000},
             8008.75, 100004, 1672531200000],
            ['01HTHKQYZPV5Z3RQGYBWAJEYVZ', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 661.72, 'unique_contract_id': 100105, 'value_creation_timestamp': 1672531200000}, 661.72, 100105,
             1672531200000],
            ['01HTHKQYZQ4A1EWK35JAXXACV2', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 2674.59, 'unique_contract_id': 200001, 'value_creation_timestamp': 1672531200000},
             2674.59, 200001, 1672531200000],
            ['01HTHKQYZQFDSVM17M4JYH37P7', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
             {'value': 1236.46, 'unique_contract_id': 999003, 'value_creation_timestamp': 1672531200000}, 1236.46,
             999003,
             1672531200000],
            ['01HTHKQYZQE85SZB2R2DBM2Y7J', 'future_contract_price', 1, 20230101, 20230101, 2300, None, 'EOD',
             {'value': 5195.01, 'unique_contract_id': 100001, 'value_creation_timestamp': 1672531200000},
             5195.01, 100001, 1672531200000]]

t.columns = ['id', 'name', 'asof', 'business_date', 'asof_date', 'asof_time', 'asof_date_time', 'snapshot_type',
             'payload', 'value', 'unique_contract_id', 'value_creation_timestamp']

where_conditions: dict = {'name': "future_contract_price", 'asof_time' : 600}
output_fields: list = ['id', 'name', 'value', 'unique_contract_id']

from operator import itemgetter

def _dict_pretty(d: dict, pairs = " AND ", items = "="):
    ls = list(map(lambda pair: pair[0] + items + f"'{pair[1]}'", d.items()))
    return pairs.join(ls)

print(_dict_pretty(where_conditions))

print("select rows by where +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for where_condition in where_conditions.items():
    t.values = list(filter(lambda x: x[t.columns.index(where_condition[0])] == where_condition[1], t.values))
print(t.values)

print("select columns by output fields ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
t_out = Tbl()
t_out.columns = output_fields
for row in t.values:
    idx: list = list(filter(lambda x: t.columns[x] in output_fields, range(len(t.columns))))
    t_out.values.append(list(itemgetter(*idx)(row)))

print(t_out.columns)
print(t_out.values)

