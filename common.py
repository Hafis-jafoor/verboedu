import pymysql


def connect_db():
    return pymysql.connect(host="localhost", user="root", password="", database="verbo")


def fetch_random_question(cursor, syllabus, tutor_id, excluded_question_ids=None):
    if excluded_question_ids:
        query = f"SELECT * FROM {syllabus} WHERE slno NOT IN ({', '.join(map(str, excluded_question_ids))}) ORDER BY RAND() LIMIT 1"
    else:
        query = f"SELECT * FROM {syllabus} ORDER BY RAND() LIMIT 1"

    cursor.execute(query)
    return cursor.fetchone(), tutor_id


def fetch_tutor_score(cursor, tutor_id):
    query = f"SELECT score FROM tutors_registeration WHERE slno = {tutor_id}"
    cursor.execute(query)
    return cursor.fetchone()[0]


def update_tutor_score(cursor, tutor_id):
    # Fetch the current score
    current_score_query = f"SELECT score FROM tutors_registeration WHERE slno = {tutor_id}"
    cursor.execute(current_score_query)
    current_score = cursor.fetchone()[0]

    # Calculate the new score
    new_score = current_score + 1

    # Update the score in the database
    update_query = f"UPDATE tutors_registeration SET score = {new_score} WHERE slno = {tutor_id}"
    cursor.execute(update_query)


def render_header():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Quiz</title>
    </head>
    <body>
    """


def render_footer():
    return """
    </body>
    </html>
    """


def render_question_and_options(question):
    return f"""
        <div>
            <h2>Question: {question[1]}</h2>
            <form method="post" action="#">
                <input type="hidden" name="question_id" value="{question[0]}">
                <input type="radio" name="option" value="{question[2]}" id="opt1" required><label for="opt1">
                {question[2]}</label><br>
                <input type="radio" name="option" value="{question[3]}" id="opt2" required><label for="opt2">
                {question[3]}</label><br>
                <input type="radio" name="option" value="{question[4]}" id="opt3" required><label for="opt3">
                {question[4]}</label><br>
                <input type="radio" name="option" value="{question[5]}" id="opt4" required><label for="opt4">
                {question[5]}</label><br>
                <input type="submit" name="submit" value="Submit">
            </form>
        </div>
    """

# def fetch_tutor_score1(cursor, tutor_id):
#     query = f"SELECT score FROM tutors_registeration WHERE slno = {tutor_id}"
#     cursor.execute(query)
#     return cursor.fetchone()[0]  # Assuming the score is in the first column of the result


# import pymysql
#
#
# def connect_db():
#     return pymysql.connect(host="localhost", user="root", password="", database="verbo")
#
#
# def fetch_random_question(cursor, syllabus, tutor_id, excluded_question_ids=None):
#     if excluded_question_ids:
#         query = f"SELECT * FROM {syllabus} WHERE slno NOT IN ({', '.join(map(str, excluded_question_ids))}) ORDER BY RAND() LIMIT 1"
#     else:
#         query = f"SELECT * FROM {syllabus} ORDER BY RAND() LIMIT 1"
#
#     cursor.execute(query)
#     return cursor.fetchone(), tutor_id
#
#
# def update_tutor_score(cursor, tutor_id):
#     query = f"UPDATE tutors_registration SET score = score + 1 WHERE slno = {tutor_id}"
#     cursor.execute(query)
#
#
#
# def render_header():
#     return """
#     <!DOCTYPE html>
# <html lang="en">
#
# <head>
#     <meta charset="utf-8">
#     <title>Tutor Evaluation Form</title>
#     <meta content="width=device-width, initial-scale=1.0" name="viewport">
#     <meta content="" name="keywords">
#     <meta content="" name="description">
#
#     <!-- Favicon -->
#     <link href="img/favicon.ico" rel="icon">
#
#     <!-- Google Web Fonts -->
#     <link rel="preconnect" href="https://fonts.googleapis.com">
#     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#     <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">
#
#     <!-- Icon Font Stylesheet -->
#     <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">
#
#     <!-- Libraries Stylesheet -->
#     <link href="lib/animate/animate.min.css" rel="stylesheet">
#
#     <!-- Customized Bootstrap Stylesheet -->
#     <link href="css/bootstrap.min.css" rel="stylesheet">
#
#     <!-- Template Stylesheet -->
#     <link href="css/style.css" rel="stylesheet">
# </head>
#
# <body>
#     """
#
#
# def render_footer():
#     return """
#     <!-- JavaScript Libraries -->
#     <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
#     <script src="lib/wow/wow.min.js"></script>
#     <script src="lib/easing/easing.min.js"></script>
#
#     <!-- Template Javascript -->
#     <script src="js/main.js"></script>
# </body>
#
# </html>
#
#     """
#
#
# def render_question_and_options(question):
#     return f"""
#         <div>
#             <h2>Question: {question[1]}</h2>
#             <form method="post" action="#">
#                 <input type="hidden" name="question_id" value="{question[0]}">
#                 <input type="radio" name="option" value="1" id="opt1"><label for="opt1">{question[2]}</label><br>
#                 <input type="radio" name="option" value="2" id="opt2"><label for="opt2">{question[3]}</label><br>
#                 <input type="radio" name="option" value="3" id="opt3"><label for="opt3">{question[4]}</label><br>
#                 <input type="radio" name="option" value="4" id="opt4"><label for="opt4">{question[5]}</label><br>
#                 <input type="submit" name="submit" value="Submit">
#             </form>
#         </div>
#     """
