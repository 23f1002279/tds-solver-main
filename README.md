TDS Solver
Project Overview
The TDS Solver is an LLM-based application designed to automatically answer questions from the graded assignments of the "Tools in Data Science" course at IIT Madras' Online Degree in Data Science. This project aims to provide a reliable API endpoint that accepts assignment questions, optionally with attached files, and returns the correct answer ready to be entered into the assignment submission.

This solver leverages the power of Large Language Models to interpret complex natural language questions, process associated data (from files), and derive the precise answer required for the assignments.

Features
Intelligent Question Answering: Utilizes an LLM to understand and solve questions from TDS graded assignments.
Multipart/Form-data Support: Accepts questions along with file attachments (e.g., CSV, ZIP) as multipart/form-data.
Standardized JSON Response: Returns answers in a simple JSON format {"answer": "..."}, directly usable for assignment submissions.
Focus on Accuracy: Designed to produce exact, verifiable answers to graded assignment questions.
Publicly Deployable: Built for deployment to a public URL (e.g., Vercel), ensuring accessibility for evaluation.
API Endpoint
Your application will expose a single API endpoint to handle all assignment questions.

POST /api/
This endpoint accepts a question string and optional file attachments as multipart/form-data.

URL: https://your-app.vercel.app/api/ (Replace your-app.vercel.app with your actual deployed URL)

Method: POST

Content-Type: multipart/form-data

Request Body Fields:

question (string, required): The plain-text question from the graded assignment.
file (file, optional): An optional file attachment related to the question (e.g., abcd.zip, extract.csv). This field can be repeated for multiple files if necessary.
Example Request (using curl):

Bash

curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the \"answer\" column of the CSV file?" \
  -F "file=@abcd.zip"
Response:

HTTP 200 OK: If the answer is successfully determined.
Body: A JSON object with a single answer field.
<!-- end list -->

JSON

{
  "answer": "1234567890"
}
Error Responses: While the problem description implies a successful response format, a robust API should also handle errors (e.g., HTTP 400 Bad Request for malformed questions, HTTP 500 Internal Server Error for processing failures). The answer field in error cases might contain an error message or be empty.
