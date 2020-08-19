@echo off
IF exist C:\Users\%USERNAME%\Documents\bin ( echo Folder Exists Continuing... ) ELSE ( mkdir C:\Users\%USERNAME%\Documents\bin && echo Folder Did Not Exist. Creating and Continuing ..)
setx /M PATH "%PATH%;C:\Users\%USERNAME%\Documents\bin"
copy .env C:\Users\%USERNAME%\Documents\bin\
copy create.py C:\Users\%USERNAME%\Documents\bin\
copy create.bat C:\Users\%USERNAME%\Documents\bin\
pip install -r requirements.txt
pause