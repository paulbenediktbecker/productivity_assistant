import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .secret import spotify_client_id, spotify_client_secret, spotify_user_id



class spotify(object):

    def __init__(self) -> None:
        pass

    def _get_sp():
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                    client_secret=spotify_client_secret,
                                                    redirect_uri="http://localhost:3000",
                                                    scope="user-modify-playback-state"))
        return sp
    
    def next_track(*arg):

        sp = spotify._get_sp()
        sp.next_track()

    def prev_track(*arg):
        sp = spotify._get_sp()
        sp.previous_track()

    def get_playlists(*arg):
        sp = spotify._get_sp()
        playlists = sp.current_user_playlists()["items"]
        return playlists
    
    def play_playlist(uri):
        sp = spotify._get_sp()
        sp.start_playback(context_uri=uri)

    def play_beckersbeste(*arg):
        uri = "spotify:playlist:6SH6SCvMxJV7sozLRaPc4l"
        spotify.play_playlist(uri)

    def play_studdybuddy(*arg):
        uri = 'spotify:playlist:0YfFzLGEcwBLAbUyAT8NEY'
        spotify.play_playlist(uri)
    
    def play_adhd(*arg):
        uri = 'spotify:playlist:2RHfgparZ8PzI4tJnYtVof'
        spotify.play_playlist(uri)

    def shuffle(*arg):
        sp = spotify._get_sp()
        sp.shuffle(state=True)

    def shuffle_off(*arg):
        sp = spotify._get_sp()
        sp.shuffle(state=False)




    def choose_playlist(*arg):
        playlists = spotify.get_playlists()

        playlist_infos = {}

        for i, ls in enumerate(playlists):
            uri = ls["uri"]
            name = ls["name"]

            playlist_infos[i] = {"name":name, "uri":uri}

            print(f"{i} : {name}")
        print("___________________________")
        inp = input("Select index.\n")

        inp = int(inp.split()[0])
        spotify.play_playlist(playlist_infos[inp]["uri"])
        






    

#spotify.prev_track()
#spotify.next_track()
#spotify.choose_playlist()





    
