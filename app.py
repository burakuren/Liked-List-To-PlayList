from ytmusicapi import YTMusic

YTMusic.setup(filepath="headers_auth.json",headers_raw="""accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
authorization: SAPISIDHASH 1646816790_1498164d6ca8e09cbf13b1299529af2d4a7105a9
content-length: 1773
content-type: application/json
cookie: VISITOR_INFO1_LIVE=AGj4iiKHF5Y; LOGIN_INFO=AFmmF2swRQIgJyRw4q-77KOrH30q5QBBTlRwl6fTQn4xMiDzPXJteQsCIQCNRGMS0EHItw4LQynTLnDu4YJTk-zRa8i9Zz0eXbTuhg:QUQ3MjNmeWpyd25jRjNzbVlKT1NXTEY1Y2NtdkdoS1c2MG1pZmNnS3BOaXZhZ3EyNlJOMWZ0S0czTlNtQ1VsUmFMSFdwYk4xZDJ5QjlrWE1YalJOWDZCRlJPV0VKZXV6SWRNQ1A2bXlHRkNKcGtXc3VxUE9Ea0JmSmdJRnlPOGVoVWhiWU0xS0ZfUDlHelpMeVRjS0JOM05sTVVCWkNENUJB; YSC=XdskBT2ZcV8; wide=1; SID=Hwj2I8FI4vO-ILX7rHtJftlxHiAbmNJRV_J4rxTZrSZe-q4WnkGDRIvWn_7H7HT3nzqtng.; __Secure-1PSID=Hwj2I8FI4vO-ILX7rHtJftlxHiAbmNJRV_J4rxTZrSZe-q4W9JAH4K8uPAicbdhcTqEPJg.; __Secure-3PSID=Hwj2I8FI4vO-ILX7rHtJftlxHiAbmNJRV_J4rxTZrSZe-q4Wtyc3G0IHRhwRqNqft_rMTw.; HSID=AyLRG4cN8ecD-Q3Qe; SSID=AJo0zTcRJqY92ShGg; APISID=aD28SyoueKvQfCku/AHtUSMqdNXuGFT6yJ; SAPISID=rMh7hoxruQDZHVUK/AyO9eaeYzCopJN1uU; __Secure-1PAPISID=rMh7hoxruQDZHVUK/AyO9eaeYzCopJN1uU; __Secure-3PAPISID=rMh7hoxruQDZHVUK/AyO9eaeYzCopJN1uU; PREF=f6=80&f4=4000000&tz=Europe.Istanbul&library_tab_browse_id=FEmusic_liked_playlists; SIDCC=AJi4QfGA-AP8rfVhjuJGn6Teje3QENbLarM2z3whm1pSsn3OrCp5ldbdyLKFNysxTK_7eyPOzQ; __Secure-3PSIDCC=AJi4QfGnx9XSShanWzBi0BOY1Ruuo7-FlLH2HAzAy1sG6LGus285aQAA7QsrQOx-oGEGVdZcLA
origin: https://music.youtube.com
referer: https://music.youtube.com/
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
sec-gpc: 1
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
x-goog-authuser: 0
x-goog-visitor-id: CgtBR2o0aWlLSEY1WSiU3KGRBg%3D%3D
x-origin: https://music.youtube.com
x-youtube-client-name: 67
x-youtube-client-version: 1.20220302.01.01""")


ytmusic = YTMusic('headers_auth.json')



liked_songs_dict = ytmusic.get_liked_songs(limit=800)

id_list = []

for current_dict in liked_songs_dict["tracks"]:

    id_list.append(current_dict["videoId"])

playlist_ID = ytmusic.create_playlist(title="Myfavs",description="My Favs is a playlist now",privacy_status="PUBLIC",video_ids=id_list)

print(f"Successfully created the playlist here is id {playlist_ID}")