from tensorflow.keras.preprocessing import image_dataset_from_directory

train_dataset = image_dataset_from_directory(
    "dataset_split/train",
    image_size=(224,224),
    batch_size=32
)

print(train_dataset.class_names)