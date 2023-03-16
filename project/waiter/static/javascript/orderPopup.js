var menuChoices = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < menuChoices.length; i++) {
    menuChoices[i].addEventListener("click", function() {
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
    var j;
    for (j = 0; j < menuChoices.length; j++){
        if (menuChoices[j] != this) {
            var content = menuChoices[j].nextElementSibling;
            content.style.display = "none";
        }
    }
  });
}