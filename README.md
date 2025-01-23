A virtual environment is a tool used to isolate specific python environments in a single machine,allowing you to work on multiple projects with different dependecies and pakages without conflict
<br>
This is specially useful when working on projects that have collective pakage version or pakages that are not compatible with each other
<br>
--> Creating a virtual environment
python -m venv  myenv(folder_name)
<br>
--> Activating the virtual environment
myenv\Scripts\activate.bat  (windows)
<br>
myenv/bin/activate (linux/mac)
<br>
myenv\Scripts\activate.ps1 (Power Shell)
<br>
--> Deactivating the virtual environment
deactivate

<br>
2-Requirement.txt:-
<br>
It is useful to have a requirement text file that contains all names and versions of all the pakages the project depends upon .This file can be used to install all the required pakages in a new environment
<br>
You can create this text file and automatically export the pakages and its versions in this text file and your friend can also automatically import and install all these pakages in another virtual environement.
<br>
--> Creating a requirement.txt file
<br>
pip freeze > requirement.txt
<br>
--> Installing pakages from the requirement.txt file
<br>
pip install -r requirement.txt
<br>
--->Note:-
<br>
1-The basic use for this is for creating our own seperate environment in python in which we want to use different pakages that may cause a conflict with  other pakages
<br>
2-We can also use this to share our project with other developers and they can easily install all
pakages required for the project by just running the command pip install -r requirement.txt
<br>