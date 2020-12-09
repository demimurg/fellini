import requests
import re
import os
import pandas as pd
from bs4 import BeautifulSoup
from tqdm.std import tqdm

reviews_kp_url = lambda idx: f"https://www.kinopoisk.ru/film/{idx}/reviews/?ord=rating"
review_list_api_url = lambda idx: f"https://kinopoiskapiunofficial.tech/api/v1/reviews?filmId={idx}&page=1"
review_api_url = lambda idx: f"https://kinopoiskapiunofficial.tech/api/v1/reviews/details?reviewId={idx}"

TOKEN = os.getenv("TOKEN")

def parse_reviews(idx):
    page = requests.get(reviews_kp_url(idx))
    soup = BeautifulSoup(page.content, "html.parser")

    reviews = []
    for block in soup.find_all("span", {"itemprop": "reviewBody"}):
        reviews.append(block.text.replace("\n\r\n", " "))

    return "\n---NEXT REVIEW---\n".join(reviews)

def load_reviews(idx):
    auth = {"X-API-KEY": TOKEN}
    
    resp = requests.get(review_list_api_url(idx), headers=auth).json()
    reviews = []
    for review in resp["reviews"][:10]:
        details = requests.get(review_api_url(review["reviewId"]), headers=auth).json()
        reviews.append(
            details["reviewTitle"] + " " + 
            details["reviewDescription"].replace("\r\n\r\n", " ")
        )

    return "\n---NEXT REVIEW---\n".join(reviews)

def main():
    df = pd.DataFrame(columns=[
        "ID", "Title", "Year",
        "Crew", "Plot", "Rating",
        "Country", "Reviews"
    ])

    kp250 = pd.read_csv("kp250raw.csv")
    for i, mov in tqdm(kp250.iterrows()):
        kp_id = re.findall("_(\d+).jpg", mov["url_logo"])[0]
        df.loc[i + 1] = [
            kp_id, mov["movie"], mov["year"],
            ", ".join([
                mov["director"], 
                mov["screenwriter"], 
                mov["actors"]]
            ).replace(";", ","),
            mov["overview"].replace(";", ","), 
            f'{mov["rating_ball"]:.2f}', 
            mov["country"], load_reviews(kp_id)
        ]

    
    df.to_csv("yoohoo.csv")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    main()
