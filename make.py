import csv
import glob
from operator import itemgetter
import folium
from pyproj import Proj, Transformer

csv_files = glob.glob('Data/*.csv')
# Relevant OS fields: Name, Type, Easting, Northing
get = itemgetter(2,7,8,9)

names = [
    # English
    "brush",
    "cops",
    "coppic",
    "charcoal",
    "collier",
    "hasl",
    "haesl",
    "haz",
    "hiz",
    "iron",
    "nut",
    "spring",
    # Scottish Gaelic
    "calbh",
    "calltain",
    "challtain",
    "caomhan",
    "caomhain",
    "cnò",
    "cnomh",
    "collainn",
    "garan",
    "garain",
    "preasarlach",
    "preasarlaich",
    # Welsh
    "cnau",
    "cneu",
    "coedlan",
    "prysg",
]

# Transform from OS grid ref to WGS84 lat/long
transformer = Transformer.from_crs("epsg:27700", "WGS84")

def makemap(woods):
    mapp = folium.Map(location=[53.5, -3.4], zoom_start=8)

    for wood in woods:
        print(wood)
        folium.Marker([wood[3], wood[2]],
            tooltip=wood[0],
            popup=f'<a href="https://www.geograph.org.uk/near/{wood[3]},{wood[2]}" target="geog">Geograph</a><br><a href="https://www.google.com/maps?q={wood[3]},{wood[2]}" target="goog">Google Maps</a>'
            ).add_to(mapp)
    mapp.save("index.html")


if __name__ == "__main__":
    places = []
    for csv_file in csv_files:
        with open(csv_file, encoding='utf-8') as csvf:
            reader = csv.reader(csvf)
            for row in reader:
                data = list(get(row))
                # type = "Woodland or Forest"
                if data[1].startswith('Woodland'):
                    for name in names:
                        if name in data[0].lower():
                            long_lat = transformer.transform(data[2], data[3])
                            data[2] = long_lat[1]
                            data[3] = long_lat[0]
                            places.append(data)
                            break
    makemap(places)
