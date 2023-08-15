import os

# Read the "outliers.txt" file and retrieve image paths
with open("outliers.txt", "r") as f:
    outlier_paths = f.readlines()
outlier_paths = [path.strip() for path in outlier_paths]

# Delete the images
for path in outlier_paths:
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted: {path}")
    else:
        print(f"Image not found: {path}")
    
# Clear the content of "outliers.txt" file
with open("outliers.txt", "w") as f:
    f.write("")

print("Image deletion process completed.")
