
$(".registerButton").click(function(event) {
	/* Act on the event */
	$(".loginForm").hide( "slow");
	$(".loginButton").hide("slow");
	$(this).hide("slow");
	$(".registerForm").show("slow");
	initValidationErrors();
	$(".backToLoginContainer").show("slow");



});

$(".backToLoginContainer").click(function(event) {
	/* Act on the event */
	loginState();
});


function loginState(){
	$(".registerForm").hide("slow");
	$(".backToLoginContainer").hide("slow");
	initValidationErrors();
	$(".loginForm").show( "slow");
	$(".loginButton").show("slow");
	$(".registerButton").show("slow");
}

var clicks = 0;
$('.registerSubmitButton').click(function(){
	
	event.preventDefault();

	var data = {
		'username': $('.registerForm #username').val(),
		'email' : $('#email').val(),
    	'password1': $('#password1').val(),
    	'password2' : $('#password2').val()
    };
	initValidationAjax(data);
	return;

	

});

function initValidationErrors() {
	$(".reg-error").hide("slow")
	$(".reg-error").text("");
}

function initValidationAjax(obj_fields) {
	$.ajax({
        type: "POST",
        url: "/register/submit/",
        data: obj_fields,
        success: function(r) {
			if (r['errors']) {
				setupValidationErrors(r['errors']);
			} else {
				loginState();
				$(".creationLabel").show("slow");

			}
        },
        error: function(r) {
            console.log(r);
        }
	});
}

function setupValidationErrors(err_obj) {
	initValidationErrors();
	var error_field_class = '.reg-error';
	console.log(err_obj);

	var error_field_ids = Object.keys(err_obj);
	console.log(error_field_ids);

	for (i = 0; i < error_field_ids.length; i++) { 
		var field = $("."+error_field_ids[i]+error_field_class);
	    field.text(err_obj[error_field_ids[i]]);
	    field.show("slow"); 
	}

}
