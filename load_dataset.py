import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory



TRAIN_DIR = "dataset_split/train"
VAL_DIR = "dataset_split/val"
TEST_DIR = "dataset_split/test"


IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32

train_dataset = image_dataset_from_directory(
    TRAIN_DIR,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    shuffle=True
)


val_dataset = image_dataset_from_directory(
    VAL_DIR,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    shuffle=True
)


test_dataset = image_dataset_from_directory(
    TEST_DIR,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    shuffle=False
)



class_names = train_dataset.class_names

print("\nDisease Classes:\n")

for i, name in enumerate(class_names):
    print(i, ":", name)

print("\nTotal Classes:", len(class_names))