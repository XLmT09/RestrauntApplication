function search(searchText) {
    var searchValue = searchText.value;
    searchValue = searchValue.toLowerCase();

    var itemContainers = document.getElementsByClassName("container");
    var resultContainer = document.getElementById("resultcontainer");
    var resultName = document.getElementById("resultname");
    var resultPrice = document.getElementById("resultprice");
    var resultDetails = document.getElementById("resultdetails");

    for (var itemContainer of itemContainers) {
        itemHeader = itemContainer.getElementsByClassName("header")[0];
        itemName = itemHeader.getElementsByClassName("name")[0];
        itemNameValue = itemName.innerHTML.toLowerCase();
        
        if (itemNameValue == searchValue) {
            itemPrice = itemHeader.getElementsByClassName("price")[0];
            itemPriceValue = itemPrice.innerHTML;
            itemDetails = itemContainer.getElementsByClassName("details")[0];
            itemDetailsValue = itemDetails.innerHTML;

            resultName.innerHTML = itemName.innerHTML;
            resultPrice.innerHTML = itemPriceValue;
            resultDetails.innerHTML = itemDetailsValue;
        }
    }
}