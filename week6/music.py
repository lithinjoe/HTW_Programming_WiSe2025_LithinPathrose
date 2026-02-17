tracks = []
genres = {}
for i in range(3):
    s, g = input("Song: "), input("Genre: ")
    tracks.append((s, g))
    genres[g] = genres.get(g, 0) + 1
print("List:", tracks)
print("Counts:", genres)
