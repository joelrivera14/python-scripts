from pathlib import Path
import shutil

source = Path.home() / "Downloads"
destination = Path.home() / "Desktop/deskdownloads"
count = 0

destination.mkdir(exist_ok=True)
for item in source.iterdir():
    if item.is_file:
        #takes two argumentsz: the source path and the dest path
        shutil.move(item, destination/item.name)
        count +=1
print(count)