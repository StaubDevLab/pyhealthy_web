
//Ajax function to login, signup and logout

/*
This function allows via ajax to connect the user by querying the view provided for this purpose.
*/
var csrftoken = $("[name=csrfmiddlewaretoken]").val();
function login(){


    $.ajax({
        url:'/users/ajax_login',
        type: 'POST',
        headers:{
        "X-CSRFToken": csrftoken
    },
        data:$("#formLogin").serialize(),
        success:(data)=>{
            $('#connexionModal').modal('toggle');
            location.reload(true);

        },
        error :(e) =>{
            if (!$('#id_username').hasClass('is-invalid') && !$('#id_password').hasClass('is-invalid')){
                $('#id_username').addClass('is-invalid');
                $('#id_password').addClass('is-invalid');
                $('#id_password').after('<div class="invalid-feedback">Adresse e-mail ou mot de passe non valide, veuillez réessayer.</div>');
            }

    }


    });

};

//This function allows to disconnect the user with a simple server side view.
var csrftoken = $("[name=csrfmiddlewaretoken]").val();
function logout(){

    $.ajax({
        url:'/users/ajax_logout',
        type: 'GET',
        headers:{
        "X-CSRFToken": csrftoken
    },
        data:{},
        success:(data)=>{
            location.reload(true)


        },
        error :() =>{
            console.log('Il y a une erreur')
    }


    });

};

/*

Complex function that uses ajax to send the data from the registration form to the server,
error messages are managed and displayed without refreshing the page.
 */
function signup(){

    $.ajax({
        url:'/users/signup',
        type: 'POST',
        headers:{
        "X-CSRFToken": csrftoken
    },
        data:$("#formSingUp").serialize(),
        success:(data)=>{
            location.reload(true)

        },
        error :(e) =>{
            if (e.responseJSON.formErrors.email){
                $('#id_email').addClass('is-invalid');
                $('#id_email').after('<div class="invalid-feedback">Adresse e-mail invalide ou déjà utilisée.</div>');
            }else if (e.responseJSON.formErrors.__all__){
                $('#id_confirm_password').addClass('is-invalid');
                $('#group-confirm-password').after('<div class="invalid-feedback">Le mot de passe et la confirmation ne correspondent pas</div>');
            }else if (e.responseJSON.formErrors.password){
                $('#id_password_signup').addClass('is-invalid');
                $('#group-password').after('<div class="invalid-feedback">'+e.responseJSON.formErrors.password+'</div>');
            }
    }


    });

};


//Selection of DOM elements to assign events to them
var password = document.getElementById("id_password_signup");
var confirmPassword = document.querySelector('#id_confirm_password');
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var message = document.getElementById("message");
var visiblePassword = document.getElementById("basic-addon2");
var visibleConfirmPassword = document.getElementById("basic-addon3");
var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{9,20}$/;

//These two functions allow you to show or hide the password hints.
function visibleMessage(){
  message.style.display ="block";
};
function hiddenMessage(){
  message.style.display ="none";
};


/*his function tests whether all the elements required for the password are present.
If they are elements are added to the DOM.*/
function testPassword(){
    var lowerCaseLetters = /[a-z]/g;
  if(password.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalidPass");
    letter.classList.add("validPass");
  } else {
    letter.classList.remove("validPass");
    letter.classList.add("invalidPass");
  }

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(password.value.match(upperCaseLetters)) {
    capital.classList.remove("invalidPass");
    capital.classList.add("validPass");
  } else {
    capital.classList.remove("validPass");
    capital.classList.add("invalidPass");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(password.value.match(numbers)) {
    number.classList.remove("invalidPass");
    number.classList.add("validPass");
  } else {
    number.classList.remove("validPass");
    number.classList.add("invalidPass");
  }

  // Validate length
  if(password.value.length >= 9) {
    length.classList.remove("invalidPass");
    length.classList.add("validPass");
  } else {
    length.classList.remove("validPass");
    length.classList.add("invalidPass");
  }
};

/*This function checks if the password matches the regex pattern.
If it matches elements are added to the DOM to indicate it.

 */
function checkPassword(){
    if (password.value.match(pass)){
        password.style.borderColor = '#75B782';

    }else{
        password.style.borderColor = '#D86055';

    }
}

//This function verifies that the password matches the confirmation and displays it on the DOM.
function checkConfirmPassword(){
    if (password.value === confirmPassword.value){
        confirmPassword.style.borderColor = '#75B782';

    }else{
        confirmPassword.style.borderColor = '#D86055';

    }
}

//This function allows you to interact with the button after the password. It allows you to show or hide the password.
visiblePassword.addEventListener('click',()=>{
    if (password.type === 'password'){
        password.type = 'text';
        visiblePassword.innerHTML ='<i class="fas fa-eye-slash"></i>';
    }else{
        password.type = 'password';
        visiblePassword.innerHTML ='<i class="fas fa-eye"></i>';
    };

});
/*This function allows you to interact with the button after the confirm password.
It allows you to show or hide the confirm password.
 */
visibleConfirmPassword.addEventListener('click',()=> {
    if (confirmPassword.type === 'password'){
        confirmPassword.type = 'text';
        visibleConfirmPassword.innerHTML ='<i class="fas fa-eye-slash"></i>';
    }else{
        confirmPassword.type = 'password';
        visibleConfirmPassword.innerHTML ='<i class="fas fa-eye"></i>';
    }
});

//Attachment of functions to elements of the DOM.
password.addEventListener('keyup',testPassword);
password.addEventListener('keydown',checkPassword);
password.addEventListener('keyup',checkConfirmPassword);
confirmPassword.addEventListener('keyup',checkConfirmPassword);
password.addEventListener('focusin',visibleMessage);
document.querySelector('#id_email').addEventListener('focusin',hiddenMessage)
confirmPassword.addEventListener('focusin',visibleMessage);


//Attachment of functions to elements of the DOM.
$('body').on('click', '#logout', function (){

        logout();
    });

$('#formLogin').on('submit', function(event){
event.preventDefault();
login();
});
$('#formSingUp').on('submit', function(event){
event.preventDefault();
signup();
$(':input').removeClass('is-invalid');
$('.invalid-feedback').remove();
});
$('#id_email').on('keydown',()=>{
    $('#id_email').removeClass('is-invalid');
    $('.invalid-feedback').remove();
})
$('#id_password_signup').on('keydown',()=>{
    $('#id_password_signup').removeClass('is-invalid');
    $('#id_confirm_password').removeClass('is-invalid');
    $('.invalid-feedback').remove();
})
$('#id_confirm_password').on('keydown',()=>{
    $('#id_confirm_password').removeClass('is-invalid');
    $('#id_password_signup').removeClass('is-invalid');
    $('.invalid-feedback').remove();
})

$('#id_username').on('keydown', ()=>{
    $('#id_username').removeClass('is-invalid');
    $('.invalid-feedback').remove();

})
$('#id_password').on('keydown', ()=>{
    $('#id_password').removeClass('is-invalid');
    $('.invalid-feedback').remove();

})


$("#alert").delay(2000).hide();