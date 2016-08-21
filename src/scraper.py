from lxml import html, etree
import requests
import config

class Scraper:
    def __init__(self):
        self.page = requests.get(config["page"])
        self.tree = html.fromstring(self.page.content)

    def getGameList(self):
        self.games = self.tree.xpath(config["games_selector"])
        return self.games