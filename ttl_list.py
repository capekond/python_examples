cfg_restore_properties = []
d = {'config_file': 'cf1', 'property_name': 'pn1', 'property_value': 'pv'}
cfg_restore_properties += [{'config_file': 'cf1', 'property_name': 'pn1', 'property_value': 'pv'}]
print(cfg_restore_properties)
cfg_restore_properties += [{'config_file': 'cf2', 'property_name': 'pn2', 'property_value': 'pv2'}]
print(cfg_restore_properties)
print(cfg_restore_properties[1])
print(cfg_restore_properties[1]['property_value'])

s = ' exists: '
print(len(s) == 6)
print(len(s))


import re
s = 'gs://system-test-backup/1.0.0//'
slashes = [m.start() for m in re.finditer(r"/", s)]
print(s[:slashes[2]+1])

s = "data/data/"
s = s[1:] if s[0] == '/' else s
s = s if s[-1] == '/' else s + '/'
print (s)