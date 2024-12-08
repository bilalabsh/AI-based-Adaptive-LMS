const { collection, addDoc } = require("firebase/firestore");

const fs = require("fs");
// Node.js file system module to read files
const db = require("./firebase"); // Import your Firestore configuration


// Path to your JSON files
const jsonFiles = ["../MayJun-2019-11/structured_5054_s19_qp_11.json"];

// Function to upload data to Firestore
const uploadData = async () => {
  for (const filePath of jsonFiles) {
    try {
      // Read JSON file
      const rawData = fs.readFileSync(filePath);
      const data = JSON.parse(rawData);

      // Loop through each question in the file and add it to Firestore
      for (const question of data) {
        try {
          await addDoc(collection(db, "questions"), question);
          console.log(
            `Successfully added question: ${question.QuestionNumber}`
          );
        } catch (error) {
          console.error(
            `Error adding question ${question.QuestionNumber}:`,
            error
          );
        }
      }
    } catch (error) {
      console.error(`Error reading file ${filePath}:`, error);
    }
  }
};

uploadData();
