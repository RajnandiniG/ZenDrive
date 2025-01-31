import fiftyone as fo
import fiftyone.utils.annotations as foua
import os

# Input folder containing images
input_folder = r"C:\Users\Rajnandini Sharma\Downloads\state-farm-distracted-driver-detection\imgs\train\c2"

# Output folder to save annotated images
output_folder = r"C:\Users\Rajnandini Sharma\Downloads\output\c02-output"
os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

# Load all images from the input folder
dataset = fo.Dataset("distracted-drivers-v2")
dataset.add_dir(
    dataset_dir=input_folder,
    dataset_type=fo.types.ImageDirectory,  # Load images without labels
)

# Process each image in the dataset
for sample in dataset:
    # Define annotations for the current image
    sample["gt_label"] = fo.Classification(label="c0")  # Ground truth: normal driving
    sample["pred_label"] = fo.Classification(label="c1", confidence=0.85)  # Predicted: texting - right
    sample["gt_objects"] = fo.Detections(
        detections=[
            fo.Detection(
                label="driver",
                bounding_box=[0.1, 0.2, 0.3, 0.4],  # Bounding box for the driver
            ),
            fo.Detection(
                label="steering_wheel",
                bounding_box=[0.4, 0.5, 0.2, 0.3],  # Bounding box for the steering wheel
            ),
        ]
    )
    sample["pred_objects"] = fo.Detections(
        detections=[
            fo.Detection(
                label="driver",
                bounding_box=[0.12, 0.22, 0.28, 0.38],  # Predicted bounding box for the driver
                confidence=0.90,
            ),
            fo.Detection(
                label="talking_on_the_phone_right",  # Predicted: mobile phone (texting - right)
                bounding_box=[0.6, 0.7, 0.1, 0.1],  # Predicted bounding box for the phone
                confidence=0.95,
            ),
        ]
    )

    # Save the annotated image
    outpath = os.path.join(output_folder, os.path.basename(sample.filepath))
    foua.draw_labeled_image(sample, outpath)

    print(f"Annotated image saved to: {outpath}")

print("All images processed and annotated.")