const express = require("express");
const bodyParser = require("body-parser");
const { createUploadthing } = require("@uploadthing/node");

require("dotenv").config();
const app = express();
app.use(bodyParser.json());

const port = 5000;

const uploadHandler = createUploadthing({
  image: { maxFileSize: "5MB" },
}).onUploadComplete(async ({ file }) => {
  console.log("Uploaded file URL:", file.url);
});

app.post("/upload", async (req, res) => {
  try {
    const { file } = req.body; // Expect the file as base64 or Blob URL
    const result = await uploadHandler.handle(file);
    res.status(200).json({ success: true, result });
  } catch (err) {
    console.error("Upload error:", err);
    res.status(500).json({ success: false, error: err.message });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
