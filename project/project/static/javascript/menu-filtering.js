function filter(selectedOption) {
    optionValue = selectedOption.value;

    for (var container of document.getElementsByClassName("course")) {
        container.style.display = "block";
    }

    if (optionValue != "default") {
        for (var container of document.getElementsByClassName("course")) {
            if (container.id != optionValue) {
                container.style.display = "none";
            }
        }
    }
}