
# labset 12
'''Develop a program to display contents of 
a folder recursively (Directory) having sub-folders and files (name and type). 
'''

import os
def display_directory(path , level = 0):
    try:
        items = os.listdir(path)
    except PermissionError:
        print(" "*level + "PErmmission denied")

    return 
    for item in items:
        full_path = os.path.join(path , item)
        if os.path.isdir(full_path):
            print(" "*level +f"[Folder] {item}")
            display_directory(full_path , level+4)

        else:
            _,ext = os.path.splitext(full_path)
            ext = ext if ext else "No Extension"
            print(" "*level +f"[File]{item} Type: {ext}")

path = input("Enter the file path: ")
print("----- Directory Content--------")
display_directory(path)

