import zipfile
import os

def zipdir(path, zipf):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

zip_filename = 'C:/Users/username/Desktop/exp/vietnam.zip'
folder_to_zip = 'C:/Users/username/Desktop/vietnam'

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(folder_to_zip, zipf)
    zipf.setpassword(b'hej')