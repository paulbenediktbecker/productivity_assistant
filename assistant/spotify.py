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

    def get_playlists_infos(*arg):
        sp = spotify._get_sp()
        playlists = sp.current_user_playlists()["items"]
        playlist_infos = {}

        for i, ls in enumerate(playlists):
            uri = ls["uri"]
            name = ls["name"]

            playlist_infos[i] = {"name":name, "uri":uri}

        return playlist_infos
    
    def play_playlist(uri):
        sp = spotify._get_sp()
        sp.start_playback(context_uri=uri)

    def play_beckersbeste(*arg):
        uri = "spotify:playlist:6SH6SCvMxJV7sozLRaPc4l"
        spotify.play_playlist(uri)
        
    def play_beckersbeste_cmds(*arg):
        return "PLAYLISTNAME BB"

    def play_studdybuddy(*arg):
        uri = 'spotify:playlist:0YfFzLGEcwBLAbUyAT8NEY'
        spotify.play_playlist(uri)
    
    def play_studdybuddy_cmds(*arg):
        return "PLAYLISTNAME STUDY"
    
    def play_adhd(*arg):
        uri = 'spotify:playlist:2RHfgparZ8PzI4tJnYtVof'
        spotify.play_playlist(uri)
        
    def play_adhd_cmds(*arg):
        return "PLAYLISTNAME ADHD"

    def shuffle(*arg):
        sp = spotify._get_sp()
        sp.shuffle(state=True)

    def shuffle_off(*arg):
        sp = spotify._get_sp()
        sp.shuffle(state=False)

        
    def choose_playlist(*arg):
        playlist_infos = spotify.get_playlists_infos()

        for i in playlist_infos:
            print(f"{i} : {playlist_infos[i]['name']}")
        print("___________________________")
        inp = input("Select index.\n")

        inp = int(inp.split()[0])
        return "PLAYLISTINDEX " + str(inp)
    
    def play_playlist_by_index(text):
        index = int(text.split(" ")[1])
        playlist_infos = spotify.get_playlists_infos()
        
        spotify.play_playlist(playlist_infos[index]["uri"])

    def play_playlist_by_keyword(text):
        keyword = text.lower().split(" ")[1]
        
        inner_trigger_dict={
        "bb":spotify.play_beckersbeste, 
        "study":spotify.play_studdybuddy,
        "adhd": spotify.play_adhd
        }
        inner_trigger_dict[keyword]()
        
        
    def _spotify_inner(text):
        split = text.split(" ")
        if len(split) > 1: #if its not only "list"
            second_word = split[1]

            inner_trigger_dict={
            "bb":spotify.play_beckersbeste_cmds, 
            "study":spotify.play_studdybuddy_cmds,
            "adhd": spotify.play_adhd_cmds
            }
        
        #return commands of chosen playlist
            if second_word in inner_trigger_dict:
                return inner_trigger_dict[second_word]()
        
        return spotify.choose_playlist() #get cmds from user input        
    





    

#spotify.prev_track()
#spotify.next_track()
#spotify.choose_playlist()





    
