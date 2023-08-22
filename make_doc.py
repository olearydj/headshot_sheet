import os
import math
import docx
from docx.shared import Inches
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from rich.traceback import install

install()  # install rich traceback

# Specify your input directory and output docx file here
output_dir = "/Users/djo/Dropbox/Personal/Studies/0-Grad School/MEM Program/IR INSY 3010 - Python SQL/roll-attendance/headshots"
input_dir = output_dir
output_docx = os.path.join(output_dir, "headshots.docx")
placeholder_image = "./placeholder.jpg"
student_list_file = "./all_students.txt"

# Load the student list
with open(student_list_file, "r") as f:
    all_students = [line.strip() for line in f]

# Create a new Word document
doc = docx.Document()

# Create a dictionary mapping names to image paths
image_dict = {}
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        name_parts = filename.split("_")
        first_name = "".join([i for i in name_parts[1] if not i.isdigit()]).title()
        last_name = name_parts[0].title()
        name = f"{first_name} {last_name}"
        image_dict[name] = os.path.join(input_dir, filename)

# Create a single table of students; allow word to flow the rows
num_students = len(all_students)
num_cols = 5
num_rows = math.ceil(num_students / num_cols)
print(f"students: {num_students}, cols: {num_cols}, rows: {num_rows}")

table = doc.add_table(rows=num_rows, cols=num_cols)

for i in range(0, num_students):
    # Add an image and a name to each cell
    if i < num_students:
        # Get the student's name
        name = all_students[i]

        # Get the image path or placeholder image if none exists
        image_path = image_dict.get(name, placeholder_image)

        # Add the image to the cell
        cell = table.cell(i // num_cols, i % num_cols)
        paragraph = cell.paragraphs[0]
        paragraph.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.add_run()
        try:
            run.add_picture(image_path, width=docx.shared.Inches(1))
        except Exception as e:
            print(f"Error adding image: {image_path}")
            print(e)

        # Add the name to the cell
        paragraph = cell.add_paragraph()
        paragraph.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.add_run()
        run.text = name

# Save the document
doc.save(output_docx)
