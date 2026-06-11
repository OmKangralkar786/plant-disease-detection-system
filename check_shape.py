from prepare_data import train_dataset

for images, labels in train_dataset.take(1):
    print("Image Shape:", images.shape)
    print("Labels Shape:", labels.shape)