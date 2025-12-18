import json
import os
import sys
from datetime import datetime
from hashlib import sha256

out_dir = ""
if sys.argv[1] == "build":
    out_dir = "temp_dist"

fc = 0
registered = {"registered": {}, "listed": []}
for root, dirs, files in os.walk("posts"):
    for dir in dirs:
        os.makedirs(os.path.join(out_dir, root, dir), exist_ok=True)
    for file in files:
        if os.path.splitext(file)[1] == ".md":
            out_file = os.path.join(out_dir, root, os.path.splitext(file)[0] + ".json")
            in_file = os.path.join(root, file)
            content = ""

            file_item = {
                "title": "Placeholder Title",
                "date": "Jan 1,1970",
                "tags": [],
                "abstract": ":(",
                "listed": False,
                "external": False,
                "path": os.path.join(root, os.path.splitext(file)[0] + ".json"),
            }
            with open(in_file) as f:
                f.readline()
                meta_end = False
                while not meta_end:
                    x = f.readline().strip()
                    if x[:9].lower() == "abstract:":
                        abstract = ""
                        while (y := f.readline()).strip() != "---":
                            abstract += y
                        file_item["abstract"] = abstract
                        meta_end = True
                    elif x[:6].lower() == "title:":
                        file_item["title"] = x[6:].strip()
                    elif x[:6].lower() == "listed":
                        file_item["listed"] = True
                    elif x[:9].lower() == "external:":
                        file_item["external"] = True
                        file_item["tags"].append("External")
                        file_item["path"] = x[9:].strip()
                    elif x[:5].lower() == "date:":
                        file_item["date"] = x[5:].strip()
                    elif x[:5].lower() == "tags:":
                        file_item["tags"] += x[5:].strip().split(", ")

                content = f.read()

            if not file_item["external"]:
                with open(out_file, "w") as f:
                    json.dump({"content": content}, f)
            post_id = (
                os.path.splitext(file)[0]
                + "_"
                + sha256(root.encode()).digest()[:5].hex()
            )
            if file_item["listed"]:
                registered["listed"].append(
                    (post_id, datetime.strptime(file_item["date"], "%b %d,%Y"))
                )
            registered["registered"][post_id] = file_item
            fc += 1

registered["listed"] = list(
    map(lambda e: e[0], sorted(registered["listed"], key=lambda e: e[1], reverse=True))
)
with open("posts/registered.json", "w") as f:
    json.dump(registered, f, indent=4)
print(f"[*] {fc} posts registered")
