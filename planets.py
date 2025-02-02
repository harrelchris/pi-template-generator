import bz2
import csv
import io
import urllib.request

url = "https://www.fuzzwork.co.uk/dump/latest/mapDenormalize.csv.bz2"

response = urllib.request.urlopen(url)
compressed_data = response.read()
decompressed_data = bz2.decompress(compressed_data)
decoded_data = io.StringIO(decompressed_data.decode("utf-8"))
csv_reader = csv.reader(decoded_data)

# itemID	typeID	groupID	solarSystemID	constellationID	regionID	orbitID	x	y	z	radius	itemName	security	celestialIndex	orbitIndex
# 40222329	2015	7	30003503	20000511	10000043	40222328	-19619041642	-196198731	20110272738	1710000	Madirmilire I	0.603228207	1	None

columns = [
    1,  # typeID
    3,  # solarSystemID
    10, # radius
    11, # itemName
]

header = next(csv_reader)
trimmed_header = [header[i] for i in columns]

with open("planets.csv", "w", newline="", encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(trimmed_header)

    for row in csv_reader:
        if row[2] == "7":  # groupID 7 is planet
            trimmed_row = [row[i] for i in columns]
            radius = trimmed_row[2]
            radius = float(radius)
            radius = int(radius)
            trimmed_row[2] = radius
            csv_writer.writerow(trimmed_row)
