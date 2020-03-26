import dropbox
import pandas as pd

# Dropbox access token. Change the string below to your own token.
access_token = 'INSERT_YOUR_TOKEN_HERE'

# Instance of Dropbox class that grants access to the user's Dropbox files.
dbx = dropbox.Dropbox(access_token)

# Global list of all folders.
all_folders = []

# Global list of hierarchies associated with each folder.
all_hierarchies = []

# Global list of folder sizes.
all_sizes_cumul = []

def main():
    """Calculates the size of all subfolders in your Dropbox account and 
    generates a CSV file containing the output.
    
    This is done by calling the recursive check_folders function, generating
    a DataFrame with the results, and then writing the DataFrame to disk.
    """
    
    # Run recursive function.
    check_folders('', 1)
    
    # Create DataFrame with results.
    folder_db = pd.DataFrame({"folder":all_folders})
    folder_db["hierarchy"] = all_hierarchies
    folder_db["size_cumul"] = all_sizes_cumul
    
    # Calculate folder sizes in kilobytes, megabytes and gigabytes.
    for i,this_size in enumerate(["kb","mb","gb"]):
        folder_db["size_cumul_" + this_size] = (folder_db["size_cumul"]
                                                * 1.0 / (1024 ** (i+1)))
    # Export results to a CSV file
    folder_db.to_csv("folder_sizes.csv",index=False, encoding='utf8')


def check_folders(folder_path, hierarchy):
    """Recursive function that actually calculates folder sizes.
    
    Keyword arguments: 
      folder_path: string that defines the path to the current folder.
      hierarchy: integer that defines depth in the folder tree. Example:
           root (hierarchy = 1)
            ∟sub_a (hierarchy = 2)
            ∟sub_b (hierarchy = 2)
              ∟subsub_a (hierarchy = 3)
    
    Outputs: folder size 
    
    Note: This function also edits the three main global variables: 
          all_folders, all_hierarchies, all_sizes_cumul.
    """
    
    # List of subfolders in current folder.
    folder_temp_list = []
    
    # List of files in current folder.
    file_temp_list = []
    
    # Running tally of current folder's size.
    this_folder_size = 0.0
    
    # Scans through all files and subfolders, appending them to the two
    # lists created above.
    for entry in dbx.files_list_folder(folder_path).entries:
        if type(entry) == dropbox.files.FolderMetadata:
            folder_temp_list.append(entry)
        if type(entry) == dropbox.files.FileMetadata:
            file_temp_list.append(entry)
            
    # For each of the subfolders, recursively call the check_folders function.
    for this_subfolder in folder_temp_list:
        this_subfolder_name = this_subfolder.name
        this_subfolder_full_path = folder_path + "/" + this_subfolder_name
        this_subfolder_size = check_folders(this_subfolder_full_path,
                                            hierarchy+1)
        this_folder_size = this_folder_size + this_subfolder_size
    
    # For each of the files, add their size to the current folder's size tally.
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
