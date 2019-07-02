// init
const url = '/post';
$( document ).ready(function() {
    $("#home-navlink").addClass("active");
    if ( msg_type == "spam" ) {
        $("#msg-btn").removeClass("btn-light").removeClass("btn-success")
                .addClass("btn-danger").attr("value", "Spam");
    } else if ( msg_type == "ham" ) {
        $("#msg-btn").removeClass("btn-light").removeClass("btn-danger")
            .addClass("btn-success").attr("value", "No-Spam");
    }
});