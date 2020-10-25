import scrapy
import csv
import pandas as pd
import pymongo
import json
import os
from pymongo import MongoClient


class ShopcluesSpider(scrapy.Spider):
    # name of spider
    name = 'shopclues'

    start_urls = [
        'https://www.sheypoor.com/ایران/موبایل-تبلت-لوازم/موبایل-تبلت']

    def parse(self, response):
        # Extract product information
        titles = response.css('img::attr(title)').extract()
        prices = response.css('.item-price::text').extract()
        print(type(titles))
        print(type(prices))
        dict = {'title': titles, 'price': prices}
        df = pd.DataFrame(dict)
        df.to_csv('GFG.csv', encoding='utf-8-sig')
        #myclient = pymongo.MongoClient()

        # df = pd.read_csv('GFG.csv', encoding='utf-8-sig')   # loading csv file
        # saving to json file
        # df.to_json('jsonfile.json')
        # loading the json file
        #jdf = open('jsonfile.json').read()
        #data = json.loads(jdf)
        client = MongoClient('localhost', 27017)
        db = client['name_of_database']
        collection = db['name_of_collection']
        collection.insert(dict)
