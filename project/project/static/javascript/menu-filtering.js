function hide(selectedOption) {
    optionValue = selectedOption.value;

    for (var container of document.getElementsByClassName("course")) {
        if (container.id != optionValue) {
            container.style.display = "none";
        }
    }
}