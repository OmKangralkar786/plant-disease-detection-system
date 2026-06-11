import os

train_classes = os.listdir("dataset_split/train")

print("Total Classes:", len(train_classes))

for cls in train_classes:
    print(cls)