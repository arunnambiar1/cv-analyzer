\## Session 2 — Upload endpoint (/analyze)



What I built:

\- Added POST /analyze that accepts an uploaded file (multipart/form-data)

\- Returned filename, content\_type, and size\_bytes



What I learned (explain in your own words):

\- UploadFile: FastAPI gives metadata (filename/content\_type) and lets me read bytes with await file.read()

\- multipart/form-data: how browsers send files to an API

\- Why async: reading the uploaded file is I/O, so FastAPI supports async endpoints



How I tested:

\- Ran: uvicorn app.main:app --reload

\- Opened: http://127.0.0.1:8000/docs

\- Used “Try it out” to upload an image and saw JSON response

