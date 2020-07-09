<html>
<head>
<style>
form{background-color:pink;
text-align:center;
border:5px solid red;
width:300; height:400;}
.head{text-align:left; color:blue;}

</style>
</head>
<script>
function func(){
	var pass= document.getElementById("pass");
var pass1=document.getElementById("pass1");
if(pass!=pass1)
	alert("passwords do not match");
	return false;
}

</script>
<body>

<form action="" onsubmit="return func()" method="post">
<table align="center" cellspacing="10px">

<tr><th>first name:</th><td><input type=text name="t1" placeholder=firstname></td></tr>
<tr><th>Last name:</th><td><input type=text name="t2" placeholder=lastname> </td></tr>
<tr><th>Age:</th><td><input type=number name="t3" placeholder=age></td></tr>
<tr><th>Gender:</th><td>
      <input type=radio name=sex value=male>male
      <input type=radio name=sex value=female>female
<tr><th>Email id:</th><td><input type=email name="t5" placeholder=email></td></tr>
<tr><th>Date of birth::</th><td><input type="date" name="t6"  placeholder=birthdate></td></tr>
<tr><th>Mobile no::</th><td><input type=number name="t7" placeholder=contact number></td></tr>
<tr><th>user id:</th><td><input type=text name="t8" placeholder=username></td></tr>
<tr><th>password:</th><td><input type=password name="t9" id="pass" placeholder=password></td></tr>
<tr><th>confirm password:</th><td><input type=password id="pass1" name="t10" placeholder= confirm password></td></tr>
</table>
<input type=submit value=submit name="sub" style="background-color:violet">
<input type=reset value=reset style="background-color:violet" >


</form>

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

$con=mysql_connect("localhost","root","");
if($con){
	mysql_select_db("sf",$con);
	
	if($_POST['sub']=='submit')
	{
		$q=mysql_query("insert into registry values('$fname','$lname','$age','$email','$dob','$contact','$userid','$password','$cnfpassword')",$con);
		if($q)
		{
			echo ("<script>alert('value inserted');</script>");
		}
	}}
	else{
	echo "database not connected";	
			
	}

	
}	
	

?>