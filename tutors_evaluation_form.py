#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import cgi
import pymysql

a = cgi.FieldStorage()
id1 = a.getvalue("sno")
# print(id1)
conn = pymysql.connect(host="localhost", user="root", password="", database="verbo")
cur = conn.cursor()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Tutor Evaluation Form</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="" name="keywords">
    <meta content="" name="description">

    <!-- Favicon -->
    <link href="img/favicon.ico" rel="icon">

    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">

    <!-- Icon Font Stylesheet -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">

    <!-- Libraries Stylesheet -->
    <link href="lib/animate/animate.min.css" rel="stylesheet">

    <!-- Customized Bootstrap Stylesheet -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Template Stylesheet -->
    <link href="css/style.css" rel="stylesheet">
</head>

<body>
    <!-- Header Start -->
    <div class="container-fluid bg-primary py-5 mb-5 page-header" style="background: linear-gradient(white, #00A79D);">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-10 text-center">
                    <h1 class="display-3 text-white animated slideInDown">Tutor Evaluation Form</h1>
                </div>
            </div>
        </div>
    </div>
    <!-- Header End -->

    <!-- Mentorship Importance Section Start -->
<div class="container-fluid bg-light py-5">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <h2 class="display-4 mb-4">Become a Mentor</h2>
                <p class="lead">Mentoring is a rewarding experience where you can make a positive impact on someone's life. As a mentor, you can share your knowledge and expertise, provide guidance and support, and help others achieve their goals.</p>
                <p class="lead">By becoming a mentor, you not only contribute to the personal and professional growth of others but also enhance your own skills, build meaningful relationships, and give back to the community.</p>
            </div>
            <div class="col-lg-6 text-center">
                <img src="img/parent-engagement.webp" class="img-fluid" alt="Mentorship Image">
            </div>
        </div>
    </div>
</div>
<!-- Mentorship Importance Section End -->

    <!-- Tutor Selection Form Start -->
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-12">
                <form action="" method="post">
                    <div class="mb-3 row">
                        <div class="mb-3 col-lg-4">
                            <label for="class" class="form-label">Select Class:</label>
                            <select class="form-select" id="class" name="class" required>
                                <option value="" selected disabled>Select Class</option>
                                <option value="1">Class 1</option>
                                <option value="2">Class 2</option>
                                <option value="3">Class 3</option>
                                <!-- Add more options as needed -->
                            </select>
                        </div>
                        <div class="mb-3 col-lg-4">
                            <label for="subject" class="form-label">Select Subject:</label>
                            <select class="form-select" id="subject" name="subject" required>
                                <option value="" selected disabled>Select Subject</option>
                                <option value="Math">Math</option>
                                <option value="Science">Science</option>
                                <option value="English">English</option>
                                <!-- Add more options as needed -->
                            </select>
                        </div>
                        <div class="mb-3 col-lg-4">
                            <label for="syllabus" class="form-label">Select Syllabus:</label>
                            <select class="form-select" id="syllabus" name="syllabus" required>
                                <option value="" selected disabled>Select Syllabus</option>
                                <option value="demo_question">CBSE</option>
                                <option value="ICSE">ICSE</option>
                                <option value="State Board">State Board</option>
                                <!-- Add more options as needed -->
                            </select>
                        </div>
                    </div>
                    <div class="mb-3 d-grid gap-2">
                        <input type="submit" class="btn btn-primary btn-lg" name="sub" id="otpSubmitButton" 
                        value="Submit">
                    </div>
                </form>
            </div>
        </div>
    </div>
    <!-- Tutor Selection Form End -->

    <!-- JavaScript Libraries -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="lib/wow/wow.min.js"></script>
    <script src="lib/easing/easing.min.js"></script>

    <!-- Template Javascript -->
    <script src="js/main.js"></script>
</body>

</html>

""")

classes = a.getvalue("class")
subject = a.getvalue("subject")
syllabus = a.getvalue("syllabus")
sub = a.getvalue("sub")

if sub is not None:
        print("""
               <script>
                   alert("exam starts - all the very best");
                   location.href = "demo_1.py?sno=%s&class=%s&subject=%s&syllabus=%s"
               </script>
               """ % (id1, classes, subject, syllabus))

