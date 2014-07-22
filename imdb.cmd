@echo on
cls
:my_loop
IF %1=="" GOTO completed
  python C:\imdb-viewer.py %1
  SHIFT
  GOTO my_loop
:completed
