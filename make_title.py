import glob
import os

files = glob.glob("./pages/*.html")
for file in files:
    print(file)

if os.path.exists("./index.html"):
    os.remove("./index.html")

html = "<h1>RiST 初心者向け Webページ公開編</h1>\n"
html += "<ul>"
for file in files:
    user_name = file.split("/")[-1].split(".")[0]
    path = file
    html += f"<li><a href='{path}'>{user_name}</li>"

html += "</ul>"

with open('index.html', mode="w") as f:
    f.write(html)