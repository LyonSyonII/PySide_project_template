# Convert window.ui to window.py
src/ui_to_window.sh

# Create windows executable
wineconsole ./build.bat && echo -e "\033[0;32mWindows build Successful!\033[0m" &


# Install needed dependencies
pip install -r ./src/requirements.txt

# Create linux executable
pyinstaller ./src/app.py -F -n "app.x" -i ./assets/icon.png -s --distpath ./build/dist --workpath ./build/tmp && echo -e "\033[0;32mLinux Build Successful!\033[0m"
