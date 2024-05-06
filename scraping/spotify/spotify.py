import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

url = 'https://www.billboard.com/charts/hot-100/'
date = input('what is the exact date would u like to travel to? (YYYY-MM-DD:)')

responce = requests.get(url+date)

soup = BeautifulSoup(responce.text, 'html.parser')
all_songs = soup.select('li ui li h3')
song_titles = [song.getText().strip() for song in all_songs]

# 1. need to signin to spotify pl
# 2. then go to this the developer dashboard "https://developer.spotify.com/dashboard/" and create a new spotify app
# 3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.

# entering spotify
sp = spotipy.Spotify(
  auth_manager=SpotifyOAuth(
      scope="playlist-modify-private",
      redirect_uri="http://example.com",
      client_id='YOUR UNIQUE CLIENT ID',
      client_secret='YOUR UNIQUE CLIENT SECRET',
      show_dialog=True,
      cache_path="token.txt",
      username='YOUR SPOTIFY DISPLAY NAME',
  )
)
user_id = sp.current_user()["id"]
year = date.split("-")[0]
# Search Spotify for the Songs from Step 1

user_id = sp.current_user()["id"]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)