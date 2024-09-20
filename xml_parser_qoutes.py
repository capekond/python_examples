import os


from xml.etree import ElementTree as ET
sample = """
<visu>aaa
     <time>12:34</time>
     <name>my_visu</name>
     <language>english</language>
     <vars>
         <var name="input1">2</var>
        <var name="input2">45.6</var>
         <var name="input3">"hello"</var>
     </vars>
 </visu>
"""
root = ET.fromstring(sample)
name = 'input2'
f = root.find("visu")
# f = root.find('.//vars/var[@name="{}"]'.format(name)).text
print(f)
ROOT_DIR = os.path.abspath(os.curdir)
# xml_nodes = ['QuoteList', 'Quote' 'evtTimstamp']
# xml_values = "2025-12-31T20:30:00"
#
tree = ET.parse(ROOT_DIR + '/xml/pattern.xml')
root = tree.getroot()
pass
# for xml_node in xml_nodes:
#     n = root.find(xml_node)
#     pass
