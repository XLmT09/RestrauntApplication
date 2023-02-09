function sort(selectedOption) {
    optionValue = selectedOption.value;

    switch (optionValue) {
        case 'dlt':
            window.location.href = 'http://127.0.0.1:8000/menu'

            break;
        case 'ltoh':
            window.location.href = 'http://127.0.0.1:8000/menu/sort-low-to-high'

            break;
        case 'htol':
            window.location.href = 'http://127.0.0.1:8000/menu/sort-high-to-low'

            break;
    }
}