import urllib.request
import os
import music
while True:
    urllib.request.urlretrieve("url_to_transmittion_text_file/nameOfYourFile.txt","nameOfYourFile.txt")
    file = open("nameOfYourFile","r")
    name = file.read()
    name = name.lower()
    music.run(name)
    os.remove("nameOfYourFile.txt")
    
