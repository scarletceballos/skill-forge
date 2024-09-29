from fastapi import FastAPI, UploadFile, File
from pdfparser import parse_pdf
import os

app = FastAPI()

os.makedirs('uploads', exist_ok=True)

@app.post("/api/parse-document")
async def parse_document(file: UploadFile = File(...)):
    # Save the uploaded file
	file_location = f"uploads/{file.filename}"
	with open(file_location, "wb") as f:
		f.write(await file.read())
	result = parse_pdf(file_location)
	#insert code to move 

    # Send file to Affinda for parsing
    with open(file_location, "rb") as f:
        response = requests.post(
            "https://api.affinda.com/v1/parser",
            files={"file": f},
            headers={"Authorization": f"Bearer {os.getenv('AFFINDA_API_KEY')}"}
        )

    # Delete the file after processing (optional)
    os.remove(file_location)


    return {
    "success": response.json().get("success"),
    "data": response.json().get("data"),
    "message": response.json().get("message")
}

