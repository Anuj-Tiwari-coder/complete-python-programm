import os
folders= os.listdir("dir")
print("folders")
for folder in folders:
        print(os.listdir(f"dir/{folder}"))