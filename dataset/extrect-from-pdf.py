import fitz  # PyMuPDF
import os  # For directory operations

# Define replacement mappings
REPLACEMENTS = {
    "\u2192": "→",
    "\u00d7": "x",
    "\u00b0": "°",
    "\u03a9": "Ω",
    "\u00f7": "÷",
    "\u03c1": "ρ",
    "\u2013": "-",
    "\u00b3": "^3"
}

def replace_special_characters(text):
    """Replace special characters in the text based on the REPLACEMENTS dictionary."""
    for original, replacement in REPLACEMENTS.items():
        text = text.replace(original, replacement)
    return text


def extract_images_from_pdf(pdf_path, output_folder):
    # Create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # print(f"Opened PDF: {pdf_path}")

    # Loop through each page in the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        # Get list of images on the page
        image_list = page.get_images(full=True)
        # print(f"Found {len(image_list)} images on page {page_number + 1}")
        
        # Extract text from the page
        text = page.get_text("text")
        print(f"Extracted text :{text}")

        # Replace special characters in the text
        text = replace_special_characters(text)
        print(f"Extracted text (after replacements): {text}")

        # Split the text into lines and find the source text for each image
        lines = text.split("\n")

        # Loop through each image on the page
        for image_index, img in enumerate(image_list):
            xref = img[0]
            # print(f"Extracting image {image_index + 1} on page {page_number + 1} with xref {xref}")

            # Extract the image
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            # print(f"Image {image_index + 1} on page {page_number + 1} has extension: {image_ext}")
            
            # Find the source text for the image (assumption: source text is directly above the image)
            # For simplicity, this example assumes the source text is on the line above the image
            # You might need to adjust this part depending on the actual layout
            source_text = "UnknownSource"  # Default source text
            if image_index < len(lines):
                source_text = lines[image_index].strip()
            
            # Construct image filename using source text
            source_text_sanitized = source_text.replace("/", "_").replace(" ", "_")
            image_filename = f"{output_folder}/image_page{page_number + 1}_{source_text_sanitized}.{image_ext}"
            # print(f"Saving image to: {image_filename}")
            
            # Save the image to the output folder
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
            print(f"Successfully saved image: {image_filename}")

# Example usage
pdf_path = 'C:/Users/Ishma/Desktop/CAIE/5054_w21_qp_11.pdf'
output_folder = 'C:/Users/Ishma/Desktop/CAIE/images2'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created output folder: {output_folder}")


extract_images_from_pdf(pdf_path, output_folder)