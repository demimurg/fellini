import wikipedia
import pandas as pd
import os
from tqdm import tqdm
from pprint import pprint


def get_category(lis):
    for cat in lis:
        for cat_base in ["сюжет", "содержание"]:
            if cat_base in cat:
                return cat
    return None


wikipedia.set_lang("ru")

df = pd.read_csv(os.path.dirname(os.getcwd()) + "/datasets/kp250.csv", index_col="TOP")

broken = []
for i in tqdm(df.index):
    movie = df.loc[i, 'Title'].strip()
    year = df.loc[i, 'Year']

    page, plot = None, None
    for query in (f"{movie} (фильм, {year})", f"{movie} (фильм)", movie):
        try:
            page = wikipedia.page(query)
        except:
            continue

        for cat in ("Сюжет", "Содержание", "Описание сюжета", "Сюжет фильма"):
            plot = page.section(cat)
            if plot is not None:
                break

    if plot is None:
        broken.append((
            i, query,
            page.sections[:3] if page is not None else []
        ))
        continue
    df.loc[i, 'Meta'] = plot

df.to_csv("yoohoo.csv")
pprint(broken)
