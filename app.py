from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')


print("I am gonna take your songs from liked list...")
liked_songs_dict = ytmusic.get_liked_songs(limit=100000)

id_list = []

for current_dict in liked_songs_dict["tracks"]:

    id_list.append(current_dict["videoId"])

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
