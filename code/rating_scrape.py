#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import libraries
import pandas as pd
import numpy as np
import requests
import time
import xmltodict

# Create directory
import os


# In[2]:


base_url = 'https://www.boardgamegeek.com/xmlapi2/thing?id='


# In[3]:


# Function to turn web data into a dataframe with all comments in a page
def comments_into_list(comments):
    rating_index = ['id', 'username', 'rating', 'value']
    test_df = pd.DataFrame(index = rating_index).T
    for comment in comments:
        data = {}
        try:
            data['username'] = comment['@username']
        except:
            pass
        try:
            data['rating'] = comment['@rating']
        except:
            pass
        try:
            data['value'] = comment['@value']
        except:
            pass
        test_df = test_df.append(data, ignore_index = True)
    return test_df

def list_into_df(game_id, parsed_text):
    # comments_into_list returns a dataframe with (generally) 100 rows * 4 columns with an empty id column
    comment_list = parsed_text['items']['item']['comments']['comment'] # len of comment_list should be 100 until last one
    comment_df = comments_into_list(comment_list)
    comment_df['id'] = game_id
    
    return comment_df

# Function to get one page of comments
def page_ratings(game_id, page_num):
    # Get url for use
    base_url = 'https://www.boardgamegeek.com/xmlapi2/thing?id='
    url = f'{base_url}{game_id}&ratingcomments=1&page={page_num}'
    
    # Get scraped page
    res = requests.get(url)
    parsed = xmltodict.parse(res.text)
    return parsed
#     return list_into_df(game_id, parsed)

# Function to get all ratings in a page
def all_page_scrape(game_id):
    page = 1
    all_comments = pd.DataFrame()
    while 'comment' in page_ratings(game_id, page)['items']['item']['comments']:
        all_comments = all_comments.append(list_into_df(game_id, page_ratings(game_id, page)), ignore_index=True)
        page += 1
        time.sleep(8)
    
    return all_comments

# In[10]:


# Function to get scraped rating into exported csv
def scrape_to_csv(game_id_list):
    
    # Create directory for csvs to go to
    try:
        os.mkdir('./game_ratings')
    except:
        pass
    
    # Scrape and export each id
    for game_id in game_id_list:
        print(game_id)
        rating_df = all_page_scrape(game_id)
        rating_df.to_csv(f'./game_ratings/{game_id}.csv')


# In[12]:


# Get desired ids
all_id = pd.read_csv('./scrape.csv', index_col=0)
ids = all_id['id']
# ids = ids[:]

# SCRAPE AWAY
scrape_to_csv(ids)

