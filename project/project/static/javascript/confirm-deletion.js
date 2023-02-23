function confirmDeletion(order) {
    var deleteBtn = document.getElementById("deleteBtn" + order);
    var confirmation = document.getElementById("confirmation" + order);
    
    deleteBtn.style.display = "none";
    confirmation.style.display = "block";
}

function sayNo(order) {
    var deleteBtn = document.getElementById("deleteBtn" + order);
    var confirmation = document.getElementById("confirmation" + order);
    
    deleteBtn.style.display = "block";
    confirmation.style.display = "none";
}