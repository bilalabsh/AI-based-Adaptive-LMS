import json
import PyPDF2
import re

def extract_answers_from_pdf(pdf_path):
    # Initialize a PDF reader
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Use regex to find answer patterns, e.g., "1 D", "2 C", etc.
    answers = {}
    matches = re.findall(r'(\d+)\s+([A-D])', text)
    for match in matches:
        question_number = match[0]  # Use the raw number from the PDF
        answer = match[1]
        answers[question_number] = answer
        print(f"Extracted - Question: {question_number}, Answer: {answer}")
    return answers

def update_json_with_answers(json_path, answers):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        question_number = item.get("QuestionNumber")
        if question_number in answers:
            item["answer"] = answers[question_number]
            print(f"Updated - Question: {question_number}, Answer: {answers[question_number]}")
        else:
            print(f"No match found for Question: {question_number}")

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Updated JSON file saved at: {json_path}")

if __name__ == "__main__":
    pdf_path = "./5054_w20_ms_11.pdf"
    json_path = "./5054_w20_qp_11.json"

    answers = extract_answers_from_pdf(pdf_path)
    update_json_with_answers(json_path, answers)
