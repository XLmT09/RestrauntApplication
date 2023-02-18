function search(searchText) {
    var searchValue = searchText.value;
    searchValue = searchValue.toLowerCase();

    var itemContainers = document.getElementsByClassName("container");

    for (var itemContainer of itemContainers) {
        itemHeader = itemContainer.getElementsByClassName("header")[0];
        itemName = itemHeader.getElementsByClassName("name")[0];
        itemNameValue = itemName.innerHTML.toLowerCase();
        
        if (itemNameValue == searchValue) {
            itemContainer.scrolIntoView();
            itemContainer.classList.add("highlight");
            document.documentElement.scrollTop -= searchResult.offsetHeight;
        }
        else {
            itemContainer.classList.remove("highlight");
        }
    }
}