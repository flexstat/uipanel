<?
session_start();
if(!isset($_SESSION['user_id'])) {
    header("Location: /auth.php");
    exit;
}

?>


<!DOCTYPE html>
<!--=== Coding by CodingLab | www.codinglabweb.com === -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!----======== CSS ======== -->
    <link rel="stylesheet" href="style.css">
     
    <!----===== Iconscout CSS ===== -->
    <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>



    <!--<title>Admin Dashboard Panel</title>--> 
</head>
<body>
    <nav>
        <div class="logo-name">
            <div class="logo-image">
                <!--<img src="images/logo.png" alt="">-->
            </div>

            <span class="logo_name">CloseDoorLab</span>
        </div>

        <div class="menu-items">
            <ul class="nav-links">
                <li><a href="panel.php">
                    <i class="uil uil-estate"></i>
                    <span class="link-name">Dahsboard</span>
                </a></li>
                <li><a href="#">
                    <i class="uil uil-files-landscapes"></i>
                    <span class="link-name">Protection</span>
                </a></li>
                <li><a href="#">
                    <i class="uil uil-chart"></i>
                    <span class="link-name">Analytics</span>
                </a></li>
            </ul>
            
            <ul class="logout-mode">
                <li><a href="exit.php">
                    <i class="uil uil-signout"></i>
                    <span class="link-name">Logout</span>
                </a></li>

                <li class="mode">
                    <a href="#">
                        <i class="uil uil-moon"></i>
                    <span class="link-name">Dark Mode</span>
                </a>

                <div class="mode-toggle">
                  <span class="switch"></span>
                </div>
            </li>
            </ul>
        </div>
    </nav>

    <section class="dashboard">
        <div class="top">
            <i class="uil uil-bars sidebar-toggle"></i>

            <div class="search-box">
                <i class="uil uil-search"></i>
                <input type="text" placeholder="Search here...">
            </div>
            
            <!--<img src="images/profile.jpg" alt="">-->
        </div>

        <div class="dash-content">
            <div class="overview">
                <div class="title">
                    <i class="uil uil-tachometer-fast-alt"></i>
                    <span class="text">Add domen/ip</span>
                </div>
                    <img id="gif" class="load" src="preview.gif" alt="">
                    <div id="result_form"> </div>
                    <div id="load"> </div>
                    <form id="add" action="" method="post">
    <input id="domain" name="field1" class="form-control"  type="text" placeholder="??????????" required="true" />
    <br>
    <input id="ip" name="field2" class="form-control"  type="text" placeholder="ip ?????????? ??????????" required="true" />
    <br>
    <input id="button" type="submit" class="btn btn-success"  name="submit" value="Save">
</form>

                    </div>
                </div>
            </div>
        </div>
    </section>

    <script src="script.js"></script>
</body>
</html>


<script>
$(document).ready(function() {
    $("#add").submit(function() {
         var result_add = 0;
         document.getElementById("button").disabled = true; 
         $('#gif').show();
        $.ajax({
            type: "POST",
            url: 'myprocessingscript.php',
            data:$("#add").serialize(),
            success: function (data) {
                // Inserting html into the result div on success
                $('#result_form').html('?????????? ?????????????? ????????????????');
                $('#ip').val('');
                $('#domain').val('');
                document.getElementById("button").disabled = false; 
                $('#gif').hide();

            },
            error: function(jqXHR, text, error){
            // Displaying if there are any errors
                $('#result_form').html(error);
        }
    });
        return false;
    });
});
</script>


