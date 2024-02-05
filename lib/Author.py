from .Article import Article

class Author:
    all_authors = [] # list of all authors that have inherited from this "author class"& keeps track of all authors

    def __init__(self, name):
        #Initializing the instance variables
        self._name = name
        self._articles = [] # list of articles that have inherited from this "author class"
        Author.all_authors.append(self) 
#The getter metods  to return the author's name& list of :-articles associated with the aurthor/list of unique magazines associated with the articles written by the author/
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine() for article in self._articles))
# The Add Article Method: Adds a new article to the author's list of articles
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article
#Topic Areas Method:Returns a list of unique topic areas (categories) associated with the magazines the author has written for. 
    def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines()))
# Contributing Authors Method: Returns a list of authors associated with the articles written by the author.

    def contributing_authors(self):
        return [article.author() for article in self._articles]