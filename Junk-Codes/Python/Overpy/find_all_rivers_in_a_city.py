import overpy

api = overpy.Overpass()
city = input("Enter city name: ")

q = f"""
area["name"="{city}"]->.a;
(way["waterway"="river"](area.a););out body;
"""

result = api.query(q)
for way in result.ways:
    river_name = way.tags.get("name", "Unnamed River")
    if river_name != "Unnamed River":
        print(river_name)
