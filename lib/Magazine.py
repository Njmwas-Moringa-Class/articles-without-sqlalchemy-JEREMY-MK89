class Magazine:
     # Class variable to store all magazines
    all_magazines = []
#Initializing the instance variables
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
         # Append the new instance to the class variable
        Magazine.all_magazines.append(self)
#The getter metods  to return the  name of the magazine&the category of the magazine
    def name(self):
        return self._name

    def category(self):
        return self._category
#Contributors Method:contributors(self): Returns a list of contributors (authors) associated with the articles published in the magazine. I
    def contributors(self):
        return [article.author() for article in self._articles]
#Class Method (find_by_name) with/using the @classmethod decorator :find_by_name(cls, name): Takes a class parameter (cls) and a magazine name (name).
    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all_magazines if magazine.name() == name), None)
#Class Method (article_titles)with/using the @classmethod decorator :-article_titles(cls): Takes a class parameter (cls). It returns a list of article titles from all magazines.
    @classmethod
    def article_titles(cls, magazine_instance):
        return [article.title() for article in magazine_instance._articles]
