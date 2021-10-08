# BoardGameGeek Recommender System

## Table of Contents
---
1. Background
2. Problem Statement
3. Analysis Overview
4. Recommendations and Future Work
5. Python Libraries
6. Project Map
7. Sources

## Background
---
BoardGameGeek is the premier website for any board game enthusiast or someone merely looking for recommendations and reviews. In fact, googling "Board Game" or "Board Game Review" brings up the website as the top option. In the [website's own words](https://www.boardgamegeek.com/wiki/page/Welcome_to_BoardGameGeek): 
> 
    BoardGameGeek is an online resource and community that aims to be the definitive source for board game and card game content. The site is updated on a real-time basis by its large and still growing user base — more than two million registered users! — making the Geek the largest and most up-to-date place to get gaming information... BGG features reviews, ratings, images, play-aids, translations, and session reports from board game geeks around the world, as well as live discussion forums. 

Anyone looking for more information can use the [Guide to BoardGameGeek](https://www.boardgamegeek.com/wiki/page/Guide_to_BoardGameGeek#).

Surface level exposure to the topic of board games is still heavily limited to old classics that have usually not stood the test of time. For example, Monopoly is probably the most well known board game in the U.S. outside of Chess. Monopoly itself is rated 4.4/10 on BoardGameGeek and is primarily known for straining relationships and causing frustration. Recently, the interest in board games is rising due to new forms of advertisement like Kickstarter, online reviews, and let's play videos. There are also board game cafes and game stores that allow for public play for a small fee and programs like Tabletop Simulator that allows for online play. While these new avenues help assuage the previously mentioned issues of opportunity cost, it is still difficult to know if a game is simply worth playing.

## Problem Statement
---
Even with the recent emergence of video games and online entertainment, board games remain as a popular source of fun that are distinct due to the use of unique set pieces, rulesets, and colorful boards. They are usually played with a group of people and can be cooperative or competitive in nature. I believe that this medium is held back by several issues, especially due to the opportunity costs of both money and time. While basic party games range around $25 or less, highly rated board games can easily cost upwards of $50. In fact, the highest ranked game on BoardGameGeek, Gloomhaven, had an original retail price of $130-$150 on release. Timewise, board games can take a lot of emotional undertaking. Between reading the rules, setting up the game, and teaching other people, it can take half an hour or more before a board game is played, let alone fun. As a result, it is optimal to pick games that you believe are worth the effort before starting.

The main goal of this project is to use data gathered from BoardGameGeek in order to create a recommender system that provides board game recommendations based on personal interest. Users are recommended to have tried out a game or two from the top rankings of BoardGameGeek they find interesting and use this model to find recommendations. Can this model use data from BoardGameGeek to create appropriate recommendations for new board games?

## Analysis Overview
---
The bulk of this project consisted of properly scraping data from BoardGameGeek in order to gain three main datasets: ranked data containing the ids and rankings of top ranking games, categorical data containing information about each game, and user rating data containing usernames and ratings for each game. This was accomplished using a mix of mainly Selenium, BeautifulSoup, and requests libraries along with BoardGameGeek's built in API, the BGG XML API2. 
    
The model used for this project was a recommender system utilizing cosign similarity between games. Cosign similarity is a method to measure the angular distance between two vectors in order to see similarity in data. This distance spans from 0 to 1, with 1 indicating that both vectors are the same. This was accomplished by creating vectors on each BoardGameGeek user found utilizing the user rating data. A pivot table was created using the ratings and implemented into a sparse matrix in order to calculate the cosign distances. The libraries used for this process were Pandas, SciPy, and scikit-learn.

The model works using the BGG_recommender function in the modeling notebook. This function takes in a string input and searches through the ranked dataset for each game containing that input. If desired, the recommender can also be restricted to a specific game containing the exact name. The output is a list of the top 10 recommendations for the game based on cosign similarity and the list of categories regarding the input game.

## Conclusion
---
From analyzing various outputs of the model, the model was deemed successful. While the model doesn't directly reduce problems with time and money, it increases the chance of picking a worthwhile game. There was clear correlation between games and user ratings regarding measures of popularity, continuity, and category. The relative strength of the recommendations from the model was also demonstrated by the distance values as shown bygames in the same franchise.

## Recommendations and Future Work
---
I recommend that individuals interested in board games to research a few games on BoardGameGeek and use this model in order to try out some recommendations. The [website](https://boardgamegeek.com/advsearch/boardgame) contains a strong advanced search tool that sorts through specific categorical data.

For future work on this subject, I recommend adding filters to the recommendation output. A goal is to take aspects of the advanced search tool from BoardGameGeek and implement them into the model in order to make the model more self-sufficient rather than relying on the website. Another recommendation is to gather more data on games outside of the top 2000. Entertainment is largely subjective, and even though games may have low average ratings, the model utilizes collaborative data between users. As such, having additional games and user connections can strengthen the model. The recommender can also produce data on rank and average rating if desired as well.

## Python Libraries
---
* Pandas
* Numpy
* Requests
* Time
* BeautifulSoup
* Selenium
* xmltodict
* os
* Matplotlib.pyplot
* Seaborn
* Scipy.sparse
* Sklearn.metrics.pairwise.cosine_distances
* collections.Counter

## Project Map
---
|File |Location |Description |
|--- |--- |--- |
|Technical_Report.ipynb |./ | This notebook contains the technical report for this project. There is an executive summary and detailed procedure included within.
|01_Web_Scraping.ipynb |./code/ | This notebook contains the code required to web scrape BoardGameGeek.  **Important**: To properly run this notebook to collect the initial ranked data, a FireFox geckodriver and filepath is needed for Selenium to function.
|02_Cleaning.ipynb |./code/ | This notebook contains the code used to clean the data gathered from BoardGameGeek.
|03_EDA.ipynb |./code/ | This notebook contains the eda code completed on the ranked, categorical, and user rating datasets.
|04_Modeling.ipynb |./code/ | This notebook contains the model used in this project and examples of useful outputs regarding specific recommendations.
|rating_scrape.py |./code/ | This python file contains code for the script run in order to gather user ratings from BoardGameGeek.

## Sources
---
https://www.boardgamegeek.com/wiki/page/Guide_to_BoardGameGeek
https://www.boardgamegeek.com/wiki/page/Welcome_to_BoardGameGeek
https://boardgamesland.com/the-complete-history-of-board-games/
https://www.boardgamegeek.com/boardgame/1406/monopoly
https://boardgamegeek.com/advsearch/boardgame