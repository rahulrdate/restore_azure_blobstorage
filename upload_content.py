import os, uuid, sys, glob
from azure.storage.blob import BlockBlobService, PublicAccess

def run_sample():
    try:
        files = []
        for r, d, f in os.walk('/directory/path/of/content/to/upload'):
            for file in f:
                files.append(os.path.join(r, file))


        block_blob_service = BlockBlobService(account_name='storage_account_name', account_key='storage_account_key_ending_in==')
        for f in files:
            print(f)
            print f.replace('/directory/path/of/content/to/upload','')
            block_blob_service.create_blob_from_path('name_of_container_in_blobstorage', f.replace('/directory/path/of/content/to/upload/',''), f)
    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()
