

class Photo:
    def __init__(self):
        self.url = None,
        self.thumb = None,
        self.title = None,
        self.desc = None,
        self.taken = None,
        self.CRC = None


class PhotoCollection:
    def __init__(self):
        print('')

    def fetchall(self):
        raise NotImplementedError()

    def fetchone(self, objectID):
        raise NotImplementedError()

    def addone(self, photo):
        raise NotImplementedError()
