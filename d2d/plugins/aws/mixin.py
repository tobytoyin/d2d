import os

import boto3


class SessionMixin:
    def _create_session(self, access_key_id, secret_access_key):
        # we separate the session as another function
        # so that we can monkeypatch this in our tests
        access_key_id = os.environ.get("AWS_KEY", access_key_id)
        secret_access_key = os.environ.get("AWS_SECRET", secret_access_key)

        return boto3.Session(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
        )
