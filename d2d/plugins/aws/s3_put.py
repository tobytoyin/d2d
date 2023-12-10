import logging
import os

from d2d.contracts.documents import Document

from .mixin import SessionMixin


class S3Put(SessionMixin):
    def put_objects(
        self,
        document: Document,
        /,
        put_prefix: str = "",
        bucket_name: str,
        access_key_id: str | None = None,
        secret_access_key: str | None = None,
    ):
        session = self._create_session(access_key_id, secret_access_key)
        s3 = session.client("s3")

        paths = document.obj_refs.paths
        prefix = document.obj_refs.prefix

        if paths is None:
            return

        for f in paths:
            path = os.path.join(prefix, f)
            put_path = os.path.join(put_prefix, f)
            s3.upload_file(path, bucket_name, put_path)
            logging.info("uploaded: %s", path)
