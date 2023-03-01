from datetime import datetime, timedelta

from config import config

import oci
from oci.object_storage.models import CreatePreauthenticatedRequestDetails
class OracleDriver:
    def __init__(self) -> None:
        # Initialize object storage client
        self.object_storage_cli = oci.object_storage.ObjectStorageClient(config)
    
    # Get the name of the bucket where your videos are stored
    def get_objects_on_bucket(
        self, namespace: str, bucket_name: str, prefix: str)->list:
        # List all objects in the bucket
        objects = self.object_storage_cli.list_objects(
            namespace_name = namespace,
            bucket_name = bucket_name,
            prefix = prefix
        ).data.objects
        # Extract the URLs for the video files
        video_urls = []
        for obj in objects:
            video_url = self.object_storage_cli.create_preauthenticated_request(
                namespace_name=namespace,
                bucket_name=bucket_name,
                create_preauthenticated_request_details=CreatePreauthenticatedRequestDetails(
                    name=obj.name +"_"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    access_type="AnyObjectReadWrite",
                    bucket_listing_action="ListObjects",
                    object_name=obj.name,
                    time_expires=datetime.utcnow() + timedelta(hours=1)
                )
            )
            url = self.object_storage_cli.base_client.endpoint+\
            video_url.data.access_uri+ video_url.data.object_name
            video_urls.append(url)
            # https://objectstorage.us-ashburn-1.oraclecloud.com
            # /n/id916ejdksls/b/raw-storage-data/
            # o/videos%2Ftutorials%2Fbootcamp_engenharia_de_dados%2Faula-04-bootcamp-de-engenharia-de-dados.mp4?
            # time=1646220849&authToken=eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.
            # eyJzdWIiOiAiYXBpLWNsaWVudC0xLzI5ODgxMzI4L3Jhdy1zdG9yYWdlLWRhdGFiYXNlL3Jhdy1zdG9y
            # YWdlLWRhdGFiYXNlIiwgImV4cCI6IDE2NDYyMjA4NDl9.r6_hZqJUOxdOV0I9ODFgJr-cG56CmIWdAGOFB_6xJg8

        return video_urls[1:]
        