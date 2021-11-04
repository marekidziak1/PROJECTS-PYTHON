import xml.etree.ElementTree as ET
tree=ET.parse('hodlers.xml')
root=tree.getroot()
print(ET.tostring(root))

print(root.get('coin'))
root.text='fdfd'
tree.write('hodlers.xml')
print(root.text)

data='''<crypto coin="Money!!!">INWESTORZY:
            <investor>Joe 1</investor>
            <investor>Joe 2</investor>
        </crypto>'''
tree=ET.ElementTree(ET.fromstring(data))
id=1
for investor in tree.findall('investor'):
    investor.set('id',str(id))
    id+=1
for investor in tree.findall('investor'):
    print(ET.tostring(investor))
tree.write('hodlers3.xml')





  