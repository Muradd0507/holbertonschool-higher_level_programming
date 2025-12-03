#!/usr/bin/python3
import requests
import csv

# 1. Fetch və ekranda göstərmək
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()   # JSON → Python list
        for post in data:
            print(post["title"])  # hər postun title-i
    else:
        print("Request failed.")


# 2. Fetch və CSV-ə yazmaq
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        posts_list = []
        for post in data:
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        # CSV-ə yazmaq
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)

        print("posts.csv yaradıldı.")
    else:
        print("Request failed.")
