function search(searchText) {
    var searchValue = searchText.value;
    searchValue = searchValue.toLowerCase();

    var itemContainers = document.getElementsByClassName("container");

    for (var itemContainer of itemContainers) {
        if (itemContainer.match(/(?:^|\s)highlight(?!\S)/)) {
            itemContainer.classList.remove("highlight");
        }

        itemHeader = itemContainer.getElementsByClassName("header")[0];
        itemName = itemHeader.getElementsByClassName("name")[0];
        itemNameValue = itemName.innerHTML.toLowerCase();
        
        if (itemNameValue == searchValue) {
            itemContainer.classList.toggle("highlight");

            break;
        }
    }
}