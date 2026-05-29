def song_reader(path):
    with open(path, 'r', encoding ="UTF-8") as file:
        songs = file.readlines()
        for song in songs:
            print(song.strip())

song_reader("song_list.txt")
#---------------------------------------------------------------

def songs_sort(path1, path2):
    with open(path1, 'r', encoding = "UTF-8") as file2:
        album = file2.readlines()
    album = [line.strip() for line in album]
    album.sort()
    with open(path2,'w',encoding= "UTF-8") as file3:
        file3.writelines( "\n" .join(album))
            
songs_sort("song_list.txt","song_list2.txt")