# https://x.com/clcoding/status/1993523588327178509

import os
import hashlib

path = input("Folder: ")
seen = {}

for file in os.listdir(path):
    file_data = open(os.path.join(path, file), "rb").read()
    file_hash = hashlib.md5(file_data).hexdigest()
    if file_hash in seen:
        print("Duplicate", file, "<-->", seen[file_hash])
    else:
        seen[file_hash] = file
