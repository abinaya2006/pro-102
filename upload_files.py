import dropbox,os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    
    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for main_folder,folder,files in os.walk(file_from):
            
            for file_name in files:
                local_path=os.path.join(main_folder,file_name)

                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
    

def main():
    access_token="ix4GoxYnpF0AAAAAAAAAAZl1dU4Ya2Rw754MZ3-zOJYR6xGuZDC0kgNDLcWd--j3"
    transferData=TransferData(access_token)

    file_from=input("Enter the file path to upload: ")
    file_to=input("Enter the full path to upload to dropbox: ")

    transferData.upload_files(file_from,file_to)

    print("The file has been moved.")

main()



    
