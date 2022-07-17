pip install -r .\src\requirements.txt
pyinstaller .\src\app.py -F -n "app.exe" -i .\assets\icon.png --distpath .\build\dist --workpath .\build\tmp
