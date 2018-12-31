from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from .photocollection import Photo


class PhotoCollectionAzureTable:
    _connectionstring = ''

    def __init__(self, connectionstring):
        self._connectionstring = connectionstring

    def fetchall(self):
        table_service = TableService(connection_string=self._connectionstring)
        photos = table_service.query_entities('phototable').items
        [photo.pop('etag', None) for photo in photos]
        [photo.pop('Timestamp', None) for photo in photos]
        return photos

    def fetchone(self, objectID):
        table_service = TableService(connection_string=self._connectionstring)
        photos = table_service.query_entities('phototable',
                                              "RowKey eq '" + objectID + "'"
                                              ).items
        [photo.pop('etag', None) for photo in photos]
        [photo.pop('Timestamp', None) for photo in photos]
        if photos:
            return photos[0]
        return None

    def addone(self, photo):
        table_service = TableService(connection_string=self._connectionstring)
        photoAzure = photo
        photoAzure['PartitionKey'] = photo['taken']
        photoAzure['RowKey'] = photo['objectID']
        table_service.insert_entity('phototable', photoAzure)
