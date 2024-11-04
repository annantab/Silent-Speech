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

# Project Setup

### Step 1: Create a Virtual Environment
```bash
python3 -m venv 528_project_venv
```

### Step 2: Activate the Virtual Environment
- **On macOS/Linux:**
  ```bash
  source 528_project_venv/bin/activate
  ```
- **On Windows:**
  ```bash
  528_project_venv\Scripts\activate
  ```

## Installing Dependencies
Once the virtual environment is activated, install the following Python packages:

```bash
pip install python-dotenv
pip install spotipy
```

## Setting Up Spotify API
To control Spotify, you need to set up a Spotify Developer account and create an app.

### Step 1: Create a Spotify Developer Account
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.
2. Click on "Create an App" and fill in the required details.

### Step 2: Get Client ID and Client Secret
After creating the app, you'll find the **Client ID** and **Client Secret** on the app dashboard. 

### Step 3: Store Credentials
Create a `.env` file in the root directory of your project and add the following lines:

```plaintext
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

## Running the Project
To run the project and start controlling Spotify, use the following command:

```bash
python main.py
```

You will be prompted to enter commands such as **play**, **pause**, **resume**, **back**, and **skip**.
```
=======
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
