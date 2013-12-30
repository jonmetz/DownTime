<?php
error_reporting(0);
//test account: email:theyonester@gmail.com password:fuckyoni

include("dbconnect.php");
$email = $_GET['email'];
$password = $_GET['password'];
$name = $_GET['name'];
$interests = $_GET['interests'];

$users=$db->users;
$cursor=$users->find(array("email"=>$email));
if($cursor->count()!=0){
	echo("no");
}
else{
	$user_array=array('email'=>$email,'password'=>$password,'name'=>$name,'name'=>$name, 'interests'=>explode(",",$interests), 'visited_urls'=>array());
	$users->insert($user_array);
	send_welcome_email($email,$name);
	echo("yes");
}


function send_welcome_email($email, $name){
	$url = 'https://sendgrid.com/api/mail.send.json';
//api_user=your_sendgrid_username&api_key=your_sendgrid_password&to=destination@example.com
//&toname=Destination&subject=Example_Subject&text=testingtextbody&from=info@domain.com
$fields = array(
						'api_user' => urlencode("lukel"),
						'api_key' => urlencode("fuckyoni"),
						'to' => urlencode($email),
						'toname' => urlencode($name),
						'subject' => urlencode("Welcome to DownTime - Explore our tools and services"),
						'text' => urlencode("Dear ".$name.",

Thank you for subscribing and welcome to DownTime, the only web app that lets you make the most out of the times when you want to think the least! In today's productivity driven culture, DownTime taps into the guilt we all feel when wasting time: transforming those minutes from guilt to guilty pleasure.

From all of us at DownTime we are excited to bring you content that sparks your interest and allows you to be the most productive you that you want to be.

Enjoy our product and confirm your account now at http://ec2-54-201-48-236.us-west-2.compute.amazonaws.com/team_fisher/backend/confirmation.php



Any Questions?

We're here to help you make the most of DownTime. If you have any questions or need technical assistance please email support@downtime.com


All The Best,
The DownTime Team"),
						'from' => urlencode("support@downtime.com")
				);

//url-ify the data for the POST
foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
rtrim($fields_string, '&');

//echo($fields_string);

//open connection
$ch = curl_init();

//set the url, number of POST vars, POST data
curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_POST, count($fields));
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);

//execute post
$result = curl_exec($ch);
//echo($result);

//close connection
curl_close($ch);
}

?>