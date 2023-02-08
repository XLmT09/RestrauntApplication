function sort(selectedOption) {
    optionValue = selectedOption.value;

    switch (optionValue) {
        case 'ltoh':
            if (! ('' + window.location).includes("low-to")) {
                window.location.href = 'http://127.0.0.1:8000/menu/sort-low-to-high'
            }
    }
}