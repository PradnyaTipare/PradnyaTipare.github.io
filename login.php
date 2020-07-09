<html>
<head>
<script>

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
width:300;height:350px;}
.head{text-align:left; color:blue;}
.right{position:absolute}
.d1{position:relative;top:200px;left:500;}
</style>
</head>
<body>
<div class="main">
<div class="header">
<h1>SONG FEVER</h1>
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
<p>If music be the food of love, play on. #Shakespeare #quotes #music #Kpop #hiphop #rap #Electro #songs #MusicInspiresLife #musicislife #life</p><br>
<p>If you people love music/maroon 5 you will love these guys.#music #slightlyleftofcentre #Maroon5 #pop #funky #Australia #songs #dance</p><br>
<p>Trying to find great music for an epic DJ playlist. Any song suggestions? #music #songs</p><br>
</marquee>
</div>
<div class="right">
<div class="d1">
<form  action="" onsubmit="return func();" method="POST">
<br><br>
<table align="center" cellspacing="10px">

<tr><th>User id:</th><td><input type="text" name="uname"  placeholder="username" style="border-radius:10px;width:200px;height:30px;"></td></tr>
<tr><th>Password:</th><td><input type="password" name="pass" style="border-radius:10px;width:200px;height:30px;" placeholder="password"></td></tr>
</table>
<input type="submit" name="submit" value="Login" style="background-color:black;color:white;border-radius:10px;width:200px;height:40px; " onclick="return func();"><br></br>
<tr><th> No account yet?<b> <a href="register.php">Sign up</a><br></br></b>
<tr><th>  <a href="">forgot password?</a><br></br>
 <tr><th> <a href="www.gmail.com">Continue using Google</a><br></br>
 <tr><th> <a href="www.facebook.com">Continue using Facebook</a><br></br>  
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
if(isset($_POST['submit'])){	
	session_start();
$con=mysqli_connect("localhost","root","","sf");

if(!$con){
die("error!");}
	$uname=@$_POST["uname"];
	$pass=@$_POST["pass"];
	$sql="select * from registry where userid='$uname' and password='$pass'";
	$result=mysqli_query($con,$sql);	
	echo $row=mysqli_num_rows($result);
	if($row)
	{	
		$_SESSION['userid']=$uname;
		header('location:user.php');
	}
	else
	{
	echo "<script>alert('invalid credentials')</script>";	
	}

}
?>