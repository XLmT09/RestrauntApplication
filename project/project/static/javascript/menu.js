var itemsOrdered;
var itemIds;
var itemWithId;

function initialiseLists() {
  var itemList = getCookie("items").split(",");
  var idList = getCookie("itemIds").split(",");
  var ItemIdList = getCookie("itemWithIds").split(",");

  if (itemList == ""){itemsOrdered = [];}
  else {itemsOrdered = itemList;}

  if (idList == ""){itemIds = [];}
  else {itemIds = idList;}

  if (ItemIdList == ""){itemWithId = [];}
  else {itemWithId = ItemIdList;}

}

function addItem(id, addSubtract, price, name, itemId) {
  var element = document.getElementById(id);
  var text = element.textContent;
  var numberOfItems = parseInt(text);

  var basket = document.getElementById("basket");
  var priceText = parseFloat(basket.textContent);

  var newPrice = parseFloat(price);

  var numberOfItems = parseInt(text);

  if (numberOfItems > 0 && addSubtract < 0) {
    numberOfItems = numberOfItems - 1;
    element.innerHTML = numberOfItems;
    basket.innerHTML = (parseFloat(priceText) - parseFloat(newPrice)).toFixed(2);
    itemsOrdered.splice(itemsOrdered.indexOf(name), 2);
    itemIds.splice(itemIds.indexOf(itemId), 1);
    itemWithId.splice(itemWithId.indexOf(name), 2);
  } else if (addSubtract > 0) {
    numberOfItems = numberOfItems + 1;
    element.innerHTML = numberOfItems;
    basket.innerHTML = (parseFloat(priceText) + parseFloat(newPrice)).toFixed(2);
    itemsOrdered.push([name, price]);
    itemIds.push(itemId);
    itemWithId.push([name,itemId]);
  }
}

function deleteCookies() {
  document.cookie = "items" + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;"
  document.cookie = "itemIds" + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;"
  document.cookie = "itemWithIds" + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;"
  itemsOrdered = [];
  itemIds = [];
  itemWithId = [];
}

function setCookie(cname, cvalue, exdays) {
  let expires = "expires=";
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkout() {
  if (itemsOrdered.length == 0){
    alert("You're basket is currently empty. Try adding items to your basket");
  }
  setCookie("items", itemsOrdered, 3000);
  setCookie("itemIds", itemIds, 3000);
  setCookie("itemWithIds", itemWithId, 3000);
}

function alterChecout(itemPrice, itemQuantity, itemName, operation) {
  var items = getCookie("items").split(",");
  var Ids = getCookie("itemIds").split(",");
  var itemWithIds = getCookie("itemWithIds").split(",");

  var itemId = itemWithIds.at(itemWithIds.indexOf(itemName) + 1);

  var curValues = getCurrentValues(itemName, itemPrice);

  var priceStr = items[items.indexOf(itemName) + 1]
  var priceOfItem =  parseFloat(priceStr);

  var newValues = updateValues(curValues, priceOfItem, operation);

  if (newValues[0] > 0 && operation < 0) {
    updateHtml(items, Ids, itemName, itemPrice, newValues);
    items.splice(items.indexOf(itemName), 2);
    Ids.splice(Ids.indexOf(itemId), 1);
    itemWithIds.splice(itemWithIds.indexOf(itemName), 2);
  } else if (operation > 0) {
    updateHtml(items, Ids, itemName, itemPrice, newValues);
    Ids.push(itemId);
    items.push([itemName, priceStr]);
    itemWithIds.push([itemName,itemId]);
  }
  updateCookies(items, Ids, itemWithIds);
}

function updateHtml(items, Ids, itemName, itemPrice, newValues){
  // newValues = [newItemQuantity, newItemPrice, newTotalQuantity, newTotalPrice]
  document.getElementById(itemName).textContent = newValues[0];
  document.getElementById(itemName + itemPrice).textContent = "£" + newValues[1].toFixed(2);
  document.getElementById("TotalQuantity").textContent = newValues[2];
  document.getElementById("TotalPrice").textContent = "£" + newValues[3].toFixed(2);
}

function updateCookies(items, Ids, itemWithIds){
  setCookie("items", items, 3000);
  setCookie("itemIds", Ids, 3000);
  setCookie("itemWithIds", itemWithIds, 3000);
}

function getCurrentValues(itemName, itemPrice){
  var curValues = [
    parseInt(document.getElementById(itemName).textContent),
    parseFloat(document.getElementById(itemName + itemPrice).textContent.substring(1)),
    parseInt(document.getElementById("TotalQuantity").textContent),
    parseFloat(document.getElementById("TotalPrice").textContent.substring(1))
  ];
  return curValues; // curValues = [curQuantity, curPrice, totalQuantity, totalPrice]
}

function updateValues(values, priceOfItem, operation) {
  values[0] += 1 * operation;
  values[1] += priceOfItem * operation;
  values[2] += 1 * operation;
  values[3] += priceOfItem * operation;
  return values; // newValues = [newItemQuantity, newItemPrice, newTotalQuantity, newTotalPrice]
}

function deleteItemFromBasket(itemName) {
  if (confirm("Are you sure you want to remove this item?")){
    var items = getCookie("items").split(",");
    var Ids = getCookie("itemIds").split(",");
    var itemWithIds = getCookie("itemWithIds").split(",");

    var index = items.indexOf(itemName);
    while (index != -1){
      items.splice(index, 2);
      itemWithIds.splice(index, 2);
      Ids.splice(Math.floor(index/2), 1);
      index = items.indexOf(itemName);
    }

    updateCookies(items, Ids, itemWithIds);
    alert(itemName + " has been removed from your basket");
    if (items.length == 0){
      alert("You're basket is empty. Redirecting you to the menu");
    }
  }
}

function setBasketValue(){
  var basket = document.getElementById("basket");
  basket.innerHTML = (parseFloat("2.5")).toFixed(2);
}

function saveBasket() {
  setCookie("items", itemsOrdered, 3000);
  setCookie("itemIds", itemIds, 3000);
  setCookie("itemWithIds", itemWithId, 3000);
}
