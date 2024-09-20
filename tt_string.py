from datetime import datetime

from numpy import array

columns = ["business_date", "asof_date", "asof_time", "asof_date_time", "snapshot_type"]
payload = ["product_id", "contract_type", "product_symbol", "contract_status", "expiration_date", "contract_mnemonic",
           "contract_frequency", "unique_contract_id"]
nfs = {"asof_time": ["700", "800"], "asof_date_time": ["123456"], "snapshot_type": ['SOD', 'EOD'],
       "contract_status": ["1", "2"], "expiration_date": "A"}
entity_name = "test_entity"

w_cols = set(nfs.keys()).intersection(columns)
w_pays = set(nfs.keys()).intersection(payload)
wc = [c + " IN ('" + "', '".join(nfs[c]) + "')" for c in w_cols]
# wp = ["payload ->> '" + c + "' IN ('" + "', '".join(nfs[c]) + "')" for c in w_pays]
wp = []
sql_where = f"name = '{entity_name}'"
sql_where += " AND " + " AND ".join(wc + wp) if (wc + wp) else ""
print(sql_where)
sql = f"SELECT * FROM public.entity_table WHERE {sql_where};"

exp = {1: [7235.02675569, 9381.40203045, 13680.70368839, 9457.06340536, 9119.93414228], 2: [122]}
res = {1: [7235.02675569, 9381.40203045, 13680.70368839, 9457.06340536, 9119.93414228], 2: [122]}

print(exp[1])
print(exp[1][2])


def cast(value, totype):
    return totype(value)


types = [int, str, str]
v = "1"
for tp in types:
    a = cast(v, tp)
    print(a, type(a))


dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)
print(ts)
a1 = cast(a, type_1)
a2 = cast(a, t2)
print(a1, type(a1))
print(a2, type(a2))

mystr = cast(35, str)
print(mystr, type(mystr))

myfloat = cast("35", float)
print(myfloat, type(myfloat))

pay_sql = [('value', 'number'), ('value_creation_timestamp', 'string'), ('unique_contract_id', 'number')]
d = {}
# for l in ls:
#     d[l[0]] = l[1]
keys = [it[0] for it in pay_sql]
values = [it[1] for it in pay_sql]
d = dict(zip(keys, values))
dd = dict(zip([it[0] for it in pay_sql], [it[1] for it in pay_sql]))




pass