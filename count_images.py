import os

for dataset_type in ["train", "val", "test"]:
    path = f"dataset_split/{dataset_type}"

    total = 0

    for folder in os.listdir(path):
        total += len(os.listdir(os.path.join(path, folder)))

    print(dataset_type, ":", total, "images")