function filter(selectedOption) {
    optionValue = selectedOption.value;

    for (showContainer of document.getElementsByClassName("course")) {
        showContainer.style.display = "block";
    }

    if (optionValue != "none") {
        for (hideContainer of document.getElementsByClassName("course")) {
            if (hideContainer.id != optionValue) {
                hideContainer.style.display = "none";
            }
        }
    }
}