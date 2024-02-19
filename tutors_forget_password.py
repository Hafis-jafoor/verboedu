#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import cgi
import pymysql
import random
otp = random.randint(00000, 99999)


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
                    <h1 class="display-3 text-white animated slideInDown">Tutors Forget Password</h1>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb justify-content-center">
                            <li class="breadcrumb-item"><a class="text-white" href="#">Home</a></li>
                            <!-- <li class="breadcrumb-item"><a class="text-white" href="#">Pages</a></li> -->
                            <li class="breadcrumb-item text-white active" aria-current="page">Password Forgot</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>
    <!-- Header End -->

    <!-- Form Start -->
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-6">
                <h2 class="text-center mb-4">Tutors Forget Password</h2>
                <form action="#" method="post" role="form" id="loginForm">
                    <div class="mb-3">
                        <label for="username" class="form-label">Linked Email</label>
                        <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email" required>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="mb-3 d-grid gap-2">
                                <input type="submit" class="btn btn btn-lg" id="submitButton" name="sub" value="Send Otp" style="background: #00A79D;color: white;">
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                        </div>
                        <div class="col-md-6 text-end">
                            <p><a href="tutors_login.py">Back login page?</a></p>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <!-- Form End -->

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
</html>

""")

a = cgi.FieldStorage()
email = a.getvalue("email")
sub = a.getvalue("sub")
if sub is not None:
    cur.execute("""select slno,email from tutors_registeration where email = '%s'""" % email)
    f = cur.fetchone()
    if f is not None:
        import smtplib
        from email.message import EmailMessage

        fromaccount = "sticknobillshafis@gmail.com"
        password = "voyp trhk rhox oekl"
        toaccount = email
        msg = EmailMessage()
        msg.set_content(' This is your OTP: %s' % otp)

        msg['Subject'] = 'admin password reset'
        msg['From'] = "sticknobillshafis@gmail.com"
        msg['To'] = email

        # This is your  password reset otp :%s"""%(otp)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromaccount, password)
        server.send_message(msg)
        server.quit()
        print("""
        <script>
           alert(" email(otp) sent successfully..!");
           location.href = "tutors_forget_otp.py?otp=%s&sno=%s"
        </script>
        """ % (otp, f[0]))
    else:
        print("""
        <script>
           alert(" email not registered or linked..!");
        </script>
        """)
