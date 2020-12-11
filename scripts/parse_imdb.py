import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import os


top250url = lambda tok: "https://imdb-api.com/API/Top250Movies/" + tok
movie_url = lambda tok, idx: "https://imdb-api.com/en/API/Title/" + tok + "/" + idx
reviews_url = lambda idx: "https://www.imdb.com/title/" + idx + "/reviews"


tokens = os.getenv("TOKENS").split(", ")
output_file = "../datasets/yoohoo.csv"
reviews_max_number = 10


def get_reviews(mov_id):
    page = requests.get(reviews_url(mov_id))
    soup = BeautifulSoup(page.content, "html.parser")

    reviews, reserve_reviews = [], []
    for container in soup.find_all("div", class_="review-container"):
        if len(reviews) == reviews_max_number:
            break
        if not container.find("span", class_="spoiler-warning"):
            reserve_reviews.append(container.find("div", class_="text").text)
        reviews.append(container.find("div", class_="text").text)

    if len(reviews) < reviews_max_number:
        reviews += reserve_reviews[:reviews_max_number - len(reviews)]

    return "\n---NEXT REVIEW---\n".join(reviews)


def main():
    token = tokens[0]

    df = pd.DataFrame(columns=[
        "ID", "Title", "Year",
        "Crew", "Plot", "Meta",
        "Duration", "Rating",
        "Genre", "Country", "Reviews"
    ])

    top250 = requests.get(top250url(token)).json()["items"]

    for i, mov in tqdm(enumerate(top250)):
        extra = requests.get(movie_url(token, mov["id"])).json()
        if extra["errorMessage"]:
            token = tokens[tokens.index(token) + 1]
            extra = requests.get(movie_url(token, mov["id"])).json()
        if extra["writers"] is not None:
            mov["crew"] += ", " + extra["writers"]

        df.loc[i + 1] = [
            mov["id"], mov["title"], mov["year"],
            mov["crew"], extra["plot"], extra["keywords"],
            extra["runtimeMins"], mov["imDbRating"],
            extra["genres"], extra["countries"],
            get_reviews(mov["id"])
        ]

    df.to_csv(output_file)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    main()
