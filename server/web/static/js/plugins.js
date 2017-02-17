// place any jQuery/helper plugins in here, instead of separate, slower script files.
var SERVER_ADDRESS = "http://192.168.1.123:5000"

$(".alert").delay(1750).slideUp(400, function() {
    $(this).alert("close");
});

function monitorNotifications() {
    $.ajax({
        type: "POST",
        url: SERVER_ADDRESS + "/api/device/notifications",
        success: function(data) {
            if (data.success) {
                buildNotificationList(data.data);
            }
        }
    })
}

function buildNotificationList(notifications) {
    $("#notification-list").empty();
    $.each(notifications, function(i, notification) {
        if (notification.device_id)
            var url = "/device/" + notification.device_id;
        else
            var url = "";
        $("#notification-list").append(
            $("<a>").attr("href", url).addClass("list-group-item")
            .append($("<i>").addClass("fa").addClass("fa-comment").addClass("fa-fw"))
            .append(notification.message)
            .append($("<span>").addClass("pull-right").addClass("text-muted").addClass("small").append($("<em>").append(notification.timestamp)))
        );
    });
}
