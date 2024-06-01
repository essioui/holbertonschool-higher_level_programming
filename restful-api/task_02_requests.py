#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(f"{post['title']}")
        else:
            print("Failed to fetch posts.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()

            posts_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

            with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
                writer.writeheader()
                writer.writerows(posts_data)


    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
