# Dependencies for running the assessment locally

I have implemented this assignment in a docker container. To start:

Clone the repo and open it using a docker container
Run the markdown.py script to process and transform the products.json index
Front-end app:
  Run npm install
  Run npm start

# Algolia TAM Assignment 
  
This is the hiring assignment for the TAM Team at Algolia. It’s intended to mimic work you might do here, while giving us an understanding of your skills in:  
  
* Coding
* Problem Solving
* Communication
  
If you want to know how we will judge the assignment, you can view our scoring rubric.  
  
## Brief
Spencer and Williams have provided us with raw product data and a repo of their front end code. They have asked us for help to enhance their implementation and have asked that we create an Algolia application to demonstrate this to them.

### Technical Assignment - Part One (1 hrs)
Spencer and Williams are having a sale on Cameras. They would like you create and run a demo script that reduces the price of everything in the camera category by 20% and then round to the lowest full number. They have provided the raw data as products.json . The data should be transformed and sent to algolia in a single script.  

--

Implemented a python script (markdown.py) that parses the products.json data and processes the markdowns for the category to transform the data.

I've added the option to change the path to the json index [-p, --path], category string [-c, --cateogy], and markdown percentage [-m, --markdown] to the script.

Some assumptions and possible improvements:
  I've removed the values in the .env file for privacy. The script is assuming that the reviewer will have an algolia application and supply their own API keys and index name.
  Possibly add a new key:value on the products index for the sale/markdown price for comparisons?
  Possibly add some more parameters to the script to be able to pick a specific key in the index to markdown (instead of limiting it to "category".

  
### Technical Assignment - Part Two (2 hrs)
Our customer Spencer and Williams want to use Personalisation in order to to do this they need to implement **_Algolia Insights_** . They have asked for us to create a demo of the events included in their provided codebase.  
  
It is imperative that we send clicks and conversion on the result page hit results, any other events included will be a bonus.  

--

The following javascript files have been modified: 
  results-page.js
    imported the following libraries for event handling: instantsearch.js/es/middlewares & search-insights

    refinementList:
      brand and categories facets (this is for Part Three of the assignment)
    
    _startSearch():
      function, I've added the insightsMiddleware and hooked it to the _searchInstance
  
  result-hit.js
    added bindEvent parameter to resultHit for binding the click and conversion events on the View and Add To Cart buttons respectively

Some assumptions and possible improvements:
  The event binding and sending are the deliverables. The View and Add To Cart buttons template implementations are out of scope for the assignment.
  A click event is assumed to be bound to the View button and the View button is supposed to call a modal or template to give more product data (description, shipping info, etc.).
  A conversion event is assumed to be bound to the Add To Cart button.
  Possibly add the click and conversion analytics data into the product hits on the frontend? Additionally, adding the rating field could help drive conversions.
  Possibly add an indicator for markdown items or a facet/filter option.
  
### Technical Assignment - Part Three (0.5 hrs)
Spencer and Williams want some guidance on their optimal relevance set up. In the Algolia index that you have uploaded the data and events to, configure the relevance so that when users are searching they are seeing the results that make most sense. 

--

Changes in the frontend application:
  added Price Range facet panel container index.html and Price Range widget results-page.js

Changes in the index configuration:
  added name and description as searchable attributes in the index
  added popularity and rating fields (descending - assuming higher rating value is better) as custom ranking attribute
  added brand (searchable), categories, and price range attributes as facets

Possible improvements:
  Implement the hierarchical menu for the categories facet to narrow down to the deeper levels of hierarchicalCategories
  Possibly modify the "no keyword" search to display the most popular and highest ranked items in the index
  
### Questions (0.5 hrs)
  
Please answer example customer questions in the questions directory.  
  
## Getting started
  
1. You'll need to sign up for an Algolia account @ https://www.algolia.com/users/sign_up.  
2. You can find the product dataset in the data folder inside this repo. Feel free to use any language to perform the data transformation  
3. To run the front end of the application you will need to add your app id, api key and index name to the file .env.test and rename it .env. Once added run `npm install` & `npm start` to see the UI  
  
Everything you need to complete this assignment can be found on algolia.com/docs.  
  
## How to submit
1. Push your code into a code sandbox and share it with us  
2. Reply to our email with a link to your code sandbox, and anything else you think is applicable  
  
## Scoring Rubric
  
### Technical Assignment
  
| Did the candidate: | Yes | No |
| :------------- | :------------- | :------------- |
| Follow the instructions of the assignment? | | |
| Write code that follows best-practices? | | |
| Avoid over-engineering? | | |
| Demonstrate understanding of the code they wrote? | | |
| Demonstrate good code and process organization? | | |
| Complete the assignment in an efficient manner? | | |
| Ask for clarification when necessary? | | |
  
### “Customer” Questions

| Did the candidate: | Yes | No |
| :------------- | :------------- | :------------- |
| Answer the questions correctly? | | |
| Answer in a succinct manner? | | |
| Have minimal spelling, grammar, or formatting mistakes? | | |
| Employ a friendly, helpful tone? | | | |

### Overall Impressions

| Does the candidate demonstrate being in the top 10% of: | Yes | No |
| :------------- | :------------- | :------------- |
| Technical aptitude | | |
| Problem Solving | | |
| Communication skills | | | |
