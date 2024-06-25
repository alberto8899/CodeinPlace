# ARMIN VAN BUUREN SPOTIFY 
# Brings the data from an artist based on country location and popularity of song

# Import spotipy library
# Import Spotify validation credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Use ID from APP and SECRET, include artist ID =   MATHAME artist
CLIENT_ID = 'deb0f49329464a9892e5a8fd87bfbc27'
CLIENT_SECRET = 'f1031855091e46ada3163de2a7ba5956'
ARTIST_ID = '0SfsnGyD8FpIN4U4WCkBZ5'

# Set up authentication
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get top tracks of an artist
def get_artist_top_tracks(artist_id, country='MX'):
    results = sp.artist_top_tracks(artist_id, country=country)
    for track in results['tracks']:
        print(f"Track: {track['name']} - Popularity: {track['popularity']}")

# Get top tracks for the specified artist
get_artist_top_tracks(ARTIST_ID)