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
    "region": os.getenv("REGION")
}

oci.config.validate_config(config)

identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
print(user)
compartment_id = config["tenancy"]
print(compartment_id)