# hackernews_scraper

This web scraping project is a tool to find the most popular/important stories (those with 100+ points) on the first two pages of the hacker news site.

Click here for a live, interactive version of the code:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kdhenderson/hackernews_scraper/master)
- Click on the 'New' dropdown button and select 'Terminal'
  - Run the program from the command line like this:
	$ python3 scrape.py

This is what the program does step-by-step:
  - Retrieves data from the first 2 pages of the the hacker news URL using the requests library get method.
  - Parsing the html with Beautiful Soup.
  - Creates lists of the links and the subtext (that contains the vote count) for each article with the appropriate CSS selectors using the select method.
  - Enumerates the links (to generate an index) and loops through them, grabbing the title of the article and the link to it with the getText and get methods.
  - Finds stories with votes using the index for each link, converts the vote count to an integer, and for articles that have 100 or more votes, adds the title, link and votes as a dictionary to a new list of hacker news articles to read.
  - Sorts the stories in decending order by the votes dictionary key using a lambda function. 
  - Uses the pretty print module to print the article list in more readable format.


Dependencies:
  - Install the requirements using pip install -r requirements.txt.
  - Make sure you use Python 3.
  - You may want to use a virtual environment for this.


Usage:
  - Run the program from the command line.
