import React from "react";
import { generateUploadButton } from "@uploadthing/react";

const UploadButton = generateUploadButton();

const UploadComponent = () => {
  const handleUpload = async (files) => {
    try {
      const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: files,
      });
      const data = await response.json();
      console.log("Uploaded Files:", data);
    } catch (error) {
      console.error("Upload Error:", error);
    }
  };

  return (
    <div>
      <UploadButton
        onUploadComplete={(res) => console.log("Upload successful:", res)}
        onUploadError={(err) => console.error("Upload failed:", err)}
      />
    </div>
  );
};

export default UploadComponent;
