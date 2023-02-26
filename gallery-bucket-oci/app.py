from flask import Flask, jsonify
from flask_cors import CORS
import oci

app = Flask(__name__)
CORS(app)

# Set up OCI SDK
config = oci.config.from_file()

# Define endpoint to fetch videos
@app.route('/api/videos')
def get_videos():
    # Initialize object storage client
    object_storage = oci.object_storage.ObjectStorageClient(config)

    # Get the name of the bucket where your videos are stored
    bucket_name = 'your-bucket-name'

    # List all objects in the bucket
    objects = object_storage.list_objects(bucket_name).data

    # Extract the URLs for the video files
    video_urls = []
    for obj in objects:
        video_url = object_storage.generate_presigned_url(
            'get_object',
            namespace_name=config["namespace"],
            bucket_name=bucket_name,
            object_name=obj.name,
            expiration_time=3600  # Link is valid for 1 hour
        )
        video_urls.append(video_url)

    # Return the video URLs as a JSON response
    return jsonify(video_urls)
