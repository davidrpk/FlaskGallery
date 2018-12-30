

class PhotoCollection:
    def __init__(self):
        print('')

    def fetchall(self):
        raise NotImplementedError()

    def fetchone(self, objectID):
        raise NotImplementedError()

    def addone(self, photo):
        raise NotImplementedError()
