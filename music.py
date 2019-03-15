import os
import urllib.request

def run(name):
    name = name.replace(" ","%20")
    
    urllib.request.urlretrieve("url_to_music_folder"+name+".mp3",name+".mp3")
    os.system("start "+name+".mp3")
    os.remove(name+".mp3")
                               
    
