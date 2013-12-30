<?php
//test account: email:theyonester@gmail.com password:fuckyoni

include("dbconnect.php");
$email = $_GET['email'];
$password = $_GET['password'];

$users=$db->users;
$cursor=$users->find(array("email"=>$email,"password"=>$password));
if($cursor->count()==0){
	echo("no");
}
else{
	//setcookie("User",$email);
	echo("yes");
}

?>