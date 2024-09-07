import os
# Creating a Dir
if(not os.path.exists("dir")):
        os.mkdir("dir")
for i in range(0,100):
# if we want dir's name change then
        os.rename(f"dir/day {i+1}",f"dir/Practice {i+1}")

# if we want to read
folders= os.listdir("dir")
print("folders")
for folder in folders:
        print(os.listdir(f"dir/{folder}"))