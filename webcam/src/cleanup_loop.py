import time
import os
import glob


def delete_old_file(video_dir, delay=0):
    while True:
        # Get all files in the directory and their full paths
        files = glob.glob(os.path.join(video_dir, "*"))

        # Ensure the directory is not empty
        if files:
            # Find the oldest file by modification time
            oldest_file = min(files, key=os.path.getmtime)

            # Print the file that will be deleted
            print(f"Deleting the oldest file: {oldest_file}")

            # Delete the file
            os.remove(oldest_file)

        else:
            print("No files found in the directory.")

        time.sleep(delay)


if __name__ == "__main__":
    video_dir = "videos/"
    delete_old_file(video_dir, 4)
