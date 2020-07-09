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
			echo "<script>alert('value inserted')</script>";
		}
	}

	}
}
else{
echo "database not connected";
}
}
else{
echo "server not connected";
}
?>