# UI-Diagnostic
This project will help you visualise the generated data. You need to place all the generated .csv data in a subfolder /data to work.

**You can skip all these step below if you just want to use the compiled .exe**

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

To compile you need to run `py COMPILE.py` and your .exe will be ready to go in dist folder.
## Visual Studio
You will need Visual Studio 2017 or later with the `Python development` module enabled (run Visual Studio Installer to check if it's enabled and enable it if not)

When you open the code in Visual Studio, it's recommended to open all files so Visual Studio's intellisense can recognize the other files and their contents

Another option is to use your IDE of choice for Python, but matplotlib will act differently in some IDEs, like PyCharm.

## Getting the project running
This project excpects to have a subfolder /data where all the .csv files are located. Where it will read all the files in that folder and generates charts for them.
