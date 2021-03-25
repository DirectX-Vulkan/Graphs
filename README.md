# UI-Diagnostic

## Python
Download and install Python 3.9.2

### matplotlib
After installing python, open a commandline and run the following 2 lines:
```python -m pip install -U pip```
```python -m pip install -U matplotlib```

### PyInstaller
To compile the code, I've prepared the `COMPILE.py` script, which uses the PyInstaller library.
Run the following line to install it:
```python -m pip install -U PyInstaller```

## Visual Studio
You will need Visual Studio 2017 or later with the `Python development` module enabled (run Visual Studio Installer to check if it's enabled and enable it if not)

When you open the code in Visual Studio, it's recommended to open all files so Visual Studio's intellisense can recognize the other files and their contents

Another option is to use your IDE of choice for Python, but matplotlib will act differently in some IDEs, like PyCharm.
