class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise Exception("Title must be between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        result = []
        for x in Article.all:
            if x.author == self:
                result.append(x)
        return result

    def magazines(self):
        m = []
        for a in self.articles():
            if a.magazine:
                if a.magazine not in m:
                    m.append(a.magazine)
        if len(m) > 0:
            return m
        else:
            return None

    def add_article(self, magazine, title):
        art = Article(self, magazine, title)
        return art

    def topic_areas(self):
        t = []
        for a in self.articles():
            if a.magazine:
                cat = a.magazine.category
                if cat not in t:
                    t.append(cat)
        if len(t) > 0:
            return t
        return None


class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise Exception("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) == 0:
            raise Exception("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise Exception("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        res = []
        for x in Article.all:
            if x.magazine == self:
                res.append(x)
        return res

    def contributors(self):
        auth = []
        for a in self.articles():
            if a.author:
                if a.author not in auth:
                    auth.append(a.author)
        if len(auth) > 0:
            return auth
        return None

    def article_titles(self):
        tit = []
        for a in self.articles():
            tit.append(a.title)
        if len(tit) > 0:
            return tit
        return None

    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            if a.author:
                if a.author in counts:
                    counts[a.author] = counts[a.author] + 1
                else:
                    counts[a.author] = 1
        res = []
        for author in counts:
            if counts[author] > 2:
                res.append(author)
        if len(res) > 0:
            return res
        return None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        counts = {}
        for article in Article.all:
            if article.magazine:
                if article.magazine in counts:
                    counts[article.magazine] += 1
                else:
                    counts[article.magazine] = 1
        if not counts:
            return None
        return max(counts, key=counts.get)