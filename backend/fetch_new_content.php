<?php
include("dbconnect.php");
$email = $_GET['user'];
$timeLeft=$_GET['timeLeft'];

$users = $db->users;
$userCursor=$users->find(array("email"=>$email));
$user=$userCursor->getNext();
$visitedUrls = $user['visited_urls'];
$userCategories = $user['interests'];

$items;
if($email=="jmetzman@princeton.edu"){
	$items= $db->sample_items;
}
else{
	$items = $db->items;
}


$tagsArray=array('$in'=>$userCategories);
$timeArray=array('$lt'=>$timeLeft);

$itemsCursor = $items->find(array("tags"=>$tagsArray,"duration"=>$timeArray));
foreach($itemsCursor as $item){
	if(!in_array($item['url'],$visitedUrls)){
		setUrlAsRead($item['url'],$user,$users);
		echo($item['url']);
		exit(0);
	}
}
$itemsCursor = $items->find(array("tags"=>$tagsArray));
foreach($itemsCursor as $item){
	if(!in_array($item['url'],$visitedUrls)){
		setUrlAsRead($item['url'],$user,$users);
		echo($item['url']);
		exit(0);
	}
}
$itemsCursor = $items->find(array("duration"=>$timeArray));
foreach($itemsCursor as $item){
	if(!in_array($item['url'],$visitedUrls)){
		setUrlAsRead($item['url'],$user,$users);
		echo($item['url']);
		exit(0);
	}
}
$itemsCursor = $items->find();
foreach($itemsCursor as $item){
	if(!in_array($item['url'],$visitedUrls)){
		setUrlAsRead($item['url'],$user,$users);
		echo($item['url']);
		exit(0);
	}
}

function setUrlAsRead($url, $user, $users) {
	$email = $user['email'];
	$visitedUrls = $user['visited_urls'];
	array_push($visitedUrls,$url);
	$user['visited_urls']=$visitedUrls;
	$users->update(array("email"=>$email),$user);
}

?>