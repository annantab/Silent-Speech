import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env (You have to ask me directly for those)
load_dotenv()

# Scope variable to access all the Spotify functionalities 
scope = "ugc-image-upload, user-read-playback-state, user-modify-playback-state, user-follow-modify, user-read-private, user-follow-read, user-library-modify, user-library-read, streaming, user-read-playback-position, app-remote-control, user-read-email, user-read-currently-playing, user-read-recently-played, playlist-modify-private, playlist-read-collaborative, playlist-read-private, user-top-read, playlist-modify-public"

# Create Spotify object with OAuth authentication 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope, 
    client_id=os.getenv("SPOTIPY_CLIENT_ID"), 
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"), 
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI")), 
    requests_timeout=300
)

# Function to get Spotify device (need to have Spotify Premium open on your mac for this to work)
def get_active_device():
    devices = sp.devices()
    if not devices['devices']:
        print("No devices found.")
        return None
    for device in devices['devices']:
        if device['is_active']:
            print(f"Found active device: {device['name']} with ID: {device['id']}")
            return device
    print("No active devices found.")
    return None

# Function to control Spotify playback based on command
def control_spotify(command):
    device = get_active_device()
    if not device:
        print("No active device found. Please make sure you have an active Spotify device.")
        return
    
    device_id = device['id']

    try:
        if command == 'play':
            sp.start_playback(device_id=device_id)
        elif command == 'pause':
            sp.pause_playback(device_id=device_id)
        elif command == 'back':
            sp.previous_track(device_id=device_id)
        elif command == 'skip':
            sp.next_track(device_id=device_id)
        else:
            print('Unknown command')
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify exception: {e}")

# Infinite loop to collect commands from the user
while True:
    command = input("Enter Spotify command (play, pause, resume, back, skip): ").strip().lower()
    control_spotify(command)
