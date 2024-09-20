import re

s = """
ADMN.IFC.STIX.0001	HDR	FILELOCATION	/tmp/src/STIX
ADMN.IFC.STIX.0001	HDR	FILEPREFIX	test
ADMN.IFC.STIX.GLOBAL	IE4	ie4.consolidation.create_if_no_match	true
ADMN.IFC.STIX.GLOBAL	IE4	ie4.custom.consolidation.require.matchingkey	true
ADMN.IFC.STIX.GLOBAL	IE4	ie4.custom.file.parser	$AC_SYSTEM/local/bin/admn/stix_file_parser.sh
ADMN.IFC.STIX.GLOBAL	LDR	INTERFACE	STIX
ADMN.IFC.STIX.GLOBAL	LDR	TASK	STIX
ADMN.IFC.XX.GLOBAL	IE4	ie4.consolidation.adosperblock	10
ADMN.IFC.XX.GLOBAL	IE4	ie4.custom.consolidation.dont.reconsolidate	true
ADMN.IFC.XX.GLOBAL	IE4	ie4.custom.normalization.adosperblock	10
ADMN.IFC.XX.GLOBAL	IE4	ie4.custom.normalization.dont.renormalize	true
ADMN.IFC.XX.GLOBAL	IE4	ie4.flowthreadcount	16
ADMN.IFC.XX.GLOBAL	IE4	ie4.flushinterval	1000000
ADMN.IFC.XX.GLOBAL	IE4	ie4.loaderthreadcount	16
ADMN.IFC.XX.GLOBAL	IE4	ie4.log.console	false
ADMN.IFC.XX.GLOBAL	IE4	ie4.log.timethreshold	60
ADMN.IFC.XX.GLOBAL	MSC	BLOBCONTAINERNAME	blob-storage
ADMN.IFC.XX.GLOBAL	MSC	ENVIRONMENTTYPE	SND
ADMN.IFC.XX.GLOBAL	MSC	PARALELLCALCLIMIT	16
ADMN.IFC.XX.GLOBAL	MSC	STORAGEACCOUNTNAME	dbgriskpmdsr7storage
"""

items1= re.findall("^.*FILELOCATION.*$",s,re.MULTILINE)[0].split()[3]
items2= re.findall("^.*FILEPREFIX.*$",s,re.MULTILINE)[0].split()[3]
print(items1)
print(items2)