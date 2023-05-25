import xml.etree.ElementTree as ET

tree=ET.parse("prace\plants.xml")
root=tree.getroot()


for elements in root.findall("PLANT"):
    COMMON = elements.find("COMMON").text
    PRICE = float(elements.find("PRICE").text[1:])
    BOTANICAL = elements.find("BOTANICAL").text
    if PRICE <= 3.00 :
        print(COMMON, BOTANICAL, PRICE)
    
