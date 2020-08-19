# Project-Automation-Script
A script to initialize a directory for a new project and clone a basic boilerplate into it
The [HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate) was used for this project.

Note: A bin folder is create in /home/user_name directory to store the script
### Installation:
- Edit the **.env** file according to your required file path. It is set default to `~/$HOME/Desktop`
- Run the **command .sh** file in your terminal.
- Add `~/bin` to PATH so that you can use it anywhere.

```
    git clone https://github.com/devppratik/Project-Automation-Script.git
    ** Edit .env file Accordingly **
    sh command.sh
     ** Add ~/bin to path **
    nano ~/.zshrc (or nano ~/.bashrc)
     ** Add the line and save and exit**
    PATH=~/bin:$PATH
```

### Usage:
Just type create with folder name to initialize the project directory
```
create <folder-name> [flags]
```
**flags :**

-g, --git
To initialize git in the Project Folder with boilerplate and initial commit

-n, --nogit
To just copy the boilerplate. Git is not initialized

### Contribute:
If you find any errors or if there is a better way for the shell scripts do let me know and create a pull request