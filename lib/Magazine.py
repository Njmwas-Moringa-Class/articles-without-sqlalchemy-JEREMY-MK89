class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def contributors(self):
        return [article.author() for article in self._articles]

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all_magazines if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls.all_magazines for article in magazine._articles]
