import dropbox
import pandas as pd

access_token = 'INSERT_YOUR_TOKEN_HERE'

dbx = dropbox.Dropbox(access_token)

all_folders = []
all_hierarchies = []
all_sizes_cumul = []

def main():
    check_folders('', 1)
    folder_db = pd.DataFrame({"folder":all_folders})
    folder_db["hierarchy"] = all_hierarchies
    folder_db["size_cumul"] = all_sizes_cumul
    for i,this_size in enumerate(["kb","mb","gb"]):
        folder_db["size_cumul_" + this_size] = folder_db["size_cumul"] * 1.0 / (1024 ** (i+1))
    folder_db.to_csv("folder_sizes.csv",index=False, encoding='utf8')

def check_folders(folder_path, hierarchy):
    folder_temp_list = []
    file_temp_list = []
    this_folder_size = 0.0
    for entry in dbx.files_list_folder(folder_path).entries:
        if type(entry) == dropbox.files.FolderMetadata:
            folder_temp_list.append(entry)
        if type(entry) == dropbox.files.FileMetadata:
            file_temp_list.append(entry)
    for this_subfolder in folder_temp_list:
        this_subfolder_name = this_subfolder.name
        this_subfolder_full_path = folder_path + "/" + this_subfolder_name
        this_subfolder_size = check_folders(this_subfolder_full_path,hierarchy+1)
        this_folder_size = this_folder_size + this_subfolder_size
    for this_file in file_temp_list:
            this_folder_size = this_folder_size + this_file.size
    if folder_path == '':
        all_folders.append('/')
    else:
        all_folders.append(folder_path)
    all_sizes_cumul.append(this_folder_size)
    all_hierarchies.append(hierarchy)
    if hierarchy != 1:
        return this_folder_size

if __name__ == '__main__':
    main()
