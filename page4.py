#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import cgi
from common import connect_db, fetch_random_question, render_header, render_footer, render_question_and_options, \
    update_tutor_score, fetch_tutor_score

form = cgi.FieldStorage()
tutor_id = form.getvalue("sno")
syllabus = form.getvalue("syllabus")

connection = connect_db()
cursor = connection.cursor()

# Fetch a random question for the page
question, tutor_id = fetch_random_question(cursor, syllabus, tutor_id)

# Fetch the tutor's score
score1 = fetch_tutor_score(cursor, tutor_id)
if score1 is not None:
    score1 = int(score1)
print(score1)

# Render the HTML content
print(render_header())
print(f"""
    <h1>Question Page 1</h1>
    {render_question_and_options(question)}
""")

# Handle form submission
if "submit" in form:
    selected_option = form.getvalue("option")
    print('answer', selected_option)
    if selected_option is not None:
        correct_option = str(question[6])  # Assuming the correct answer is stored in column index 6
        if selected_option == correct_option:
            update_tutor_score(connection, cursor)
            connection.commit()  # Commit the transaction
        print("""
           <script>
               location.href = "page5.py?sno=%s&syllabus=%s"
           </script>
           """ % (tutor_id, syllabus))
    else:
        print("Please select an option before submitting.")
else:
    print("Submit button not clicked.")

print(render_footer())
