<!DOCTYPE html>
<html lang="en">
  <head>
  	<script type = "text/javascript">
  		//alert(localStorage.user);
  		if(localStorage.user==null){
  			window.location.href="frontend/login.html";
  		}
  		else{
  			window.location.href="frontend/start.html";
  		}
  	</script>
  </head>
  <body>
  </body>
</html>
