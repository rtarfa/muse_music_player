#import music_player
from song import song
from playlist import playlist
import library
#import pickle
from audioplayer import AudioPlayer as ap
import ytdownloader

#MAIN TODO: remove text when downloading (replace w "laoding"), fix playlist quit, get file to delete after quit(unless adding to a playlist),finish player visual
#new idea: GUI live cam viewer/app for diff animals/ (pandas, penguins)

#add functionality to delete playlist
#u can import itunes library?? maybe make that an option
#add error exceptions
#while input is not e (quit); loop

#can write to a file when add songs,playlists,etc
#add cover art!!
#transform to a webpage or google app etc
#try to get same button to pause/unpause!!
#fix: expects a command before playing next song

#note: use a linked list to fix the skip/quit issue (if skip play next, etc)
#faster than iterating thru a list

def menu():
    print("Welcome to Muse! What would you like to do?\n") #maybe put this outside the loop??
    print("a. Create a new empty playlist\n"
          "b. Add a song to an existing playlist\n"
          "c. View song library\n"
          "d. Play a song\n"
          "e. Play a playlist\n"
          "f. Quit")

loop = 1
arg = 0

while loop == 1:
    menu()
    arg= input()

    if arg=='a':
        titl=input("Playlist title: ")
        np=playlist(titl)
        library.playlists.append(np)
        with open('library.py','a') as f:
            f.write('\n'+titl+'=playlist("'+titl+'")')
            f.write('\nplaylists.append('+titl+')')
        print("Playlist added!")

    elif arg=='b':
        option='a'
        while option!='b':
            print("Which playlist?")
            print("Library: ")
            for pl in library.playlists:
                print(pl.title)
            playlist= input()
            st= input("Song title: ")
            ar= input("Artist: ")

            downl = True

            if downl == True:  # if not in library, download from youtube
                ytdownloader.download(st, ar)
                #get rid of printed text when downloads

            for pl in library.playlists:
                if playlist==pl.title:
                    playlist=pl
                for s in pl.your_playlist:
                    if s.title.lower() == st.lower() and s.artist.lower() == ar.lower():
                        downl = False

            pl.add(st,ar)

            with open('library.py','a') as f:
                f.write('\n'+pl.title+'.add("'+st+'",'+'"'+ar+'")')

            print("Song added!")
            option = input("What would you like to do? \n"
                           "a. Add another song \n"
                           "b. Return to main menu\n")

    elif arg=='c':
        option='a'
        while option!='b':
            print("Playlists:")
            for pl in library.playlists:
                print(pl.title)
            print("\n")
            playl = input("Playlist to view: ")
            for pl in library.playlists:
                if pl.title == playl:
                    if len(pl.your_playlist)==0:
                        print("--Empty--")
                    else:
                        pl.print()
            print("\n")
            option=input("What would you like to do? \n"
                  "a. View another playlist \n" #include option to delete from this playlist
                  "b. Return to main menu\n")

    elif arg=='d': #display playlist/available songs here
        # print("Playlists:")
        # for pl in library.playlists:
        #     print(pl.title)
        # print("\n")
        # print("a. View all songs")
        song= input("Song title: ")
        artist= input("Artist: ")
        downl=True
        for pl in library.playlists:
            for s in pl.your_playlist:
                if s.title.lower()==song.lower() and s.artist.lower()==artist.lower():
                    downl=False
        # if song(song,artist) in all_songs.all_songs:
        #         downl=False
        if downl==True: #if not in library, download from youtube
            ytdownloader.download(song, artist)

        curr_song = ap('song library/'+song.lower()+".mp3")
        command=None
        #include artist in filename (like "better_khalid.mp3" program it to save like this when download from youtube)
        while command!='q':
            command= input("Press a to play, p to pause, r to resume and q to quit.\n") #have a restart option?
            if command== 'a':
                curr_song.play() #loop=True
            elif command== 'p':
                curr_song.pause()
            elif command== 'r':
                curr_song.resume()
        curr_song.stop()
    elif arg == 'e':  #TODO: fix loop so that quit option works
        option = 'a'
        quit= False
        while option != 'b':
            print("Which playlist?")
            print("Library: ")
            for pl in library.playlists:
                print(pl.title)
            playlist = input()
            #print songs here
            # q=True
            for pl in library.playlists:
                if playlist == pl.title:
                    for song in pl.your_playlist:
                        curr_song = ap('song library/'+song.title.lower() + ".mp3")
                        print("Current song: "+ song.title + " by "+song.artist)
                        curr_song.play()
                        command=None
                        while command != 's': 
                            #expects a command before playing next song
                            command = input("Press p to pause, r to resume, s to skip, and q to quit.\n")
                            if command == 'p':
                                curr_song.pause()
                            elif command == 'r':
                                curr_song.resume()
                            # elif command == 'q':
                            #     q=True
                        #wait until song is done
                        curr_song.stop()
                        curr_song.close()
            option = input("What would you like to do? \n" #note: make sure this shows up after song finishes playing too
                           "a. Play another playlist \n"
                           "b. Return to main menu\n")
    elif arg=='f':
        loop=0


# def do_something(arg):
#     switcher= {
#         'a': playlist(input("Playlist title:")),
#         'c': print(library.playlists)
#     }
#     def do_something(arg):
#         func= switcher.get(arg,"nothing") #what does nothing mean??
#         return func()
# if/else/those c++ statements we used

#do_something(argument)
