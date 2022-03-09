from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')

print("I am gonna take your songs from liked list...")
liked_songs_dict = ytmusic.get_liked_songs(limit=100000)

id_list = []

for current_dict in liked_songs_dict["tracks"]:

    id_list.append(current_dict["videoId"])


def remove_dup(id_list, playlist_id_list):
    
    set_id_list = set(id_list)

    set_playlist_id = set(playlist_id_list)

    final_set = set_id_list.difference(set_playlist_id)

    final_list = list(final_set)

    return final_list



refresh_or_new = input('''
WELCOME!

If you want to create a new playlist from your liked list type "N"

If you want to refresh your playlist from your liked list type "R"

TYPE: ''')
print("******************************************")


if refresh_or_new == "N":

    title = input("Name of the new playlist: ")
    description = input("Add a description for your playlist: ")


    cont = True
    while cont:

        status = input("""
        **************

        If you want to make your playlist PUBLIC type "pub"

        If you want to make your playlist PRIVATE type "pri"

        Type: """)
        print("""
        **************

        """)

        if status == "pub":
            privacy_status = "PUBLIC"
            cont = False

        elif status == "pri":
            privacy_status = "PRIVATE"
            cont = False
        
        else:
            print("It is invalid please try again!")
            cont = True

    print("I am creating your new playlist please wait...")
    playlist_ID = ytmusic.create_playlist(title=title,description=description,privacy_status=privacy_status,video_ids=id_list)


    print(f"""
    --------------------------------------------------------------

    Successfully created the playlist! Here its id {playlist_ID}

    --------------------------------------------------------------
    """)

elif refresh_or_new == "R":

    playlist_id = input("Give the playlist id which is in the url: ")

    playlist_songs_dict = ytmusic.get_playlist(playlistId=playlist_id,limit=10000)

    playlist_id_list = []
    
    
    
    for current_dict in playlist_songs_dict["tracks"]:

        playlist_id_list.append(current_dict["videoId"])


    final_list = remove_dup(playlist_id_list=playlist_id_list,id_list=id_list)

    if final_list == []:
        print("Your playlist is up-to-date")

    elif final_list != []:
        ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=final_list, duplicates=False)
        print("Your playlist successfully refreshed.")