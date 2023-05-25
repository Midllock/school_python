import xml.etree.ElementTree as ET #import knihovny pro práci s XML soubory

#Načtení XML souboru
tree = ET.parse('C:/Users/Rosťa Patočka/Desktop/Visual studio/učitel/books.xml') #Zde zadejte cestu k požadovanému XML souboru
root = tree.getroot()


#Vyhledání autora a id knihy podle jejího názvu
for element in root.findall("book"):
    title = element.find("title").text
    if title == "Midnight Rain":
        print(element.find("author").text, element.get("id"))

#Vypsání všech knih
for element in root.findall(".//book"):
    title = element.find("title").text
    author = element.find("author").text
    genre = element.find("genre").text
    price = element.find("price").text
    publish_date = element.find("publish_date").text
    description = element.find("description").text
    print("Book:", title, "/nAuthor:", author, "/nGenre:", genre, "/nPrice:", price, "/nPublish date:", publish_date, "/nDescription:", description, "/n")
    
