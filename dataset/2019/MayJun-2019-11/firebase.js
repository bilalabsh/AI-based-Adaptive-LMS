const { initializeApp } = require("firebase/app");
const { getFirestore } = require("firebase/firestore");

const firebaseConfig = {
  apiKey: "AIzaSyC4JRpKH0GNGF80irTXUnM6G7TND0HF43Y",
  authDomain: "iparhai-app.firebaseapp.com",
  projectId: "iparhai-app",
  storageBucket: "iparhai-app.appspot.com",
  messagingSenderId: "510895139",
  appId: "1:510895139:web:aee7f3b5ab91e0e07c7d96",
  measurementId: "G-JJWC9YM75N",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app); // Get Firestore database instance

module.exports = { app, db, firebaseConfig }; // Export the db instance
