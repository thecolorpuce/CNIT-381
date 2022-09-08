import os

with os.scandir("C:\Users\AspRiley\OneDrive - University of Wisconsin-Stout\Desktop\Fall2022\") as entries:
    for entry in entries:
        print(entry.name)