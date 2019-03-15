import urllib.request
import os
import music
while True:
    urllib.request.urlretrieve("http://mo.flussbuero.at/music/newfile.txt","newfile.txt")
    file = open("newfile.txt","r")
    name = file.read()
    name = name.lower()
    music.run(name)
    os.remove("newfile.txt")
    
