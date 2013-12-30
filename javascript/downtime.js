
function login(){
	var email_input = document.getElementById("email_input").value;
	var pw_input = document.getElementById("pw_input").value;
	
	/* alert(email_input + pw_input);
	if(email_input = "yes"){
    	document.getElementById("pw_wrong").style.display= "inline";
 	 };
 	*/
 	//alert(email_input);
 	//alert(pw_input);

	$.get( "../backend/login.php", { email: email_input, password: pw_input} )
		.done(function( data ) {
			//alert('stop this shit');
    		if(data == "yes"){
    			localStorage.user=email_input;
    			window.location.href = "start.html";
  			} else {
    			document.getElementById("pw_wrong").style.display= "inline";
  			}
  		});
  	return false;

} 

$('#loginForm').submit(function () {
	//alert('i know this got clicked');
 //sendContactForm();
 return false;
});

function setCookie(c_name,value,exdays)
{
	var exdate=new Date();
	exdate.setDate(exdate.getDate() + exdays);
	var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
	document.cookie=c_name + "=" + c_value;
}

function addCat(a) {
	if (document.getElementById(a+"l").className !== "active") {
		document.getElementById(a+"l").className="active";
	} else {
		document.getElementById(a+"l").className="";
	}

}





function register(){
	var name = document.getElementById("name").value;
	var email = document.getElementById("email").value;
	var password = document.getElementById("password").value;
	var interests = "";
	
	if(document.getElementById("artsl").className == "active") {
		interests+="arts,";
	} if(document.getElementById("entertainmentl").className == "active"){
		interests+="entertainment,";
	} if(document.getElementById("sportsl").className == "active"){
		interests+="sports,";
	} if(document.getElementById("techl").className == "active"){
		interests+="tech,";
	} if(document.getElementById("worldl").className == "active"){
		interests+="world,";
	} if(document.getElementById("politicsl").className == "active"){
		interests+="politics,";
	} if(document.getElementById("catsl").className == "active"){
		interests+="cats,";
	}

	interests = interests.substring(0, interests.length - 1);

	$.get( "../backend/register.php", { name: name, email: email, password: password, interests: interests} )
		.done(function( data ) {
			localStorage.user = email;
			window.location.href = "start.html";
    		
  		}); 
}






	/* alert(email_input + pw_input);
	if(email_input = "yes"){
    	document.getElementById("pw_wrong").style.display= "inline";
 	 };
 	*/
 	//alert(email_input);
 	//alert(pw_input);

	// $.get( "../backend/login.php", { email: email_input, password: pw_input} )
	// 	.done(function( data ) {
	// 		//alert('stop this shit');
 //    		if(data == "yes"){
 //    			localStorage.user=email_input;
 //    			window.location.href = "start.html";
 //  			} else {
 //    			document.getElementById("pw_wrong").style.display= "inline";
 //  			}
 //  		});
 //  	return false;



$('#loginForm').submit(function () {
	//alert('i know this got clicked');
 //sendContactForm();
 return false;
});


$('#registerForm').submit(function () {
	//alert('i know this got clicked');
 //sendContactForm();
 return false;
});

