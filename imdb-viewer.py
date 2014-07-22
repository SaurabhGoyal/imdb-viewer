#-------------------------------------------------------------------------------
# Name		: imdb viewer
# Purpose	: To have a looka at imdb details of current video file
# Authors	: saurabh
# Created	: 22/07/14
# Licence	: GPL v3
#-------------------------------------------------------------------------------
import os
import json
import sys
import urllib2
def imdb_viewer(path):
    abspath,filepath=os.path.split(path)
    url = "http://guessit.io/guess?filename="+filepath
    jsonurl=urllib2.urlopen(url)
    data=json.loads(jsonurl.read())
    for key,value in data.items():
        if(key=='title'):
            title=value
        if(key=='series'):
            title=value

    print title    
    url2 = "http://www.omdbapi.com/?t="+title.replace(" ","%20")
    jsonurl2=urllib2.urlopen(url2)
    data2=json.loads(jsonurl2.read())
    for key,value in data2.items():
        if(key=='imdbID'):
            imdbID=value
        if(key=='Year'):
            Year=value
        if(key=='Released'):
            Released=value
        if(key=='Runtime'):
            Runtime=value
        if(key=='Genre'):
            Genre=value
        if(key=='Actors'):
            Actors=value    
        if(key=='Plot'):
            Plot=value
        if(key=='Language'):
            Language=value
        if(key=='Awards'):
            Awards=value
        if(key=='imdbRating'):
            imdbRating=value
        if(key=='imdbVotes'):
            imdbVotes=value
        if(key=='Runtime'):
            Runtime=value
        if(key=='Type'):
            Type=value
    
    file=open(title+"_imdb.txt","w")
    file.write(("\n"+Type+":\t"+title).encode("utf8"))
    file.write(("\n\nimdbID:\t"+imdbID).encode("utf8"))
    file.write(("\n\nrating:\t"+imdbRating).encode("utf8"))
    file.write(("\n\nVotes:\t"+imdbVotes).encode("utf8"))
    file.write(("\n\nReleased:\t"+Year).encode("utf8"))
    file.write(("\n\nPlot:\t"+Plot).encode("utf8"))
    file.write(("\n\nLanguage:\t"+Language).encode("utf8"))
    file.write(("\n\nGenre:\t"+Genre).encode("utf8"))
    file.write(("\n\nActors:\t"+Actors).encode("utf8"))
    
path = sys.argv[1]
imdb_viewer(path)
