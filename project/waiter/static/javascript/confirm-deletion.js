function confirmDeletion() {
    var deleteBtn = document.getElementById("deleteBtn");
    var confirmation = document.getElementById("confirmation");
    var yes = document.getElementById("yes");
    var no = document.getElementById("no");
    
    deleteBtn.style.display = "none";
    confirmation.style.display = "block";
    yes.style.display = "block";
    no.style.display = "block";
}