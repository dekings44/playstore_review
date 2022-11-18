from google_play_scraper import app, Sort, reviews, reviews_all
import pandas as pd
import numpy as np

reviews = reviews_all(
    'com.hikingproject.android',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='NG', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    #filter_score_with=5 # defaults to None(means all score)
)

opay_data = pd.json_normalize(reviews)
opay_data.to_csv('opay.csv', index = None)

print(opay_data.head())