# Silent-Speech
repo for jaw sensor analysis. Turns jaw motion signal into speech.



- Setup: 
    - create new folder for project
    - git init
    - git pull https://github.com/Gyrozaid/Silent-Speech
    - git remote add origin https://github.com/Gyrozaid/Silent-Speech

- Pull Requests:
    - create a new branch: git checkout -b new_branch_name
    - add all changes: git add .
    - commit changes: git commit -m "new commit message"
    - push changes: git push --set-upstream origin new_branch_name
        - git push if upstream already set

    - go to github and open the pull request
        - text when done so someone else can review and approve the merge into main

# Spotify  
## Python Environment Setup

### Creating an environment with venv
```
python3 -m venv 528_project
```

# Activate the virtual environment
# On Windows
```
528_project\Scripts\activate
```
# On macOS/Linux
```
source 528_project/bin/activate
```

# Install required packages
```
pip install python-dotenv
pip install spotipy
```

# Run the project
```
python Silent-Speech/Spotify/main.py
```