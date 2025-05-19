# Asteroids
Boot.dev project, my version of the classic Asteroids game

check requirements.txt for versions. 

# Create your own virtual environment
python -m venv venv
# Activate it
source venv/bin/activate  # or venv\Scripts\activate on Windows
# Install your dependencies
pip install -r requirements.txt

# Future plans to make executable with PyInstaller not yet implemented:

Create a standalone executable:

1) Install PyInstaller in your virtual environment:

    pip install pyinstaller

2) Package your game (while your virtual environment is activated):

    pyinstaller --onefile --windowed main.py

3) Find the executable in the dist folder that PyInstaller creates.

4) Share this executable file with your friends - they can just double-click it to run your game without installing Python or any packages!

Important notes:

- The executable will only work on the same operating system you build it on (Windows, Mac, Linux)
- You may need separate builds for different operating systems
- Some antivirus software may flag unknown executables - you might need to explain this to your friends