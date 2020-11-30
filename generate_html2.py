import pandas as pd
from datetime import date
DATE = str(date.today().strftime('%b %Y'))

from card import card
from body import body


def make_entry(news, color):
    string = card
    string = string.replace("THIS_IS_WHERE_IMAGE_GOES", news["Image"])
    string = string.replace("THIS_IS_WHERE_THE_TITLTE_GOES", news["Description"])
    string = string.replace("THIS_IS_WHERE_THE_TEXT_GOES", news["Intro"])
    string = string.replace("THIS_IS_COLOR", color)
    string = string.replace("THIS_IS_WHERE_THE_LINK_GOES", news["Link"])
    string = string.replace("THIS_IS_WHERE_THE_TYPE_GOES", news["Type of content"])
    return string

def make_body(news_list):
    color_i = -1
    colors = ["5FC3EB","007EAF"]
    string = ""
    for _,news in news_list.iterrows():
        color_i = (color_i+1)%2
        string += make_entry(news, colors[color_i])
    return string


if __name__ == "__main__":

    news_df = pd.read_csv('ACM - News proposal form (réponses).csv')
    string = make_body(news_df)

    page = body
    page = page.replace("THIS_IS_WHERE_CARD_GOES", string)

    f = open(f"newsletter_{DATE}.html", "wt")
    f.write(page)
    f.close()
