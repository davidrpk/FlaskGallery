from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from .photocollection import Photo


class PhotoCollectionAzureTable:

    def __init__(self):
        print('')
  
    def addone(self, photo):
        #this expects photo to be an object not a json string
        table_service = TableService(connection_string="")
        photo_dict = vars(photo)
        photo_dict['PartitionKey'] = photo.taken
        photo_dict['RowKey'] = photo.CRC
        print(photo_dict)
        table_service.insert_entity('phototable', photo_dict)
