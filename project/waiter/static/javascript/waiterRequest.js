//This function allows the waiter to select a help request and choose if they want to delete it from the webpage
function highlightRow(button) {
    var row = button.parentNode.parentNode;
    if (row.classList.contains("highlight")) {
        row.classList.remove("highlight");
    } else {
        row.classList.add("highlight");
    }
    if (row.classList.contains("highlight")) {
        var confirmed = confirm("Do you want to delete this row?");
        if (confirmed) {
            row.parentNode.removeChild(row);
            deleteHelpRequest();
        } else {
            row.classList.remove("highlight");
        }
    }
}