from datetime import datetime, timedelta

from config import *

import oci
from oci.object_storage.models import CreatePreauthenticatedRequestDetails
from flask import Flask, jsonify
from flask_cors import CORS

from oracle_driver import OracleDriver

app = Flask(__name__)
CORS(app)


# Initialize object storage client
object_storage_cli = oci.object_storage.ObjectStorageClient(config)
# Get the name of the bucket where your videos are stored
bucket_name = "raw-storage-data"
namespace_name = "id916ejdksls"
prefix = "videos/tutorials/bootcamp_engenharia_de_dados/"

# Define endpoint to fetch videos
@app.route('/api/videos')
def get_videos():
    videos_url = OracleDriver().get_objects_on_bucket(namespace_name, bucket_name, prefix)
    if not videos_url:
        return jsonify({
            'videos': [],
            'message': 'No videos found',
            'status_code': 404
        })

    # Return the video URLs as a JSON response
    return jsonify({
        'videos': videos_url,
        'status_code': 200,
    })

if __name__ == '__main__':
    app.run(debug=True)
