import argparse
import re

FC_PRICE = ("id, name, asof, business_date, asof_date, asof_time, asof_date_time, snapshot_type, "
            "payload.value, payload.unique_contract_id, payload.value_creation_timestamp")

aaa = [['01HTHKQYZV6RA7GMCKMJD7VE96', 'future_contract_price', 1, 20230101, 20230101, 820, None, 'LIVE',
       {'value': 2398.74, 'unique_contract_id': 100001, 'value_creation_timestamp': 1672531200000}, 2398.74, 100001,
       1672531200000], ['01HTHKQYYBFBHHQ74DFRNGP3J3', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
                        {'value': 1408.91, 'unique_contract_id': 100001, 'value_creation_timestamp': 1672531200000},
                        1408.91, 100001, 1672531200000],
      ['01HTHKQYZPCX2YRSJEFHAF2ETM', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
       {'value': 5968.53, 'unique_contract_id': 100002, 'value_creation_timestamp': 1672531200000}, 5968.53, 100002,
       1672531200000], ['01HTHKQYZPRSW4FHQZW131S7MC', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
                        {'value': 8885.98, 'unique_contract_id': 190002, 'value_creation_timestamp': 1672531200000},
                        8885.98, 190002, 1672531200000],
      ['01HTHKQYZPSN43E0KRHV61T2DA', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
       {'value': 8412.35, 'unique_contract_id': 100003, 'value_creation_timestamp': 1672531200000}, 8412.35, 100003,
       1672531200000], ['01HTHKQYZPJHC13N5H5ZS4DPRA', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
                        {'value': 8008.75, 'unique_contract_id': 100004, 'value_creation_timestamp': 1672531200000},
                        8008.75, 100004, 1672531200000],
      ['01HTHKQYZPV5Z3RQGYBWAJEYVZ', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
       {'value': 661.72, 'unique_contract_id': 100105, 'value_creation_timestamp': 1672531200000}, 661.72, 100105,
       1672531200000], ['01HTHKQYZQ4A1EWK35JAXXACV2', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
                        {'value': 2674.59, 'unique_contract_id': 200001, 'value_creation_timestamp': 1672531200000},
                        2674.59, 200001, 1672531200000],
      ['01HTHKQYZQFDSVM17M4JYH37P7', 'future_contract_price', 1, 20230101, 20230101, 600, None, 'SOD',
       {'value': 1236.46, 'unique_contract_id': 999003, 'value_creation_timestamp': 1672531200000}, 1236.46, 999003,
       1672531200000], ['01HTHKQYZQE85SZB2R2DBM2Y7J', 'future_contract_price', 1, 20230101, 20230101, 2300, None, 'EOD',
                        {'value': 5195.01, 'unique_contract_id': 100001, 'value_creation_timestamp': 1672531200000},
                        5195.01, 100001, 1672531200000]]

def otestuj(ln):
    print("hello")
    if ln[1] == 'future_contract_price':
        return True
    return False

f = list(filter(otestuj, aaa))
f0 = list(filter(lambda x: x[1] == 'future_contract_price', aaa))


# f = filter(lambda ln: ln[1] == 'future_contract_price', ss)

print(f)
print(f0)
print("*************************")
ff = FC_PRICE.split(", ")
f_1 = filter(lambda x: "." in x, ff)
f_0 = filter(lambda x: not "." in x, ff)
print(", ".join(f_0))
print(", ".join(f_1))
print("*************************")
numbers = [70, 60, 80, 90, 50, 82, 90, 91, 84, 82, 94, 99, 78, 65, 61, 45, 89, 87, 49, 76, 81, 94]


def check_score(number):
    if number >= 80:
        return True
    return False


percentage_score = filter(check_score, numbers)
scores = list(percentage_score)
print(scores)
print("*************************************")
a = ["a", "b", "c", "d"]
b = [1,2]
from operator import itemgetter
print(itemgetter(*b)(a))


a = [1,2,2]
b = [11,112,112]
c = [11,112,112]
x= zip(a,b,c)

print(list(x))
print(list(x[1]))