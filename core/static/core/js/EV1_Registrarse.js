$(document).ready(function () {
    
    //VALIDO QUE INGRESE ALGO EN EL INPUT
    $("#nombre").on("input", function () {
        if ($("#nombre").val() == "") {
            $("#nombre").addClass("error");
            $("#nombre").removeClass("ok");
            $("#mensaje_nom").html("Ese campo es obligatorio!.");
        } else {
            $("#nombre").removeClass("error");
            $("#nombre").addClass("ok");
            $("#mensaje_nom").html("");
        }
    });

    $("#apellido").on("input", function () {
        if ($("#apellido").val() == "") {
            $("#apellido").addClass("error");
            $("#apellido").removeClass("ok");
            $("#mensaje_ape").html("Ese campo es obligatorio!.");
        } else {
            $("#apellido").removeClass("error");
            $("#apellido").addClass("ok");
            $("#mensaje_ape").html("");
        }
    });

    $("#contraseña").on("input", function () {
        if($("#contraseña").val() == "") {
            $("#contraseña").addClass("error");
            $("#contraseña").removeClass("ok");
            $("#mensaje_con").html("Ese campo es obligatorio!.");
        } else {
            $("#contraseña").removeClass("error");
            $("#contraseña").addClass("ok");
            $("#mensaje_con").html("");
        }
    }); 

    $("#email").on("input", function () {
        if ($("#email").val() == "") {
            $("#email").addClass("error");
            $("#email").removeClass("ok");
            $("#mensaje_email").html("Este campo es obligatorio!.");
        } else {
            $("#email").removeClass("error");
            $("#email").addClass("ok");
            $("#mensaje_email").html("");
        }
    });


});