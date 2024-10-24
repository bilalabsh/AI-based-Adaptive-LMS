import json
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bilalabdul",
    database="fyp"
)

cursor = db.cursor()

# Load JSON file
with open('./5054_w23_qp_12.json', 'r') as file:
    questions_data = json.load(file)

# Insert data into the table
for question in questions_data:
    query = """
    INSERT INTO questions (question, paper, options, answer, image)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        question['Question'],
        question['QuestionNumber'],
        json.dumps(question['Options']),  # Convert options to JSON
        question['answer'],
        question['image']  # This will insert null if the image is null
    ))

db.commit()
cursor.close()
db.close()
