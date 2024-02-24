#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import cgi
import pymysql

a = cgi.FieldStorage()
id1 = a.getvalue("sno")
# print(id1)
conn = pymysql.connect(host="localhost", user="root", password="", database="verbo")
cur = conn.cursor()
cur.execute("""select * from tutors_registeration where email='hafis3052000@gmail.com'""")
f = cur.fetchone()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Tutor Dashboard</title>
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

    <!-- Highlight Checkbox Styles -->
    <style>
        /* Highlight the checkbox with a background color */
        .highlight {
            background-color: #ffcccc; /* Light red background color */
        }
    </style>

</head>

<body>
    <!-- Header Start -->
    <div class="container-fluid bg-primary py-5 mb-5 page-header" style="background: linear-gradient(white, #00A79D);">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-10 text-center">
                    <h1 class="display-3 text-white animated slideInDown">Tutor Dashboard</h1>
                </div>
            </div>
        </div>
    </div>
    <!-- Header End -->

    <!-- Tutor Info Start -->
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Tutor Information</h5>
                        <p class="card-text"><strong>Name:</strong>%s</p>
                        <p class="card-text"><strong>Phone Number:</strong>%s </p>
                        <p class="card-text"><strong>Email:</strong>%s</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Tutor Info End -->
""" % (f[1], f[6], f[2]))

print("""
    <!-- Instructions Start -->
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <h2 class="text-center mb-4">Instructions</h2>
            <div id="instructionPart1" class="instruction-part">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Part 1</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi.</p>
                    </div>
                    <div class="card-footer text-end">
                        <button onclick="showNextPart(1)" class="btn btn-primary">Next</button>
                    </div>
                </div>
            </div>
            <div id="instructionPart2" class="instruction-part" style="display: none;">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Part 2</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi.</p>
                    </div>
                    <div class="card-footer text-end">
                        <button onclick="showPrevPart(2)" class="btn btn-secondary">Back</button>
                        <button onclick="showNextPart(2)" class="btn btn-primary">Next</button>
                    </div>
                </div>
            </div>
            <div id="instructionPart3" class="instruction-part" style="display: none;">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Part 3</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi.</p>
                    </div>
                    <div class="card-footer">
                        <div class="form-check text-start">
                            <input class="form-check-input" type="checkbox" value="" id="agreeCheckbox" required>
                            <label class="form-check-label" for="agreeCheckbox">
                                I agree to the terms and conditions
                            </label>
                        </div>
                        <div class="text-end mb-3">
                            <button onclick="showPrevPart(3)" class="btn btn-secondary">Back</button>
                            <button onclick="submitForm()" class="btn btn-primary" id="finishButton" disabled>Finish</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Instructions End -->

<script>
    let currentPart = 1;

    function showNextPart(partNumber) {
        document.getElementById(`instructionPart${currentPart}`).style.display = "none";
        currentPart = partNumber + 1;
        document.getElementById(`instructionPart${currentPart}`).style.display = "block";
    }

    function showPrevPart(partNumber) {
        document.getElementById(`instructionPart${currentPart}`).style.display = "none";
        currentPart = partNumber - 1;
        document.getElementById(`instructionPart${currentPart}`).style.display = "block";
    }

    function submitForm() {
        if (!document.getElementById('agreeCheckbox').checked) {
            // Highlight the checkbox
            document.getElementById('agreeCheckbox').classList.add('highlight');
            return; // Exit the function to prevent further execution
        }

        // Perform form submission or redirect to the next page
        alert("Form submitted successfully!");
        location.href = "tutors_evaluation_form.py?sno=%s";
    }

    document.getElementById('agreeCheckbox').addEventListener('change', function() {
        document.getElementById('finishButton').disabled = !this.checked;
        // Remove highlight when checkbox is checked
        if (this.checked) {
            document.getElementById('agreeCheckbox').classList.remove('highlight');
        }
    });
</script>

""" % id1)

print("""
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
