import cv2
from PIL import Image
import os
from rich.traceback import install
install() # install rich traceback

print("imports complete")

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
print("loaded classifier")

def process_image(image_path, output_path, size=(128, 128)):
    # Read the image
    img = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # If no faces are detected return
    if len(faces) == 0:
        print(f"No faces found in {image_path}")
        return
    if len(faces) > 1:
        print(f"{len(faces)} found in {image_path}")
        print("using first found")
    # Get the first detected face
    x, y, w, h = faces[0]
    # Add padding around the face
    padding = int(w * 0.2) # adjust this to your needs
    x = max(0, x - padding)
    y = max(0, y - padding)
    w = min(img.shape[1] - x, w + 2 * padding)
    h = min(img.shape[0] - y, h + 2 * padding)
    # Crop the image to the face
    face = img[y:y+h, x:x+w]
    # Convert color from BGR to RBG
    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    # Convert to PIL Image and resize
    face_pil = Image.fromarray(face)
    face_pil = face_pil.resize(size, Image.LANCZOS)
    # Save the image
    face_pil.save(output_path)

# Specify your input directory and output directory here
input_dir = "/Users/djo/Downloads/submissions/"
output_dir = "/Users/djo/Dropbox/Personal/Studies/0-Grad School/MEM Program/IR INSY 3010 - Python SQL/roll-attendance/headshots"

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process all JPEG images in the input directory
print(f"processing files in {input_dir}")

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print(filename)
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        process_image(input_path, output_path, size=(256, 256))

