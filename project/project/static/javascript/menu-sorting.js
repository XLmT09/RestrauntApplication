function sort(selectedOption) {
    optionValue = selectedOption.value;

    var filterSelectedOption = document.querySelector('#filter');

    switch (optionValue) {
        case 'none':
            window.location.href = 'http://127.0.0.1:8000/menu'

            break;
        case 'ltoh':
            window.location.href = 'http://127.0.0.1:8000/menu/sort-low-to-high'

            break;
        case 'htol':
            window.location.href = 'http://127.0.0.1:8000/menu/sort-high-to-low'

            break;
    }

    windows.onload = function() {
        hide(filterSelectedOption);
    }
}