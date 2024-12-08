const express = require("express");
const { createUploadthing } = require("@uploadthing/node");

const app = express();
const port = 5000;

// Define your UploadThing handler
const uploadHandler = createUploadthing({
  image: { maxFileSize: "5MB" }, // Configure file type and size
}).onUploadComplete(async ({ file }) => {
  console.log("File URL:", file.url);
});

app.post("/upload", async (req, res) => {
  try {
    const result = await uploadHandler.handle(req);
    res.status(200).json({ success: true, result });
  } catch (error) {
    console.error("Upload failed:", error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
