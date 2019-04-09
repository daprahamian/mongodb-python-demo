# mongodb-python-demo
This web app connects to your MongoDB Atlas cluster and uses your data to populate the different web pages. 
It is designed to be a basic demo of how to interact with your data - so clone it, play around with it and 
tailor it to your data!

## Setup
This application requires Git and Python 3. Follow the setup instructions below for the relevant OS.

#####OSX
+ Install IDE of your choice
    + [Sublime](http://docs.sublimetext.info/en/latest/getting_started/install.html#id2)
    + [Eclipse](https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2019-03/R/eclipse-java-2019-03-R-macosx-cocoa-x86_64.dmg)
    + [IntelliJ Community](https://www.jetbrains.com/idea/download/#section=mac)
    + [Visual Studio Code](https://code.visualstudio.com/download)
+ Install HomeBrew
    + `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    + OR see detailed install instructions [here](https://docs.brew.sh/Installation)
+ Install Python3
    + Install [XCode](https://developer.apple.com/xcode/)
    + `brew install python`
    + Confirm that running `python3` outputs the correct version
+ If you haven't already installed git
    + `brew install git`
    + Create or login to your Github account [here](https://github.com/)
    + Follow instructions [here](https://gist.github.com/adamjohnson/5682757) to create a new SSH key for your Github account.
    + Restart terminal session for changes to take effect 
+ Clone this repo
    + `cd [wherever you want the repo]`
    + `git clone git@github.com:daprahamian/mongodb-python-demo.git`
    + OR see detailed instructions for cloning an existing repository [here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

#####Windows
+ Install IDE of your choice
    + [Sublime](http://docs.sublimetext.info/en/latest/getting_started/install.html#id1)
    + [Eclipse](http://docs.sublimetext.info/en/latest/getting_started/install.html#id1)
    + [IntelliJ Community](https://www.jetbrains.com/idea/download/#section=windows)
    + [Visual Studio Code](https://code.visualstudio.com/download)
+ Install Python3
    + Follow install instructions [here](https://realpython.com/installing-python/#windows)
    + Confirm that running `python` outputs the correct version
+ If you haven't already installed git
    + Follow Windows download instructions [here](https://git-scm.com/downloads)
    + Use all defaults EXCEPT for choosing `Git from the command line and 3rd party software` which will automatically 
    add Git to PATH
    + Follow instructions [here](https://gist.github.com/adamjohnson/5682757) to create a new SSH key for your (potentially new) Github account
    + Restart Command Prompt session for changes to take effect 
+ Clone this repo
    + `chdir [wherever you want the repo]`
    + `git clone git@github.com:daprahamian/mongodb-python-demo.git`
    + Or see detailed instructions for cloning an existing repository [here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Running the Application
This application runs on port 8080 by default.

For the application to connect to your cluster, you need to update the MONGODB_URL variable in 
[`server.py`](server.py) to point to your cluster. Once you've done this, run the following command to start the server:
```python
python3 server.py
```

or, depending on your setup:

```python
python server.py
```
Then, open your browser and navigate to `localhost:8080` and you should see the homepage.

## Dependencies
+ [python](https://www.python.org/) >=v3
+ [pip](https://pypi.org/project/pip/)
+ [pymongo](https://api.mongodb.com/python/current/) >=v3.7.2 (`python -m pip install pymongo`)
+ [bottle](https://bottlepy.org/docs/dev/) >=v0.12.16 (`python -m pip install bottle`)