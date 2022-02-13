import json
import math
import argparse

from os import getenv
from algoliasearch.search_client import SearchClient
from dotenv import load_dotenv, find_dotenv

def load_json_index(index_path):
  '''Takes a path parameter for the products index json data
      Returns a json dict.
  '''
  with open(index_path, 'r') as json_file:
    data = json.load(json_file)
  return data

def markdown_products(data, category, percent):
  '''Takes the three parameters below and does a price markdown to a specific category
      in the index: 
      data: the index in json format 
      category: the category in the index to markdown
      percent: the markdown percentage.'''
  for i in data:
    if category in i['categories']:
        i['price'] = math.floor(i['price'] - round(i['price']*percent, 2))

parser = argparse.ArgumentParser(description='''This script will push the index data to an Algolia application 
                                                and will markdown a specific category value in index's "category" key.
                                                The default values for the script parameters are the following:
                                                -p, --path: data/products.json
                                                -c, --category: "Cameras & Camcorders"
                                                -m, --markdown: 20''')
parser.add_argument('-p', '--path',
                    default='data/products.json',
                    type=ascii,
                    help='the path to the data index',
                    metavar='')
parser.add_argument('-c', '--category', 
                    default='Cameras & Camcorders', 
                    type=ascii,
                    help='the category to markdown [if no category matches, no product will be marked down].', 
                    metavar='')
parser.add_argument('-m', '--markdown', 
                    default=20, 
                    type=int, 
                    help='the markdown percentage [0 > m <= 100].', 
                    metavar='')
args = parser.parse_args()
category = args.category.strip("'")
percentage = abs(args.markdown)/100
path = args.path.strip("'")

print(f'loading json index from {path}')
new_object = load_json_index(path)
print(f'processing markdowns for {category} markdown for {percentage*100}%')
markdown_products(new_object, category, percentage)

load_dotenv(find_dotenv())
ALGOLIA_APP_ID = getenv('ALGOLIA_APP_ID')
ALGOLIA_API_KEY = getenv('ALGOLIA_API_KEY')
ALGOLIA_INDEX_NAME = getenv('ALGOLIA_INDEX')

print(f'connecting to algolia app index: {ALGOLIA_INDEX_NAME}')
client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
index = client.init_index(ALGOLIA_INDEX_NAME)

# Assignment Part Three: Improve Relevance
index.set_settings({
  'searchableAttributes': [
    'name',
    'description'
  ],
  'customRanking': [
    'desc(rating)',
    'desc(popularity)'
  ],
  'attributesForFaceting': [
    'searchable(brand)',
    'categories',
    'price_range'
  ]
})

print('pushing index data')
res = index.save_objects(new_object)
res.wait()
print('finished')
