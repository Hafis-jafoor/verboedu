#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import cgi
from common import connect_db, fetch_random_question, render_header, render_footer, render_question_and_options

form = cgi.FieldStorage()
id1 = form.getvalue("sno")


connection = connect_db()
cursor = connection.cursor()

# Fetch a random question for the first page
question = fetch_random_question(cursor)

connection.close()

# Handle form submission
if form.getvalue("submit"):
    selected_option = int(form.getvalue("option"))
    correct_option = int(question[6])  # Assuming correct option is stored in column 6

    if selected_option == correct_option:
        user_score = 1
    else:
        user_score = 0

# Render the HTML content
print(render_header())
print(f"""
    <h1>Page 1</h1>
    {render_question_and_options(question)}
""")
print(render_footer())
