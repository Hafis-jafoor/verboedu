#!C:\Users\PC\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n\r\n")

import cgi
import pymysql

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
                    <h1 class="display-3 text-white animated slideInDown">Become a Tutor</h1>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb justify-content-center">
                            <li class="breadcrumb-item"><a class="text-white" href="#">Home</a></li>
                            <!-- <li class="breadcrumb-item"><a class="text-white" href="#">Pages</a></li> -->
                            <li class="breadcrumb-item text-white active" aria-current="page">Tutor Registration</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>
    <!-- Header End -->
""")
print("""
<!-- Form Start -->
<div class="container my-5">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card">
                <div class="card-body">
                    <h2 class="card-title text-center mb-4">Tutor Registration Form</h2>
                    <form method = "post">
                        <div class="row">
                            <div class="col">
                                <div class="mb-3">
                                    <label for="name" class="form-label">Full Name</label>
                                    <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name" oninput="validateName(this)" required>
                                    <small id="nameValidationText" style="color: red; display: none;">Please enter a valid name (only alphabets and spaces).</small>
                                </div>
                            </div>
                            <script>
                                function validateName(input) {
                                    var nameRegex = /^[a-zA-Z\s]+$/;
                                    var nameInput = input.value;
                                    var nameValidationText = document.getElementById("nameValidationText");

                                    if (!nameRegex.test(nameInput)) {
                                        nameValidationText.style.display = "inline";
                                    } else {
                                        nameValidationText.style.display = "none";
                                    }
                                }
                            </script>
                            <div class="col">
                                <div class="mb-3">
                                    <label for="email" class="form-label">Email</label>
                                    <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email" oninput="validateEmail(this)" required>
                                    <small id="emailValidationText" style="color: red; display: none;">Please enter a valid email address.</small>
                                </div>                                
                            </div>
                            <script>
                                function validateEmail(input) {
                                    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                                    var emailInput = input.value;
                                    var emailValidationText = document.getElementById("emailValidationText");

                                    if (!emailRegex.test(emailInput)) {
                                        emailValidationText.style.display = "inline";
                                    } else {
                                        emailValidationText.style.display = "none";
                                    }
                                }
                            </script>
                        </div>
                        <div class="row">
                            <div class="col">
                                <div class="mb-3">
                                    <label class="form-label d-block" for="gender">Gender</label>
                                    <select class="form-select" id="gender" name="gender" onchange="checkOther(this.value)" required>
                                        <option value="" disabled selected>Select Gender</option>
                                        <option value="male">Male</option>
                                        <option value="female">Female</option>
                                        <option value="other">Other (Please Specify)</option>
                                    </select>
                                    <input type="text" class="form-control mt-2" id="otherGender" name="otherGender" placeholder="Specify your gender" style="display: none;">
                                </div>
                                <script>
                                    function checkOther(selectedValue) {
                                        var otherGenderInput = document.getElementById("otherGender");
                                        if (selectedValue === "other") {
                                            otherGenderInput.style.display = "block";
                                            otherGenderInput.setAttribute("required", "true"); // make the input required
                                        } else {
                                            otherGenderInput.style.display = "none";
                                            otherGenderInput.removeAttribute("required"); // remove the required attribute
                                        }
                                    }
                                </script>
                            </div>
                            <div class="col">
                                <div class="mb-3">
                                    <label for="dob" class="form-label">Date of Birth</label>
                                    <input type="date" class="form-control" id="dob" name="dob" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <div class="mb-3">
                                    <label for="whatsapp" class="form-label">WhatsApp Number</label>
                                    <input type="text" class="form-control" id="whatsapp" name="whatsapp" placeholder="Enter your WhatsApp number" oninput="validateWhatsApp(this)" required>
                                    <small id="whatsappValidationText" style="color: red; display: none;">Please enter a valid WhatsApp number (starting with a digit from 1 to 9 and exactly 10 digits).</small>
                                </div>
                                <script>
                                    function validateWhatsApp(input) {
                                        var whatsappRegex = /^[1-9]\d{9}$/;  // Updated regex to start with digit 1-9 and exactly 10 digits
                                        var whatsappInput = input.value;
                                        var whatsappValidationText = document.getElementById("whatsappValidationText");
                                
                                        if (!whatsappRegex.test(whatsappInput)) {
                                            whatsappValidationText.style.display = "inline";
                                        } else {
                                            whatsappValidationText.style.display = "none";
                                        }
                                    }
                                </script>
                            </div>     
                            <div class="col">
                                <div class="mb-3">
                                    <label for="contact" class="form-label">Contact Number</label>
                                    <input type="text" class="form-control" id="contact" name="contact" placeholder="Enter your contact number" oninput="validateContact(this)" required>
                                    <small id="contactValidationText" style="color: red; display: none;">Please enter a valid contact number (starting with a digit from 1 to 9 and exactly 10 digits).</small>
                                </div>
                                <script>
                                    function validateContact(input) {
                                        var contactRegex = /^[1-9]\d{9}$/;  // Regex to start with digit 1-9 and exactly 10 digits
                                        var contactInput = input.value;
                                        var contactValidationText = document.getElementById("contactValidationText");
                                
                                        if (!contactRegex.test(contactInput)) {
                                            contactValidationText.style.display = "inline";
                                        } else {
                                            contactValidationText.style.display = "none";
                                        }
                                    }
                                </script>                                
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="qualification" class="form-label">Qualification/Currently persuing</label>
                            <input type="text" class="form-control" id="qualification" name="qualification" placeholder="Enter your qualification" required>
                        </div>
                        <div class="mb-3">
                            <label for="languages" class="form-label">Spoken Languages</label>
                            <select id="languages" name="languages[]" class="form-select" multiple required onclick="toggleSelectedLanguage(event)">
                                <option value="english">English</option>
                                <option value="malayalam">Malayalam</option>
                                <option value="hindi">Hindi</option>
                                <option value="tamil">Tamil</option>
                                <option value="arabic">Arabic</option>
                                <!-- Add more languages as needed -->
                                <option value="others">Others</option>
                            </select>
                        </div>
                        
                        <div class="mb-3">
                            <label for="selectedLanguages" class="form-label">Selected Languages</label>
                            <input type="text" id="selectedLanguages" class="form-control" readonly onclick="removeSelectedLanguage(event)" name="selectedLanguages">
                        </div>

                        <div class="mb-3" id="othersInputContainer" style="display: none;">
                            <label for="otherLanguages" class="form-label">Other Languages</label>
                            <input type="text" id="otherLanguages" class="form-control" name="otherLanguages">
                        </div>
                        <script>
                            function toggleSelectedLanguage(event) {
                                var option = event.target;
                                var inputElement = document.getElementById("selectedLanguages");
                                var othersInputContainer = document.getElementById("othersInputContainer");
                        
                                if (option.tagName === "OPTION") {
                                    if (option.value === "others") {
                                        othersInputContainer.style.display = "block";
                                    } else {
                                        othersInputContainer.style.display = "none";
                        
                                        var selectedLanguages = inputElement.value.split(',').map(lang => lang.trim());
                                        if (!selectedLanguages.includes(option.text)) {
                                            selectedLanguages.push(option.text);
                                        } else {
                                            selectedLanguages = selectedLanguages.filter(lang => lang !== option.text);
                                        }
                        
                                        inputElement.value = selectedLanguages.join(", ");
                                    }
                                }
                            }
                        
                            function removeSelectedLanguage(event) {
                                var clickedLanguage = event.target.value;
                                var inputElement = document.getElementById("selectedLanguages");
                                var selectedLanguages = inputElement.value.split(',').map(lang => lang.trim());
                        
                                var index = selectedLanguages.indexOf(clickedLanguage);
                                if (index !== -1) {
                                    selectedLanguages.splice(index, 1);
                                    inputElement.value = selectedLanguages.join(", ");
                                }
                            }
                        </script>
        
                        <div class="row">
                            <div class="col">
                                <div class="mb-3">
                                    <label class="form-label d-block">Do you have online teaching experience?
                                    </label>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="on_teaching_experience" id="on_experience_yes" value="yes" required>
                                        <label class="form-check-label" for="on_experience_yes">Yes</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="on_teaching_experience" id="on_experience_no" value="no">
                                        <label class="form-check-label" for="on_experience_no">No</label>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="mb-3">
                                    <label class="form-label d-block">Do you have offline teaching experience?</label>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="off_teaching_experience" id="off_experience_yes" value="yes" required>
                                        <label class="form-check-label" for="off_experience_yes">Yes</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="off_teaching_experience" id="off_experience_no" value="no">
                                        <label class="form-check-label" for="off_experience_no">No</label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12 col-md-12 col-sm-6">
                                <div class="mb-3">
                                    <label class="form-label d-block">Are you available for offline classes(Home Tutions)?</label>
                                    
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="offline_teaching_experience" id="offline_experience_yes" value="yes" required onchange="toggleNoteSection()">
                                        <label class="form-check-label" for="offline_experience_yes">Yes</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="offline_teaching_experience" id="offline_experience_no" value="no" onchange="toggleNoteSection()">
                                        <label class="form-check-label" for="offline_experience_no">No</label>
                                    </div>
                                    <div id="noteSection" style="display: none;color: green;">
                                        <label class="form-label d-block">Note: Offline classes will be within 10 km from your area.</label>
                                        <label class="form-label d-block">Travel allowance will be provided.</label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <script>
                            function toggleNoteSection() {
                                var noteSection = document.getElementById("noteSection");
                                var yesRadioButton = document.getElementById("offline_experience_yes");
                        
                                if (yesRadioButton.checked) {
                                    noteSection.style.display = "block";
                                } else {
                                    noteSection.style.display = "none";
                                }
                            }
                        </script>
                             
                        <div class="mb-3">
                            <label class="form-label d-block">Select the class which you can teach</label>
                            <div class="container">
                                <div class="row">
                                    <!-- first col -->
                                    <div class="col">
                                        <!-- KG class -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="kg" id="kg" name="kg">
                                            <label class="form-check-label" for="kg">
                                                KG
                                            </label>
                                        </div>
                                        <!-- 1 - 4 class -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="one_four" id="one_four" name="one_four">
                                            <label class="form-check-label" for="one_four">
                                                1 - 4
                                            </label>
                                        </div>
                                        <!-- 5 - 7 class -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="five_seven" id="five_seven" name="five_seven">
                                            <label class="form-check-label" for="five_seven">
                                                5 - 7
                                            </label>
                                        </div>
                                        <!-- 8-10 -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="eight_ten" id="eight_ten" name="eight_ten">
                                            <label class="form-check-label" for="eight_ten">
                                                8 - 10
                                            </label>
                                        </div>    
                                        <!-- 11-12 -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="eleven_twelve" id="eleven_twelve" name="eleven_twelve">
                                            <label class="form-check-label" for="eleven_twelve">
                                                11 & 12
                                            </label>
                                        </div>
                                        <!-- btech -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="btech" id="btech" name="btech">
                                            <label class="form-check-label" for="btech">
                                                BTech
                                            </label>
                                        </div>
                                    </div>

                                    <!-- second col -->
                                    <div class="col">
                                        <!-- ug -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="ug" id="ug" name="ug">
                                            <label class="form-check-label" for="ug">
                                                UG
                                            </label>
                                        </div>
                                        <!-- PG Subjects Section -->
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="pg" id="pg" name="pg">
                                            <label class="form-check-label" for="pg">PG</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="art_and_craft" id="art_and_craft" name="art_and_craft">
                                            <label class="form-check-label" for="art_and_craft">Art &amp; Craft</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="drawing" id="drawing" name="drawing">
                                            <label class="form-check-label" for="drawing">Drawing</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="music" id="music" name="music">
                                            <label class="form-check-label" for="music">Music</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="dance" id="dance" name="dance">
                                            <label class="form-check-label" for="dance">Dance</label>
                                        </div>
                                    </div>

                                    <!-- third col -->
                                    <div class="col">
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="abacus" id="abacus" name="abacus">
                                            <label class="form-check-label" for="abacus">Abacus</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="ielts" id="ielts" name="ielts">
                                            <label class="form-check-label" for="ielts">IELTS</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="coding" id="coding" name="coding">
                                            <label class="form-check-label" for="coding">Coding</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="foreign_language" id="foreign_language" name="foreign_language">
                                            <label class="form-check-label" for="foreign_language">Foreign Language</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="country" class="form-label">Country</label>
                            <select class="form-select" id="country" name="country" required>
                                <option value="" selected disabled>Select your country</option>
                                <!-- Populate options dynamically with JavaScript -->
                                <option value="India">India</option>
                                <!-- Add other countries dynamically -->
                            </select>
                        </div>
                        <div id="indiaFields" style="display: none;">
                            <div class="mb-3">
                                <label for="state" class="form-label">State</label>
                                <input type="text" class="form-control" id="state" name="state" placeholder="Enter your state" >
                            </div>
                            <div class="mb-3">
                                <label for="district" class="form-label">District</label>
                                <input type="text" class="form-control" id="district" name="district" placeholder="Enter your district" >
                            </div>
                            <div class="mb-3">
                                <label for="taluk" class="form-label">Taluk</label>
                                <input type="text" class="form-control" id="taluk" name="taluk" placeholder="Enter your taluk" >
                            </div>
                        </div>
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
                        
                        <div class="text-center">
                            <input type="submit" class="btn btn-primary" name="sub" value="Submit">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Form End -->

<script>
    // Fetch the list of countries from the Rest Countries API
    fetch("https://restcountries.com/v3.1/all")
        .then(response => response.json())
        .then(data => {
            // Get the select element
            const countrySelect = document.getElementById("country");

            // Populate the select element with options
            data.forEach(country => {
                const option = document.createElement("option");
                option.text = country.name.common;
                option.value = country.name.common;
                countrySelect.add(option);
            });
        })
        .catch(error => console.error("Error fetching countries:", error));

        // Add event listener to the country select dropdown
        document.getElementById("country").addEventListener("change", function() {
            var selectedCountry = this.value;
            var indiaFields = document.getElementById("indiaFields");
            
            // If the selected country is India, show the additional fields
            if (selectedCountry === "India") {
                indiaFields.style.display = "block";
            } else {
                // Otherwise, hide the additional fields
                indiaFields.style.display = "none";
            }
        });
</script>

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

f = cgi.FieldStorage()
name = f.getvalue("name")
email = f.getvalue("email")
gender = f.getvalue("gender")
otherGender = f.getvalue("otherGender")
dob = f.getvalue("dob")
whatsapp = f.getvalue("whatsapp")
contact = f.getvalue("contact")
qualification = f.getvalue("qualification")
selectedLanguages = f.getvalue("selectedLanguages")
otherLanguages = f.getvalue("otherLanguages")
on_teaching_experience = f.getvalue("on_teaching_experience")
off_teaching_experience = f.getvalue("off_teaching_experience")
offline_teaching_experience = f.getvalue("offline_teaching_experience")
kg = f.getvalue("kg")
one_four = f.getvalue("one_four")
five_seven = f.getvalue("five_seven")
eight_ten = f.getvalue("eight_ten")
eleven_twelve = f.getvalue("eleven_twelve")
btech = f.getvalue("btech")
ug = f.getvalue("ug")
pg = f.getvalue("pg")
art_and_craft = f.getvalue("art_and_craft")
drawing = f.getvalue("drawing")
music = f.getvalue("music")
dance = f.getvalue("dance")
abacus = f.getvalue("abacus")
ielts = f.getvalue("ielts")
coding = f.getvalue("coding")
foreign_language = f.getvalue("foreign_language")
country = f.getvalue("country")
state = f.getvalue("state")
district = f.getvalue("district")
taluk = f.getvalue("taluk")
confirmPassword = f.getvalue("confirmPassword")
sub = f.getvalue("sub")

if sub != None:
    cur.execute("""insert into tutors_registeration(full_name,email,gender,other_gender,
        watsapp_no,contact_no,qualification_currently_persuing,spoken_language,online_exp,
        offline_exp,available_offline,kg,1_4,5_7,8_10,11_12,btech,ug,pg,arts_craft,drawing,music,
        dance,abacus,ielts,coding,foreign_language,country,state,district,taluk,password,
        dob,other_spoken_language)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'
        ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
        '%s','%s','%s','%s','%s','%s')
                       """ % (name, email, gender, otherGender, whatsapp, contact, qualification, selectedLanguages,
                              on_teaching_experience, off_teaching_experience, offline_teaching_experience,
                              kg, one_four, five_seven, eight_ten, eleven_twelve, btech, ug, pg, art_and_craft,
                              drawing, music, dance, abacus, ielts, coding, foreign_language, country, state,
                              district, taluk, confirmPassword, dob, otherLanguages))
    conn.commit()
    print("""
            <script>
                alert("successfully");
            </script>
            """)

# cur.execute("""select * from tutors_registeration where email = '%s' and contact_no = '%s' """
#             % (email, contact))
# f = cur.fetchone()
# if f != None:


# if sub != None:
#     # Check if user already exists
#     cur.execute("SELECT * FROM tutors_registeration WHERE email = %s OR contact_no = %s", (email, contact))
#     if cur.fetchone() is None:
#         # Insert new user
#         cur.execute("""INSERT INTO tutors_registeration (full_name, email, gender, other_gender, watsapp_no,
#                        contact_no, qualification_currently_persuing, spoken_language, online_exp, offline_exp,
#                        available_offline, kg, 1_4, 5_7, 8_10, 11_12, btech, ug, pg, arts_craft, drawing, music,
#                        dance, abacus, ielts, coding, foreign_language, country, state, district, taluk, password,
#                        dob, other_spoken_language)
#                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
#                     (name, email, gender, otherGender, whatsapp, contact, qualification, selectedLanguages,
#                      on_teaching_experience, off_teaching_experience, offline_teaching_experience, kg, one_four,
#                      five_seven, eight_ten, eleven_twelve, btech, ug, pg, art_and_craft, drawing, music, dance,
#                      abacus, ielts, coding, foreign_language, country, state, district, taluk, confirmPassword, dob,
#                      otherLanguages))
#         conn.commit()
#         print("""
#             <script>
#                 alert("Inserted successfully");
#             </script>
#         """)
#     else:
#         print("""
#             <script>
#                 alert("User with this email or contact number already exists");
#             </script>
#         """)
#
# cur.close()
# conn.close()
