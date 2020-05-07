Technology-stack
---------------- 
Python, Beautiful Soup, Pandas, Matplotlib

Problem Statement
-----------------
- The IMDB site has its own ratings (on the scale of 10) and also Metacritic score (on the scale of 100).
- The requirement here is to analyze the distribution of these scores and observe patterns.
- We need to consider the top 1000 movies for a give time period, sorted descending on number of votes received.
- We will scrape the data for only those movies which have both IMDB and Metacritic scores.
- Next, we will process the scraped data and cleanse/prepare it to build analytics on top.
- Finally, we will plot a normal distribution grap to vis-a-vis compare the IMDB and Metacritic scores visually.

Implementation Highlights
-------------------------
- Since the requirement is to scrape a significant amount of data, the requests are split into equal volume and the code injects deliberate delays with each new request sent in.
