function search(searchText) {
    var searchValue = searchText.value;
    searchValue = searchValue.toLowerCase();

    var itemContainers = document.getElementsByClassName("container");
    var mainBox = document.getElementsByClassName("dishbox2")[0];

    mainBox.style.visibility = "visible";

    for (var showContainer of itemContainers) {
        showContainer.style.visibility = "visible";
    }

    for (var itemContainer of itemContainers) {
        itemHeader = itemContainer.getElementsByClassName("header")[0];
        itemName = itemHeader.getElementsByClassName("name")[0];
        itemNameValue = itemName.innerHTML.toLowerCase();
        
        if (itemNameValue == searchValue) {
            for (var hideContainer of itemContainers) {
                hideContainer.style.visibility = "hidden";
            }
            
            mainBox.style.visibility = "hidden";
            itemContainer.style.visibility = "visible";
            
            previousItemContainer = itemContainer;
        }
    }
}