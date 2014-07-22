imdb-viewer
===========

A python script to have a quick look at imdb details of current video file
It works for both movies and tv-shows, hopefully for all type of cinematography available at IMDB.

Installation-
--------------
*python 2.7 or higher must be installed-

1) Put imdb.cmd file in <b>shell:sendTo</b> folder
2) Put imdb-viewer.py in C:

That's it, now to get details of any video file, right click it and in sendto context menu select imdb.cmd
and a .txt file containing all details will be generated.

I have used following two APIs-

<b>1)Guessit</b>- http://api.guessit.io/
  to extract the correct title out of the filename.
  
<b>2)Omdbapi</b>- http://www.omdbapi.com/
  to get the details of the title
  
  
For any queries or feedback, drop a mail at saurabh.2561@gmail.com
