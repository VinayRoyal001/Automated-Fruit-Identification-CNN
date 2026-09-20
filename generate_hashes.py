import os
import imagehash
from PIL import Image
import pickle

# Path to your fruit images dataset
DATASET_DIR = r'C:\Users\amyak\Desktop\Fruit_Identification_Using_Convolutional_Neural_Network\media\Fruit-Images-Dataset-master'

# Generate hashes for all images in the dataset
known_hashes = []

# Function to calculate hash for an image
def generate_hashes_for_images(dataset_dir):
    print(f"Starting hash generation for dataset at: {dataset_dir}")
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                file_path = os.path.join(root, file)
                try:
                    print(f"Processing image: {file_path}")
                    img = Image.open(file_path)
                    img_hash = imagehash.average_hash(img)
                    known_hashes.append(img_hash)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    # Save the hashes to a .pkl file
    print("Saving hashes to 'known_hashes.pkl'...")
    with open('known_hashes.pkl', 'wb') as f:
        pickle.dump(known_hashes, f)
    print("Image hashes saved to 'known_hashes.pkl'.")

# Run the hash generation
generate_hashes_for_images(DATASET_DIR)
