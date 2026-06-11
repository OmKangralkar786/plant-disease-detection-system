import os

dataset_path = "dataset/PlantVillage"

classes = os.listdir(dataset_path)

print("Total Classes:", len(classes))

for cls in classes:
    print(cls)