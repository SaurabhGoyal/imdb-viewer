imdb-viewer
===========

A python script to have a quick look at imdb details of current video file.

<b>Since it fetches the title from current filename(current file being file or directory) hence it will work on almost any folder or file having name of the title you want to look for.</b>

It works for both movies and tv-shows, hopefully for all type of cinematography available at IMDB.

Installation-
--------------
*python 2.7 or higher must be installed-

<b>(1)</b> Put imdb.cmd file in <b>shell:sendTo</b> folder
<b>(2)</b> Put imdb-viewer.py in C:

That's it, now to get details of any video file, right click it and in sendto context menu select imdb.cmd
and a .txt file containing all details will be generated.

I have used following two APIs-

<b>1)Guessit</b>- http://api.guessit.io/
  to extract the correct title out of the filename.
  
<b>2)Omdbapi</b>- http://www.omdbapi.com/
  to get the details of the title
  
  
For any queries or feedback, drop a mail at saurabh.2561@gmail.com
