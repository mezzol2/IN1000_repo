class Bok:
    def __init__(self, title, author, publication_year):
        self._title = title
        self._author = author
        self._publication_year = publication_year

    def __str__(self):
        return f"{self._title} by {self._author} ({self._publication_year})"
    
    def hent_tittel(self):
        return self._title
    
    def hent_utgivelseaar(self):
        return self._publication_year