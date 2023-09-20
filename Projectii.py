import json

class Song:
    def __init__(self, artist, song_name, genre, year, duration):
        self.artist = artist
        self.song_name = song_name
        self.genre = genre
        self.year = year
        self.duration = duration

    def __str__(self):
        return f"Artist: {self.artist}\nSong: {self.song_name}\nGenre: {self.genre}\nYear: {self.year}\nDuration: {self.duration} seconds"

class MusicLibraryApp:
    def __init__(self):
        self.song_list = []

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_song()
            elif choice == '2':
                self.remove_song()
            elif choice == '3':
                self.show_songs()
            elif choice == '4':
                self.save_to_file()
            elif choice == '5':
                self.load_from_file()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\nMusic Application")
        print("1. Add new song")
        print("2. Remove one song")
        print("3. Show all songs")
        print("4. Save to file")
        print("5. Load from file")

    def add_song(self):
        artist = input("Enter artist name: ")
        song_name = input("Enter song name: ")
        lenght = input("Enter the lenght of the song: ")

        try:
            year = int(input("Enter release year: "))
            duration = float(input("Enter duration (seconds): "))
        except ValueError:
            print("Invalid input for year or duration. Please try again.")
            return

        if not artist or not song_name or not lenght:
            print("Artist name, song name, and genre cannot be empty.")
            return

        song = Song(artist, song_name, lenght, year, duration)
        self.song_list.append(song)
        print(f"{song_name} by {artist} added successfully!")

    def remove_song(self):
        if not self.song_list:
            print("No songs to remove.")
            return

        self.show_songs()
        try:
            choice = int(input("Enter the number of the song to remove: "))
            if 1 <= choice <= len(self.song_list):
                removed_song = self.song_list.pop(choice - 1)
                print(f"{removed_song.song_name} by {removed_song.artist} removed successfully!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_songs(self):
        if not self.song_list:
            print("No songs to show.")
            return

        for i, song in enumerate(self.song_list, start=1):
            print(f"{i}. {song.song_name} by {song.artist}")

    def save_to_file(self):
        filename = input("Enter filename to save: ")
        with open(filename, 'w') as file:
            song_data = [{'artist': song.artist, 'song_name': song.song_name, 'genre': song.genre, 'year': song.year, 'duration': song.duration} for song in self.song_list]
            json.dump(song_data, file)
        print(f"Songs saved to {filename} successfully!")

    def load_from_file(self):
        filename = input("Enter filename to load: ")
        try:
            with open(filename, 'r') as file:
                song_data = json.load(file)
                self.song_list = [Song(item['artist'], item['song_name'], item['genre'], item['year'], item['duration']) for item in song_data]
            print(f"Songs loaded from {filename} successfully!")
        except FileNotFoundError:
            print(f"{filename} not found.")

if __name__ == "__main__":
    app = MusicLibraryApp()
    app.run()
