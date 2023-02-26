import oci

config = oci.config.from_file("~/.oci/config", "DEFAULT")

identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
print(user)

object_storage_client = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage_client.get_namespace().data

print(object_storage_client.list_buckets(namespace_name=namespace, compartment_id=config['tenancy']).data)
# print(dir(object_storage_client))