#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe

print("content-type:text/html\r\n\r\n")
import cgi
from common import connect_db, fetch_random_question, render_header, render_footer, render_question_and_options, update_tutor_score

form = cgi.FieldStorage()
tutor_id = form.getvalue("sno")
syllabus = form.getvalue("syllabus")

connection = connect_db()
cursor = connection.cursor()

# Fetch a random question for the page
question, tutor_id = fetch_random_question(cursor, syllabus, tutor_id)

# Handle form submission
if form.getvalue("submit"):
    selected_option = form.getvalue("option")
    correct_option = question[6]  # Assuming the correct answer is stored in column index 6
    if selected_option == correct_option:
        update_tutor_score(cursor, tutor_id)
        connection.commit()  # Commit the transaction

connection.close()

# Render the HTML content
print(render_header())
print(f"""
    <h1>Question Page 3</h1>
    {render_question_and_options(question)}
    <form method="post">
        <input type="hidden" name="sno" value="{tutor_id}">
        <input type="hidden" name="syllabus" value="{syllabus}">
        <input type="submit" name="submit" value="Next Question">
    </form>
""")
sub = form.getvalue("submit")

if sub is not None:
    print("""
           <script>
               location.href = "page4.py?sno=%s&syllabus=%s"
           </script>
           """ % (tutor_id, syllabus))
print(render_footer())
