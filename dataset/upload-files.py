import os
import firebase_admin
from firebase_admin import credentials, storage, firestore
from datetime import datetime


# Initialize Firebase Admin SDK
def initialize_firebase():
    cred = credentials.Certificate(
        "./iparhai-app-firebase-adminsdk-u8jt1-df5723e03f.json"
    )  # Replace with your key file
    firebase_admin.initialize_app(
        cred,
        {
            "storageBucket": "iparhai-app.firebasestorage.app"  # Replace with your Firebase project ID
        },
    )


# Upload image to Firebase Storage and save metadata to Firestore
def upload_paper_images(local_file_path, year, session, variant):
    bucket = storage.bucket()
    file_name = os.path.basename(local_file_path)
    firebase_path = f"papers/{year}/{session}/{variant}/{file_name}"
    blob = bucket.blob(firebase_path)
    blob.upload_from_filename(local_file_path)
    blob.make_public()
    public_url = blob.public_url

    # Add metadata to Firestore
    db = firestore.client()
    doc_ref = (
        db.collection("papers")
        .document(str(year))
        .collection(session)
        .document(str(variant))
    )
    # Update Firestore with question metadata
    doc_ref.update(
        {"questions": firestore.ArrayUnion([{"name": file_name, "url": public_url}])}
    )
    print(f"Uploaded {file_name} to {firebase_path}. Public URL: {public_url}")


def create_document_structure(year, session, variant):
    db = firestore.client()
    doc_ref = (
        db.collection("papers")
        .document(str(year))
        .collection(session)
        .document(str(variant))
    )
    doc_ref.set({"questions": []})  # Initialize an empty question list


def main():
    initialize_firebase()

    # Directory containing images
    base_directory = "./2019/MayJun-2019-11/images"  # Replace with your root directory

    # Example structure: /path/to/papers/2019/May-June/11/
    for year in os.listdir(base_directory):
        year_path = os.path.join(base_directory, year)
        if os.path.isdir(year_path):
            for session in os.listdir(year_path):
                session_path = os.path.join(year_path, session)
                if os.path.isdir(session_path):
                    for variant in os.listdir(session_path):
                        variant_path = os.path.join(session_path, variant)
                        if os.path.isdir(variant_path):
                            create_document_structure(
                                year, session, variant
                            )  # Initialize Firestore structure
                            for file_name in os.listdir(variant_path):
                                if file_name.lower().endswith(
                                    (".png", ".jpg", ".jpeg")
                                ):
                                    local_file_path = os.path.join(
                                        variant_path, file_name
                                    )
                                    upload_paper_images(
                                        local_file_path, year, session, variant
                                    )


if __name__ == "__main__":
    main()
