import time
from os import walk


if __name__ == "__main__":
    # loop infinite and and then sleep for 4 seconds
    while True:
        print("[log]: loop started")

        # put all filesnames in directory "videos/: into a list
        filenames = next(walk("videos/"), (None, None, []))[2]  # [] if no file

        # if filenames is not empty do something if empty contineu
        if not filenames:
            print("[log]: no files in filename")
        else:
            print(filenames)
            break

        time.sleep(4)
    print("yo")
