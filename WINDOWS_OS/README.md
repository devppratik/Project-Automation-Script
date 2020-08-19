Note:
- A bin folder is create in C:\Users\user_name\Documents directory to store the script
- It is assumed you have git and pyhton installed. If not install them first
### Installation
- Edit the **.env** file according to your required file path. It is set default to `C:\`
- Run the **initialize.bat** file in the CMD as administrator.
- Restart CMD for the changes to take place
```
    git clone https://github.com/devppratik/Project-Automation-Script.git
    ** Edit .env file Accordingly **
    ** Open CMD as Administrator **
    cd /D "Full Path to the cloned git folder"
    initialize.bat
```

### Usage
Just type create with folder name to initialize the project directory
```
create <folder-name> [flags]
```
**flags :**

-g, --git
To initialize git in the Project Folder with boilerplate and initial commit

-n, --nogit
To just copy the boilerplate. Git is not initialized
