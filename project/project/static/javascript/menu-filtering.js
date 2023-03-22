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

    if (optionValue == "none") {
        document.getElementById("sort").disabled = false;
    }
    else {
        document.getElementById("sort").disabled = true;
    }
}