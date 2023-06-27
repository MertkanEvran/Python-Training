import pandas as pd



class MusicRequestManager:

    def __init__(self):
        self.df = pd.read_csv("Pandas\\Datasets\\Spotify_Youtube.csv")

    def filter_by_energy(self,value):
        list = self.df[self.df["Energy"] > value]
        return list

    def filter_by_views(self,views):
        list = self.df[self.df["Views"] > views]
        return list

    def filter_by_albums(self,album):
        list = self.df[self.df["Album"] == album]
        return list

    def filter_by_speechiness(self,value):
        list = self.df[self.df["Speechiness"] > value]
        return list

    def filter_by_likes(self,likes):
        list = self.df[self.df["Likes"] > likes]
        return list
    
    def filter_by_artist(self,artist_name):
        list = self.df[self.df["Artist"] == artist_name]
        return list

    def get_spotify_url(self,song_list):
        return song_list["Url_spotify"]
    
    def get_youtube_url(self,song_list):
        return song_list["Url_youtube"]

    def get_count(self,song_list):
        return song_list.size
    
    def get_name(self,song_list):
        return song_list["Track"]
        

def filter_interface():
    manager = MusicRequestManager()
    print("Welcom to song suggestion application.\n\
          Please select your filter\n\
          1-) Search by energy\n\
          2-) Search by views\n\
          3-) Search by album\n\
          4-) Search by Speechiness\n\
          5-) Search by Likes\n\
          6-) Search by Artist\n")
    user_input = input("User input: ")
    if user_input == "1":
        value = int(input("İnput the energy(Must be between 0-100): ")) / 100
        print(value)
        song_list = manager.filter_by_energy(value)
        option_interface(song_list)
    elif user_input == "2":
        value = int(input("İnput the at least views number: "))
        song_list = manager.filter_by_views(value)
        option_interface(song_list)
    elif user_input == "3":
        value = input("İnput the album name: ")
        song_list = manager.filter_by_albums(value)
        option_interface(song_list)
    elif user_input == "4":
        value = int(input("İnput the speeechiness rate( Must be between 0-100): ")) / 100
        song_list = manager.filter_by_speechiness(value)
        option_interface(song_list)
    elif user_input == "5":
        value = int(input("İnput the at least like numbers: "))
        song_list = manager.filter_by_likes(value)
        option_interface(song_list)
    elif user_input == "6":
        value = input("İnput the artist: ")
        song_list = manager.filter_by_artist(value)
        option_interface(song_list)
    else:
        raise Exception("İnvalid input from filter intarface")

def option_interface(song_list):
    manager = MusicRequestManager()
    print("Which option do you want to learn\n\
          Please select your option\n\
          1-) Get names\n\
          2-) Get spotify links\n\
          3-) Get youtube links")
    user_input = input("User input: ")
    if user_input == "1":
        print(manager.get_name(song_list))
    elif user_input == "2":
        print(manager.get_spotify_url(song_list))
    elif user_input == "3":
        print(manager.get_youtube_url(song_list))
    else:
         raise Exception("İnvalid input from option intarface")
    
    
while True:    
    try:
        filter_interface()
    except Exception as ex:
        print(ex)