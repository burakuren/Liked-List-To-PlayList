from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')

liked_songs_dict = ytmusic.get_liked_songs(limit=800)

id_list = []

for current_dict in liked_songs_dict["tracks"]:

    id_list.append(current_dict["videoId"])

playlist_ID = ytmusic.create_playlist(title="DENEME",description="My Favs is a playlist now",privacy_status="PUBLIC",video_ids=id_list)

print(f"Successfully created the playlist here is id {playlist_ID}")
