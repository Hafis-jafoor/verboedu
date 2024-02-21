#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import pymysql
import cgi

a = cgi.FieldStorage()
id1 = a.getvalue("sno")

conn = pymysql.connect(host="localhost", user="root", password="", database="verbo")
cur = conn.cursor()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Verbo | The Individual Tution Platform</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="" name="keywords">
    <meta content="" name="description">

    <!-- webicon -->
    <link rel="website icon" type="jpg" href="img/verbo_website_icon.jpg">

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
    <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">

    <!-- Customized Bootstrap Stylesheet -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Template Stylesheet -->
    <link href="css/style.css" rel="stylesheet">
</head>

<body>
    <!-- Spinner Start -->
    <div id="spinner" class="show bg-white position-fixed translate-middle w-100 vh-100 top-50 start-50 d-flex align-items-center justify-content-center">
        <div class="spinner-border text-primary" style="width: 3rem; height: 3rem;" role="status">
            <span class="sr-only">Loading...</span>
        </div>
    </div>
    <!-- Spinner End -->

    <!-- Header Start -->
    <div class="container-fluid bg-primary py-5 mb-5 page-header" style="background: linear-gradient(  white,#00A79D);">
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-lg-10 text-center">
                    <h1 class="display-3 text-white animated slideInDown">Tutors Password Reset</h1>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb justify-content-center">
                            <li class="breadcrumb-item"><a class="text-white" href="#">Home</a></li>
                            <!-- <li class="breadcrumb-item"><a class="text-white" href="#">Pages</a></li> -->
                            <li class="breadcrumb-item text-white active" aria-current="page">Password Reset</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>
    <!-- Header End -->


    <!-- Form Section Start -->
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-lg-6">
            <form method = "post">
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" name="password" placeholder="Enter your password" oninput="validatePassword()" required>
                    <small id="passwordValidationText" style="color: red; display: none;">Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long</small>
                </div>

                <div class="mb-3">
                    <label for="confirmPassword" class="form-label">Confirm Password</label>
                    <input type="password" class="form-control" id="confirmPassword" name="confirmPassword" placeholder="Confirm your password" oninput="validatePassword()" required>
                    <small id="confirmPasswordValidationText" style="color: red; display: none;">Passwords do not match</small>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <div class="mb-3 d-grid gap-2">
                            <input type="submit" class="btn btn-primary btn-lg" name="sub" id="otpSubmitButton" value="Submit">
                        </div>
                    </div>
                </div>
                <script>
                            function validatePassword() {
                                var password = document.getElementById("password").value;
                                var confirmPassword = document.getElementById("confirmPassword").value;
                                var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$/;

                                var passwordValidationText = document.getElementById("passwordValidationText");
                                var confirmPasswordValidationText = document.getElementById("confirmPasswordValidationText");

                                if (!passwordRegex.test(password)) {
                                    passwordValidationText.style.display = "inline";
                                } else {
                                    passwordValidationText.style.display = "none";
                                }

                                if (password !== confirmPassword) {
                                    confirmPasswordValidationText.style.display = "inline";
                                } else {
                                    confirmPasswordValidationText.style.display = "none";
                                }
                            }
                        </script>
            </form>
        </div>
    </div>
</div>
<!-- Form Section End -->





    <!-- JavaScript Libraries -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="lib/wow/wow.min.js"></script>
    <script src="lib/easing/easing.min.js"></script>
    <script src="lib/waypoints/waypoints.min.js"></script>
    <script src="lib/owlcarousel/owl.carousel.min.js"></script>

    <!-- Template Javascript -->
    <script src="js/main.js"></script>
</body>

</html>""")

password = a.getvalue("password")
confirm_password = a.getvalue("confirmPassword")
sub = a.getvalue("sub")
if sub is not None:
    if password == confirm_password:
        cur.execute("""update tutors_registeration set password = '%s' where slno = '%s'""" % (password, id1))
        conn.commit()
        print("""
            <script>
               alert("password changed");
               location.href = "tutors_login.py"
            </script>
            """)
    else:
        print("""
            <script>
               alert("password not match");
            </script>
            """)
