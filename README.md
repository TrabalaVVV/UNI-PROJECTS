# <b>UNI-PROJECTS</b> Viktor Varga 
This repository contains every code file for each project I have been a part of during my studies in the <b>University of Applied Science</b> in Amsterdam. 
As a part of the <b>Digital Driven Business</b> programmme we were tasked to transform/ analyze/ utilize datasets for a wide array of purposes. Ranging from simple analyses and visualization to building a recommender system. 
In this way I aim to represent my ability to conduct robust research for marketing purposes utilizing either or a combination of the techniques demonstrated in the files.

<i>Each of the folders and their contents are described and disected below:</i>

## Basic Recommender System

<b>Dataset:</b> [Yelp dataset](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset)

A recommender system built on the Yelp dataset using both KNN and SVD in the Suprise package. The dataset includes the relations in the form of a numeric review by a user to a restaurant.
The system is able to use these user reviews to recommend a set of restaurants to an individual user of the dataset based on the cosine distance (KNN) and collaborative filtering (SVD).  

## Master Thesis Survey Analysis

<b> Dataset:</b> Results of a [quantitative survey](https://www.linkedin.com/feed/update/urn:li:activity:7097200463053246466/) conducted by me

This notebook includes analysis of results of a qualitative survey regarding the use of Personalized Advertising Interfaces in Retail settings. 
These are devices that are present in brick and mortar stores, utilize customer data collected via different methods <i>(loyalty app, bioscanning camera)</i> to personalize the product offering to customer.

In my research I tried to answer a series of research questions tied to the perceived usefulness, perceived privacy risk of the two defined data <i>collection methods</i>. This was done utilzing common statistical methods i.e. regression analysis, uneven t-test and ANOVA.

## ML Algorithm tranining

<b> Dataset:</b> Metacritic movie dataset (provided by University)

In this notebook you can observe the result of collaboration of 4 students, each having assigned one type of ML Algorithm (Neural Network, Kmeans, DBScan, Random Forest). The dataset consisted of data regarding movies and movie ratings recorded on metacritic.com. We used these ML techniques trying to predict continuous variables (i.e. international box office). 

Each student was to choose one algorithm; I was in charge of working on Random Forest and KNN was an extra effort to achieve bonus points for the assignment (See "Project12_RF_KNN"). 
However, I am familiar with the other Algorithms as well.

## SQL Databse Python wrapper

<b> Dataset:</b> Metacritic movie dataset (provided by University)

This notebook demonstrates a basic wrapper for a PostgreSQL database. A snippet of data is pulled from the database using a cursor with an SQL command into the Python environment (pandas), then subsequently visualized. 

## Text tokenization and Sentiment Analysis

<b> Dataset:</b> A scrape done by a third-party ([Fanpage Karma](https://www.fanpagekarma.com/)) of 2,000 US theme park Facebook posts (e.g. post description, reactions, comments, shares).

The description text of these FB posts is then cleaned, tokenized and sorted into different types of posts depending on keywords. These types of posts are the subsquently compared with each other and otherwise used for analysis of user sentiment.

## Webscraping Amazon metacritic

<b> Target of scraping:</b> Amazon.com and metacritic.com

In this project, working with a group of 4 students, we were tasked with programming a spider to scrape product listing information about videogames on metacritic.com and Amazon.com. Focusing on metacrtic, I was able to scrape all relevant information on thousands of game titles using the Beatiful soup4 package (See "BS4_Scraper_Metacritic") . Additionally the scraper of my colleagues for Amazon is also included.


<i> Note: Parts of the code found in the above files were written by fellow students of mine, they are credited via comments above/next to the code section in question.</i> 
