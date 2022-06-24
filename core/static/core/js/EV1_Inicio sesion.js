$(document).ready(function () {
    
    //VALIDO QUE INGRESE ALGO EN EL INPUT

    $("#email").on("input", function () {
        if ($("#email").val() == "") {
            $("#email").addClass("error");
            $("#email").removeClass("ok");
            $("#mensaje_email").html("Por favor ingrese un email.");
        } else {
            $("#email").removeClass("error");
            $("#email").addClass("ok");
            $("#mensaje_email").html("");
        }
    });
    
    $("#contraseña").on("input", function () {
        if($("#contraseña").val() == "") {
            $("#contraseña").addClass("error");
            $("#contraseña").removeClass("ok");
            $("#mensaje_con").html("Por favor ingrese una contraseña.");
        } else {
            $("#contraseña").removeClass("error");
            $("#contraseña").addClass("ok");
            $("#mensaje_con").html("");
        }
    }); 

});