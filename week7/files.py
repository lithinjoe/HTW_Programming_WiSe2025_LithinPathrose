try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Wait, the file is not there!")
