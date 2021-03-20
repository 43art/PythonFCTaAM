import xmltodict

file = open('C:\\Users\\PC\\PycharmProjects\\FCTaAM\\20.03.2021\\map.osm', 'r', encoding='utf8')
dct = xmltodict.parse(file.read())

countAllTime = 0
countFirstPeriod = 0
countSecondPeriod = 0

for node in dct['osm']['node']:
    if 'tag' in node and isinstance(node['tag'], list):
       for tag in node['tag']:
            if tag['@k'] == 'opening_hours':
                if tag['@v'] == '24/7':
                    countAllTime += 1
                elif tag['@v'] == '11:00-23:00':
                    countFirstPeriod += 1
                elif tag['@v'] == '10:00-22:00':
                    countSecondPeriod += 1

print("Количество объектов на рассматриваемом участке, которые работают ежедневно и круглосуточно : ", countAllTime)
print("Количество объектов на рассматриваемом участке, которые работают ежедневно с 11:00-23:00: ", countFirstPeriod)
print("Количество объектов на рассматриваемом участке, которые работают ежедневно с 10:00-22:00: ", countSecondPeriod)