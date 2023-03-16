var menuChoices = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < menuChoices.length; i++) {
    menuChoices[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}