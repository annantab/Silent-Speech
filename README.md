# Silent-Speech
Repository for jaw sensor analysis, transforming jaw motion signals into speech.

## Setup
1. Create a new folder for the project:
   ```bash
   mkdir Silent-Speech
   cd Silent-Speech
   ```
2. Initialize a new Git repository:
   ```bash
   git init
   ```
3. Pull the repository from GitHub:
   ```bash
   git pull https://github.com/Gyrozaid/Silent-Speech
   ```
4. Set the remote origin:
   ```bash
   git remote add origin https://github.com/Gyrozaid/Silent-Speech
   ```

## Pull Requests
1. Create a new branch:
   ```bash
   git checkout -b new_branch_name
   ```
2. Stage all changes:
   ```bash
   git add .
   ```
3. Commit changes:
   ```bash
   git commit -m "new commit message"
   ```
4. Push changes (for the first push to the new branch):
   ```bash
   git push --set-upstream origin new_branch_name
   ```
   - If the upstream is already set, use:
     ```bash
     git push
     ```

5. Open a pull request on GitHub:
   - Go to the repository on GitHub and create a new pull request.
   - Notify the team when the pull request is ready for review and approval before merging into `main`.

# Spotify Setup

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
SPOTIPY_REDIRECT_URI=your_redirect_uri
```

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

# Running the Project

```
python Silent-Speech/Spotify/main.py
```

You will be prompted to enter commands such as **play**, **pause**, **resume**, **back**, and **skip**.

