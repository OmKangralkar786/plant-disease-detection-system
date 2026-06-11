from tensorflow.keras.preprocessing import image_dataset_from_directory

dataset = image_dataset_from_directory(
    "dataset_split/train",
    image_size=(224,224),
    batch_size=32
)

print("\nClass Names:\n")

for i, cls in enumerate(dataset.class_names):
    print(i, cls)

print("\nTotal Classes:", len(dataset.class_names))