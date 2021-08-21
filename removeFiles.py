import os,shutil,time

def removeFiles():
    path=input("Enter the path of the folder: ")
    days=time.time()-(30*24*60*60)

    if os.path.exists(path):

        for main_folder, folders, files in os.walk(path):
            if days >= folders_age(main_folder):
                remove_folder(main_folder)
                break
            
            
            
            else:
                for folder in folders:
                    folder_and_main_folder=os.path.join(main_folder,folder)

                    if days>=folders_age(folder_and_main_folder):
                        remove_folder(folder_and_main_folder)

            
                for file in files:
                    path_file=os.path.join(main_folder,file)

                    if days>=folders_age(path_file):
                        remove_files(path_file)
    
    else :
        print("{path} is not found")


def remove_folder(path):
    shutil.rmtree(path)
    print("{path} is removed successfully")

def remove_files(path):
    os.remove(path)
    print("{path} is removed successfully")


def folders_age(path):
     ctime=os.stat(path).st_ctime
     return ctime

removeFiles()