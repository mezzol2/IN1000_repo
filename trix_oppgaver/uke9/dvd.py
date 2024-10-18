class Dvd:
    def __init__(self, title, producer, publication_number):
        self._title = title
        self._producer = producer
        self._publication_number = publication_number
    
    def __str__(self):
        return self._title
    
    def __eq__(self, other_film):
        if self._title == other_film._title:
            if self._producer == other_film._producer:
                if self._publication_number == other_film._producer:
                    return True
        
        return False