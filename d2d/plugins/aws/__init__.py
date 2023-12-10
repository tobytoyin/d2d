from .s3_put import S3Put


class ServiceCatalog:
    put_objects = S3Put().put_objects
