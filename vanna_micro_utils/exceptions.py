class ArticleCreationFailed(Exception):
    """Raise when creating an article fails"""

class AuthorCreationFailed(Exception):
    """Raise when creating an article fails"""

class FileUploadFailed(Exception):
    """Raise when file uplaods fail to S3"""


class InvalidResourceId(Exception):
    """ Raise when the ID is mal formed """

class ResourceNotFound(Exception):
    """ Raise when an article isn't found """

class AssetNotFound(Exception):
    """ Raise when a requeted file name asset doesn't exist on the resource"""