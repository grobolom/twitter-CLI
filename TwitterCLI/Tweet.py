class Tweet:
    def __init__(self, author, text, _id=None):
        self.author = author
        self.text = text

        if _id:
            self._id = _id
