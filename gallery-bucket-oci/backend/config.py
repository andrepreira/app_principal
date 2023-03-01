import os
import oci
from dotenv import load_dotenv

# environment variables
load_dotenv(str(os.getenv("PWD"))+"/env.dev")

config = {
    "user": os.getenv("USER_OCID"),
    "key_file": os.getenv("PRIVATE_KEY_PATH"),
    "fingerprint": os.getenv("FINGERPRINT"),
    "tenancy": os.getenv("TENANCY_OCID"),
    "region": os.getenv("REGION"),
    "log_requests": True
}

try:    
    print(config)
    oci.config.validate_config(config)
except oci.exceptions.InvalidConfig as e:
    print(f"Config file not found {e}")

# # environment variables
VUE_APP_BACKEND_URL=os.getenv("BACKEND_URL")