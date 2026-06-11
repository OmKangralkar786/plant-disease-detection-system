import splitfolders

splitfolders.ratio(
    input="dataset/PlantVillage",
    output="dataset_split",
    seed=42,
    ratio=(0.70, 0.15, 0.15)
)

print("Dataset split completed successfully!")