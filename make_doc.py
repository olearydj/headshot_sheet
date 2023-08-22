import os
import docx
from docx.shared import Inches
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

# Specify your input directory and output docx file here
output_dir = "/Users/djo/Dropbox/Personal/Studies/0-Grad School/MEM Program/IR INSY 3010 - Python SQL/roll-attendance/headshots"
input_dir = output_dir
output_docx = os.path.join(output_dir, "headshots.docx")

# Create a new Word document
doc = docx.Document()

# Get a list of all JPEG images in the input directory
images = [f for f in os.listdir(input_dir) if f.endswith(".jpg") or f.endswith(".jpeg")]

# Sort the images by name
images.sort()

# Create a 6x6 table for each group of 36 students
for i in range(0, len(images), 36):
    table = doc.add_table(rows=6, cols=6)

    # Add an image and a name to each cell
    for j in range(36):
        if i + j < len(images):
            # Get the image filename and path
            image_filename = images[i + j]
            image_path = os.path.join(input_dir, image_filename)

            # Extract the name from the filename
            name_parts = image_filename.split("_")
            first_name = ''.join([i for i in name_parts[1] if not i.isdigit()])
            first_name = first_name[:1].upper() + first_name[1:].lower()
            last_name = name_parts[0].title()
            name = f"{first_name} {last_name}"

            # Add the image to the cell
            cell = table.cell(j // 6, j % 6)
            paragraph = cell.paragraphs[0]
            paragraph.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.add_picture(image_path, width=docx.shared.Inches(1))

            # Add the name to the cell
            paragraph = cell.add_paragraph()
            paragraph.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.text = name

    # Add a page break after each table except the last one
    if i + 36 < len(images):
        doc.add_page_break()

# Save the document
doc.save(output_docx)

