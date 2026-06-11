import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.preprocessing import image_dataset_from_directory

from disease_info import DISEASE_INFO

# Load class names from training dataset
dataset = image_dataset_from_directory(
    "dataset_split/train",
    image_size=(224, 224),
    batch_size=32,
    shuffle=False
)

CLASS_NAMES = dataset.class_names

# Load trained model
model = load_model("plant_disease_model.keras")

# Test image path
IMAGE_PATH = "test_images/tomato_leaf.jpg"

# Load image
img = load_img(
    IMAGE_PATH,
    target_size=(224, 224)
)

# Convert image to array
img_array = img_to_array(img)

# Normalize image
img_array = img_array / 255.0

# Add batch dimension
img_array = np.expand_dims(
    img_array,
    axis=0
)

# Predict
prediction = model.predict(img_array)

# Get predicted class index
predicted_class_index = np.argmax(prediction)

print("Total Classes:", len(CLASS_NAMES))
print("Predicted Index:", predicted_class_index)

# Get disease name
disease_name = CLASS_NAMES[predicted_class_index]

# Get confidence
confidence = np.max(prediction) * 100

# Extract plant and disease names
if "___" in disease_name:
    plant, disease = disease_name.split("___")

elif "_" in disease_name:
    parts = disease_name.split("_", 1)
    plant = parts[0]
    disease = parts[1]

else:
    plant = "Unknown"
    disease = disease_name

# Display prediction
print("\nPrediction Result")
print("-------------------")
print("Plant:", plant)
print("Disease:", disease.replace("_", " "))
print("Confidence:", round(confidence, 2), "%")

# Display disease information if available
if disease_name in DISEASE_INFO:

    info = DISEASE_INFO[disease_name]

    print("\nCause:")
    print(info["cause"])

    print("\nTreatment:")
    print(info["treatment"])

else:

    print("\nCause:")
    print("Information not available")

    print("\nTreatment:")
    print("Information not available")