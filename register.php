<html>
<head>
<script>
function func()
{
	var pass= document.getElementById("pass").value;
var pass1=document.getElementById("pass1").value;
if(pass!=pass1)
	{alert("passwords do not match");
	return false;
	}
var a=f1.t1.value;
if(a=="")
{
alert("enter firstname");
return false;
}

var b=f1.t2.value;
if(b=="")
{
alert("enter lastname");
return false;
}

var a=f1.t3.value;
if(a=="")
{
alert("enter age");
return false;
}

var a=f1.t5.value;
if(a=="")
{
alert("enter email");
return false;
}











}
</script>

<style>
*{padding:0px;margin:0px}
.main{background-image:url(back.jpg);background-size:1000px 1000px;background-attachment: fixed}
.header{background-color:orange;height:200px;width:970px;margin:auto;}
.header h1{font-size:70px;text-align:center;line-height:200px;font-family:algerian}
.nav{background-color:black;height:50px;width:970px;margin:auto}
.cont{background-image:url(cont.jpg);background-size:100% 100%;
height:750px;width:970px;margin:auto}
.left{background-color:white;height:750px;width:300px;margin:auto;float:left;opacity:0.3;
filter:alpha(opacity=30);
}
.footer{background-color:grey;height:100px;width:970px;margin:auto}
.list{padding-left:20px}
li{float:left;list-style:none}
.list li a{text-decoration:none;display:block;height:50px;width:150px;line-height:50px;
color:grey;text-style:bold}
.list li a:hover{font-size:23px;color:white}
.list2{display:none;}
form{background-color:white;
text-align:center;
border:10px solid black;border-radius:30px;
width:400; height:500;}
.head{text-align:left; color:blue;}
.right{position:absolute}
.d2{position:relative;top:100px;left:450;}

</style>
</head>
<body>
<div class="main">
<div class="header">
<h1>SoNg FeVeR</h1>
</div>
<div class="nav">
<ul class="list">
<li><a href="sfhome.html" target="_blank">HOME</a></li>
<li><a href="languages.html" target="_blank">LANGUAGES</a></li>       
<li><a href="genre.html" target="_blank">GENRE</a></li>
<li><a href="artist.html" target="_blank">ARTIST</a></li>
<li><a href="login.php" target="_blank">LOGIN</a></li>
<li><a href="aboutus.html" target="_blank">ABOUT US</a></li>
</ul>
</div>
<div class="cont">
<div class="left">
<marquee direction="down" scrollamount="5">
<p>What is that in music that pulls you to listen it more? #music #artist #musician #newsong #spirit #Songs #Popular #Energy #questiontime</p><br>
<p>"You have to go to that broken part of your heart to #write #songs" #LaDyGaGa (..gReAtNeSs is produced by SUFFERiNg) #LoVe #mUsiC #PAiN #aRt</p><br>
<p>This tin makes me feel #weird @MuhdyungG Ar u his #idol @BadmanBinladin  or vise versa ...but u ar all killin me wit ur all ur #songs</p><br>
<p>Random thought: just listened to Joe Jackson's song Steppin' Out. Such a great song. #SONGS</p><br>
<p>If music be the food of love, play on. #Shakespeare #quotes #music #Kpop #hiphop #rap #Electro #songs #MusicInspiresLife #music	islife #life</p><br>
<p>If you people love music/maroon 5 you will love these guys.#music #slightlyleftofcentre #Maroon5 #pop #funky #Australia #songs #dance</p><br>
<p>Trying to find great music for an epic DJ playlist. Any song suggestions? #music #songs</p><br>
</marquee>
</div>
<div class="right">
<div class="d2">
<form action="register.php" onsubmit="return func()" name="f1" method="post">
<table align="center" cellspacing="10px">

<tr><th>first name:</th><td><input type=text id="fname" name="t1" style="border-radius:10px;width:200px;height:30px;" placeholder=firstname> </td></tr>
<tr><th>Last name:</th><td><input type=text id="lname" style="border-radius:10px;width:200px;height:30px;"name="t2" placeholder=lastname> </td></tr>
<tr><th>Age:</th><td><input type=number name="t3"style="border-radius:10px;width:200px;height:30px;" placeholder=age></td></tr>
<tr><th>Gender:</th><td>
      <input type=radio name=sex value=male>male  
      <input type=radio name=sex value=female>female
<tr><th>Email id:</th><td><input type=email id="i4" style="border-radius:10px;width:200px;height:30px;" name="t5" placeholder=email></td></tr>
<tr><th>Date of birth::</th><td><input type="date" style="border-radius:10px;width:200px;height:30px;"name="t6"  placeholder=birthdate></td></tr>
<tr><th>Mobile no::</th><td><input type=number style="border-radius:10px;width:200px;height:30px;" id="i4" name="t7" placeholder=contact number></td></tr>
<tr><th>user id:</th><td><input type=text style="border-radius:10px;width:200px;height:30px;" name="t8" id="i5" placeholder=username></td></tr>
<tr><th>password:</th><td><input type=password  style="border-radius:10px;width:200px;height:30px;"name="t9" id="pass" placeholder=password></td></tr>
<tr><th>confirm password:</th><td><input type=password style="border-radius:10px;width:200px;height:30px;"id="pass1" name="t10" placeholder= confirm password></td></tr>
</table>
<input type=submit value=submit style="border-radius:10px;width:200px;height:30px;" name="sub" style="background-color:violet">
<br> <input type=reset value=reset style="border-radius:10px;width:200px;height:30px;"style="background-color:black;color:white;" >


</form>


</div>
</div>
</div>
<div class="footer">
</div>
</div>
</body>
</html>
<?php
if(isset($_POST['sub']))
{
$fname=$_POST['t1'];
$lname=$_POST['t2'];
$age=$_POST['t3'];
$email=$_POST['t5'];
$dob=$_POST['t6'];
$contact=$_POST['t7'];
$userid=$_POST['t8'];
$password=$_POST['t9'];
$cnfpassword=$_POST['t10'];

$con=mysqli_connect("localhost","root","","sf");
if($con){
	echo "error";}
	
	
		$q=mysqli_query($con,"insert into registry values('$fname','$lname','$age','$email','$dob','$contact','$userid','$password','$cnfpassword')");
		//$row=mysqli_fetch_array($q);
		
		if($q)
		{
			echo "<script>alert('value inserted');</script>";
		}
	}
	else{
	echo "database not connected";	
			
	}	
?>