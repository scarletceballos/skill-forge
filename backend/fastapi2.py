from fastapi import FastAPI, UploadFile, File
from pdfparser import parse_pdf
import database
import os

db1 = new DBConnection
app = FastAPI()

os.makedirs('uploads', exist_ok=True)


@app.post("/api/parse-document")
#would it be post or get? 
async def get_skills(file: UploadFile = File(...), job_desciption):
       #job description is taken as a second argument, and it just a string imported from frontend that the user inputs
    # Save the uploaded file
	file_location = f"uploads/{file.filename}"
	with open(file_location, "wb") as f:
		f.write(await file.read())
              
    try:
		#send the file to affinda for parsing (pdfparser)
        result = parse_pdf(file_location)

    except _______________________:
        return "Sorry, we could not parse your file"

    #save the results (the response json ) into database
    db1.insert_a_user(result)
    db1.close()

    #make a call to the difference.py method
    get_difference_in_skills(result, job_description)



