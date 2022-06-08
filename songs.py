import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit()

try:
    count = int(sys.argv[-1])
except ValueError:
    # they have not specified the count, default = 1
    count = 1

if count == 1:
    artist = "".join(map(str, sys.argv[1:]))
else:
    artist = "".join(map(str, sys.argv[1:-1]))

response = requests.get(f"https://itunes.apple.com/search?term={artist}&limit={count}&media=music")

# obj is a dictionary
obj = response.json()

# obj["results"] is a list
for item in obj["results"]:
    # item is a dictionary
    print(item["trackName"])