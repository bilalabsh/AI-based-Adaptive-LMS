import json
import PyPDF2

def extract_answers_from_pdf(pdf_path):
    # Extract answers from the PDF marking scheme
    print(f"Opening PDF file: {pdf_path}")
    answers = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total number of pages in PDF: {len(reader.pages)}")
        # Extract from all pages
        for page_number, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"Extracting text from page {page_number + 1}")
            # Extract answers (assuming they are listed as '1 A', '2 B', etc.)
            lines = text.splitlines()
            for line in lines:
                parts = line.split()
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isalpha():
                    print(f"Found answer: Question {parts[0]} -> {parts[1]}")
                    answers.append(parts[1].strip())
    print(f"Total answers extracted: {len(answers)}")
    return answers

def populate_json_with_answers(json_path, answers):
    # Load the JSON file
    print(f"Loading JSON file: {json_path}")
    with open(json_path, 'r') as file:
        data = json.load(file)
    
    print(f"Total number of questions in JSON: {len(data)}")
    
    # Ensure the number of answers matches the number of questions
    if len(answers) != len(data):
        raise ValueError("The number of answers does not match the number of questions in the JSON file.")
    
    # Populate the 'answer' key in the JSON data
    for i, answer in enumerate(answers):
        print(f"Populating question {i + 1} with answer {answer}")
        data[i]['answer'] = answer
    
    # Save the updated JSON file
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Successfully saved the updated JSON file: {json_path}")


def main():
    pdf_path = 'C:/Users/Bilal/Desktop/pastPapers/dataset/2023/MayJun-2023-11/5054_s23_ms_11.pdf'
    json_path = 'C:/Users/Bilal/Desktop/pastPapers/dataset/2023/MayJun-2023-11/5054_s23_qp_11.json'
    
    answers = extract_answers_from_pdf(pdf_path)
    populate_json_with_answers(json_path, answers)
    print(f"Successfully populated the JSON file with answers from {pdf_path}.")

if __name__ == "__main__":
    main()
