import requests
import datetime as dt
import os
import slackweb
from bs4 import BeautifulSoup

def siitake(a, b):
    constellations = [
        "aries",
        "taurus",
        "gemini",
        "cancer",
        "leo",
        "virgo",
        "libra",
        "scorpio",
        "sagittarius",
        "capricorn",
        "aquarius",
        "pisces"
    ]

    constellations_kana = [
        "【おひつじ座】",
        "【おうし座】",
        "【ふたご座】",
        "【かに座】",
        "【しし座】",
        "【おとめ座】",
        "【てんびん座】",
        "【さそり座】",
        "【いて座】",
        "【やぎ座】",
        "【みずがめ座】",
        "【うお座】"
    ]

    base_url = "https://voguegirl.jp/horoscope/shiitake/"
    date = dt.date.today()
    slack = slackweb.Slack(url=os.environ["SLACK_URL"])

    for c, c_kana in zip(constellations, constellations_kana):
        url = base_url + c + "/" + date.strftime("%Y%m%d") + "/"
        res = requests.get(url)
        soup = BeautifulSoup(res.text)
        res.close()
        base_txt = soup.find("div", class_="a-text").text
        txt = c_kana + "\n\n" + base_txt.strip() + "\n\n続きはこちら⇒ " + url
        slack.notify(text=txt)