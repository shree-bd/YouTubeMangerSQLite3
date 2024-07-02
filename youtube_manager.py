import json
import time
import sqlite3

conn = sqlite3.connect('youtube.db')

cur = conn.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL) 
''')


def list_all_videos():
    print("\n")
    print("*" * 70)
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)


def add_video(name, duration):
    cur.execute("INSERT INTO videos(name,time) VALUES(?,?)", (name, duration))
    conn.commit()


def update_video_details(video_id, new_name, new_duration):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name, new_duration, video_id))
    conn.commit()


def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Welcome to YouTube Manager Application | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            duration = input("Enter the video time: ")
            add_video(name, duration)
        elif choice == '3':
            video_id = input("Enter the video id to be updated: ")
            name = input("Enter the new video name: ")
            duration = input("Enter the new video time: ")
            update_video_details(video_id, name, duration)
        elif choice == '4':
            video_id = input("Enter the video id to be deleted: ")
            delete_video(video_id)
        elif choice == '5':
            print("Thank you for using YouTube Manager")
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
