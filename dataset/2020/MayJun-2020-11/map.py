import pandas as pd
import json
import re
import os  # Import os for file path manipulation

# Step 1: Load the Excel file containing Unit, Topic, and Subtopic mappings
file_path = "Cleaned_O_LEVEL_PHYSICS_5054.xlsx"
excel_data = pd.read_excel(file_path)

# Step 2: Load the JSON file containing the original questions
json_file_path = "5054_s20_qp_11.json"
with open(json_file_path, "r") as f:
    json_data = json.load(f)


# Step 3: Function to perform exact word matching between question and subtopic
def match_subtopic(question_text, excel_data):
    for idx, row in excel_data.iterrows():
        subtopic_words = re.findall(
            r"\w+", row["Subtopic"].lower()
        )  # Extract individual words from subtopic
        question_words = re.findall(
            r"\w+", question_text.lower()
        )  # Extract individual words from question

        # Check if any word in the subtopic matches exactly with the question words
        if any(word in question_words for word in subtopic_words):
            return (
                row["Unit"],
                row["Topic"],
                row["Subtopic"],
            )  # Return matched Unit, Topic, Subtopic

    # Return empty values if no match is found
    return "", "", ""


# Step 4: Initialize an empty list to store structured questions
structured_questions = []

# Step 5: Iterate over the JSON questions and map them with Excel data based on exact subtopic matching
for question in json_data:
    question_text = question["Question"]
    unit, topic, subtopic = match_subtopic(
        question_text, excel_data
    )  # Find matching Unit, Topic, and Subtopic

    # Structure the question in the desired format
    structured_question = {
        "QuestionNumber": question["QuestionNumber"],
        "Question": question["Question"],
        "Options": question["Options"],
        "image": question.get("image", None),
        "answer": question.get("answer", None),
        "Unit": unit,
        "Topic": topic,
        "Sub_topic": subtopic,
    }

    structured_questions.append(structured_question)

# Step 6: Dynamically define the output path for the new structured JSON
base_name = os.path.basename(json_file_path)  # Extract the file name from the JSON file path
output_json_path = f"structured_{base_name}"  # Append 'structured_' to the file name

# Step 7: Save the newly structured data to a JSON file
with open(output_json_path, "w") as outfile:
    json.dump(structured_questions, outfile, indent=4)

# Output path to download the structured file
output_json_path
