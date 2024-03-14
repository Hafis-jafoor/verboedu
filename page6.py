#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe

# Last question page (page10.py)
# Similar structure to other question pages, but without the form for the next question
# Display the final score instead

print("content-type:text/html\r\n\r\n")
import cgi
from common import connect_db, render_header, render_footer, fetch_tutor_score

form = cgi.FieldStorage()
tutor_id = form.getvalue("sno")
syllabus = form.getvalue("syllabus")

connection = connect_db()
cursor = connection.cursor()

# Fetch the final score
final_score = fetch_tutor_score(cursor, tutor_id)
print(final_score)

connection.close()

# Render the HTML content
print(render_header())
print(f"""
    <h1>final page</h1>
    <p>Final Score: {final_score}</p>
""")
print(render_footer())
