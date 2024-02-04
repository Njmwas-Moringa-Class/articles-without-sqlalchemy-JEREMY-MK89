#!/usr/bin/env python3
import sys
import ipdb

sys.path.append("/root/articles-without-sqlalchemy-JEREMY-MK89")

from lib.Author import Author
from lib.Article import Article
from lib.Magazine import Magazine

if __name__ == '__main__':
    # WRITE YOUR TEST CODE HERE

    # Test Author
    author1 = Author("John Doe")
    print(author1.name())
    article1 = author1.add_article(Magazine("Tech Magazine", "Technology"), "Introduction to Python")
    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())

    # Test Magazine
    magazine1 = Magazine("Tech Magazine", "Technology")
    print(magazine1.name())
    print(magazine1.category())
    print(magazine1.contributors())
    print(Magazine.find_by_name("Tech Magazine"))
    print(Magazine.article_titles(magazine1))  
    print(Magazine.contributing_authors(magazine1)) 

    # Test Article
    print(article1.title())
    print(article1.author())
    print(article1.magazine())

    # DO NOT REMOVE THIS
    ipdb.set_trace()
