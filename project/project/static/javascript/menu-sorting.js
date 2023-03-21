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

function setDropDown(optionValue){
    switch (optionValue) {
        case 'dlt':
            document.getElementById("sort").selectedIndex = 0;
            break;
        case 'ltoh':
            document.getElementById("sort").selectedIndex = 1;
            break;
        case 'htol':
            document.getElementById("sort").selectedIndex = 2;
            break;
    }
}