class Article:
    all = []  # Class variable to store all Article instances

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title  
        Article.all.append(self) 

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if self._title is not None:
            return
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    all = []

    def __init__(self, name):
        self._name = None
        self.name = name  
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name is not None:
           return
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine = {article.magazine for article in self.articles()}
        return list(magazine) if magazine else None

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        categories = {article.magazine.category for article in self.articles()}
        return list(categories)


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Uses the name setter
        self.category = category  # Uses the category setter
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if len(value) < 2 or len(value) > 16:
            return
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = {article.author for article in self.articles()}
        return list(authors) if authors else None

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        counts = {author: authors.count(author) for author in set(authors)}
        result = [author for author, count in counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))