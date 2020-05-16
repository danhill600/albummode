#!/usr/bin/env python3
import time
import mpd

def connect_client():
    """Connect to MPD Client"""
    client = mpd.MPDClient()
    client.connect("localhost", 6600)
    return client

def get_pl_tuples(client):
    pl_tuples = []
    for song in client.playlistinfo():
        mytuple = (song["id"], song["album"])
        pl_tuples.append(mytuple)
    return pl_tuples

def get_id_of_album_start(client, album):
    pl_tuples = get_pl_tuples(client)
    for song in pl_tuples:
        if song[1] == album:
            return song[0]

def check_for_new_album(album, client):
    """See if a new album is playing and if so reset the variable"""
    try:
        currentalbum = client.currentsong['album']
    except:
        currentalbum = 'Not Sure'
    if currentalbum == album:
        print( "no new album.")
        return False
    else:
        print( "new album.")
        return True


client = connect_client()

#get current album
album = client.currentsong()['album']
print(album)

#get id of of current album's first song
firstAlbumSong = get_id_of_album_start(client, album)
print(str(firstAlbumSong))

#while loop to stay on that album

while True:
    for line in client.idle():
        if (client.currentsong()['album']) == album:
            print("same album")
        else:
            print("different album")
            client.playid(firstAlbumSong)
