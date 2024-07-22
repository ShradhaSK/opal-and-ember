// Close messages after 3 seconds
$(document).ready(function () {
    setTimeout(function () {
        let messages = document.getElementById("message-container");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
});

$(document.getElementById('copyright')).text(new Date().getFullYear());