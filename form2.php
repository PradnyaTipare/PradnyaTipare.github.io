<html>
<head>
<style>
form{background-color:pink;
text-align:center;
border:5px solid red;
width:300;}
.head{text-align:left; color:blue;}
</style>
</head>
<body>
<form  action="" method="POST">

<table align="center" cellspacing="10px">

<tr><th>User id:</th><td><input type="text" name="uname" placeholder="username"></td></tr>
<tr><th>Password:</th><td><input type="password" name="pass" placeholder="password"></td></tr>
</table>
<input type="submit" name="submit" value="Login" style="background-color:violet"><br></br>
<tr><th> No account yet?<b> <a href="form.php">Sign up</a><br></br></b>
<tr><th>  <a href="">forgot password?</a><br></br>
 <tr><th> <a href="www.gmail.com">Continue using Google</a><br></br>
 <tr><th> <a href="www.facebook.com">Continue using Facebook</a><br></br>  
</form>
</body>
</html>
<?php
if(isset($_POST['submit'])){	
	
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
			
		echo "www";
			//header('location:form.php');
	}
	else
	{
	echo "this is alert	";	
	}
}
?>