#my solution
import requests
from bs4 import BeautifulSoup
import pprint

links = []
subtext = []

for pageNum in range(1,3):
    res = requests.get(f'https://news.ycombinator.com/news?p={pageNum}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links.extend(soup.select('.storylink'))
    subtext.extend(soup.select('.subtext'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))

# #Andrei's solution
# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
#
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')
# links2 = soup2.select('.storylink')
# subtext2 = soup2.select('.subtext')
#
# mega_links = links + links2
# mega_subtext = subtext + subtext2
#
#
# def sort_stories_by_votes(hnlist):
#     return sorted(hnlist, key=lambda k: k['votes'], reverse=True)
#
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     return sort_stories_by_votes(hn)
#
# pprint.pprint(create_custom_hn(mega_links, mega_subtext))


#instruction:
#install beautiful soup (beautifulsoup4)
#BeautifulSoup allows us to use the html
#and grab different data, scrape it

#need requests library
#installed on computer, also need in IDE
#will use this a lot
#allows us to initially grab html file

# import requests
# from bs4 import BeautifulSoup
#
# #responseVariable = webBrowserW/OWindow('')
# #this is what google chrome is doing underneath the hood
# #trying to grab info from server
# res = requests.get('https://news.ycombinator.com/news')
# # print(res)
# # #got <Response [200]>
#
# # #in google chrome, view>developer>developer tools>network>
# # #refresh, news - html w/ all data
# # print(res.text)
# # #displays entire html file
# # #all we care about is the text (link and votes)
# # #we grabbed the data
# # #now use beautiful soup to clean up data
#
# #received all this html data as a string
# #beautiful soup allows us to parse
# #convert this from a string to an object that we can manipulate
# soup = BeautifulSoup(res.text, 'html.parser')
# #give beautifulsoup the string with data
# #and parse it, tell it the data needs to be modified into html
# #this gives us a soup object, assign it to a variable
#
# #we have to do 'html.parser' b/c beautiful soup also
# #parses another data, xml
# # print(soup.body)
# # print(soup.body.contents)
# # print(soup.find_all('div'))
# # print(soup.find_all('a')) #finds all 'a tags' (links) on page
# # print(soup.title)
# # print(soup.a) #first a tag that comes up
# # print(soup.find('a')) #finds the first thing, returns same as above
#
# # #go to website, right click a link>inspect
# # #gives us a html dom object with all info on page
# # #we want the a tag with the link and the title
# # #expand below that link to see score
# # #we want votes too, use id attribute
# # print(soup.find(id='score_23154886'))
#
# #one of the best ways to use soup object is to use select method
# #allows us to grab piece of data from soup we created
# #using a css selector, allows us to access the data using css selectors
# #different ways to grab elements on a html page
# # print(soup.select('a')) #selects all a tags
# # print(soup.select('div'))
#
# # #can go beyond an element
# # print(soup.select('.score')) #do it with dot notation
# # # . stands for a class
# # #grabbed all the span tags that have scores on them
#
# # print(soup.select('#score_23154886')) #use # for an id
# # #css selectors become very powerful when you select
# # #complicated nested elements
#
# #what do we want to do
# #want to grab the title and link of the stories that
# #have more than 100 points, filter out the rest
# # print(soup.select('.storylink'))
# # #grabs a tags (links for each one of the items/stories on the page
# # print(soup.select('.storylink')[0])
# # #this grabs just the first link
#
# links = soup.select('.storylink')
# votes = soup.select('.score')
# # print(votes[0]) #make sure it works
# # #links and votes, they are all in order
# # #we can keep chaining these
# # print(votes[0].get('id'))


# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.storylink')
# votes = soup.select('.score')
#
# def create_custom_hn(links, votes):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         href = links[idx].get('href', None)
#         #None is a default we are giving
#         #in case there is no link or a broken link
#         points = votes[idx].getText()
#         print(points)
#         #Andrei got a list index out of range error b/c
#         #it's possible that a story has no votes,
#         #so we have more links/titles than votes
#         #we need to make sure we only grab stories that
#         #have votes, add if statement
#         # hn.append(title)
#         # hn.append(href)
#         hn.append({'title': title, 'link': href})
#         #titles are useless w/o a link
#         #links are defined with an href attribute
#     return hn
#
# # print(create_custom_hn(links, votes))
# create_custom_hn(links, votes)


# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.storylink')
# # votes = soup.select('.score')
# #grab subtext instead of votes
# subtext = soup.select('.subtext')
#
# # def create_custom_hn(links, votes):
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#     #why did we enumerate? we have 2 lists, links and subtext
#     #only enumerating over links list, not subtext
#     #need idx to access subtext item
#     #links[idx] can be converted to item see below
#         # title = links[idx].getText()
#         # href = links[idx].get('href', None)
#         title = item.getText()
#         href = item.get('href', None)
#         # points = votes[idx].getText()
#         #need to convert to int and remove the word points
#         #do this to return a string and convert to number
#         vote = subtext[idx].select('.score')
#         #some cases may not have a vote so do this
#         if len(vote): #if array has no length will be false
#             #if true do this
#         #points = int(votes[idx].getText().replace(' points', ''))
#             points = int(vote[0].getText().replace(' points', ''))
#         # print(points)
#         # hn.append({'title': title, 'link': href})
#         #add vote to this
#         hn.append({'title': title, 'link': href, 'votes': points})
#     return hn
#
# # print(create_custom_hn(links, votes))
# # create_custom_hn(links, votes)
# # create_custom_hn(links, subtext)
# print(create_custom_hn(links, subtext))
# #built-in module we can use called pretty print


# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')
#
# #add function to sort stories from most to fewest votes
# def sort_stories_by_votes(hnlist):
#     # return sorted(hnlist)
#     #get error: TypeError: '<' not supported between
#     #instances of 'dict' and 'dict'
#     #since we are giving it a dictionary, we need to
#     #tell it what to sort by
#     #use lambda function
#     #whenever sorting dict use keys
#     #use this syntax w/ lambda and pass key you want to sort by
#     #add third parameter to sort in reverse
#     return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             #only care about articles w/ 100+ points
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     # return hn
#     return sort_stories_by_votes(hn)
#
# pprint.pprint(create_custom_hn(links, subtext))


# #how can we expand this list to include more than just
# #the first page of hn, scrape 1st 2 pages
# #?p=2
# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# links = []
# subtext = []
#
# for pageNum in range(1,3):
#     res = requests.get(f'https://news.ycombinator.com/news?p={pageNum}')
#     soup = BeautifulSoup(res.text, 'html.parser')
#     links.extend(soup.select('.storylink'))
#     subtext.extend(soup.select('.subtext'))
#
# def sort_stories_by_votes(hnlist):
#     return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     return sort_stories_by_votes(hn)
#
# pprint.pprint(create_custom_hn(links, subtext))