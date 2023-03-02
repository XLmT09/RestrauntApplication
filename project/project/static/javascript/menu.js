var itemsOrdered = [];
var itemIds = [];
var itemWithId = [];

function addItem(id, addSubtract, price, name, itemId) {
  console.log(itemId);
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
    var index = itemsOrdered.indexOf([name, price]);
    var idIndex = itemIds.indexOf(id);
    itemsOrdered.splice(index, 1);
    itemIds.splice(idIndex, 1);
    itemWithId.splice(itemIds.indexOf(name), 2);
  } else if (addSubtract > 0) {
    numberOfItems = numberOfItems + 1;
    element.innerHTML = numberOfItems;
    basket.innerHTML = (parseFloat(priceText) + parseFloat(newPrice)).toFixed(2);
    itemsOrdered.push([name, price]);
    itemIds.push(itemId);
    itemWithId.push(name);
    itemWithId.push(itemId);
  }
}

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + exdays * 3 * 1000);
  let expires = "expires=" + d.toUTCString();
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
  setCookie("items", itemsOrdered, 3000);
  setCookie("itemIds", itemIds, 3000);
  setCookie("itemWithIds", itemWithId, 3000);
}

function alterChecout(itemPrice, itemQuantity, itemName, operation) {
  var items = getCookie("items").split(",");
  var Ids = getCookie("itemIds").split(",");
  var itemWidthIds = getCookie("itemWithIds").split(",");

  var itemId = itemWidthIds.at(itemWidthIds.indexOf(itemName) + 1);

  var individualPrice = parseFloat(items[items.indexOf(itemName) + 1]);

  var itemTotal = parseFloat(
    document.getElementById(itemName + itemPrice).textContent.substring(1)
  );

  var quantity = parseInt(document.getElementById(itemName).textContent);

  var totalPrice = parseFloat(
    document.getElementById("TotalPrice").textContent.substring(1)
  );
  var totalQuantity = parseInt(
    document.getElementById("TotalQuantity").textContent
  );

  if (quantity > 1 && operation < 0) {
    document.getElementById(itemName).textContent = quantity - 1;
    var newPrice = itemTotal - individualPrice;
    var newTotal = totalPrice - individualPrice;
    document.getElementById(itemName + itemPrice).textContent = "£" + newPrice.toFixed(2);
    document.getElementById("TotalPrice").textContent = "£" + newTotal.toFixed(2);
    document.getElementById("TotalQuantity").textContent = totalQuantity - 1;
    items.splice(items.at(items.indexOf(itemName)), 2);
    Ids.splice(Ids.indexOf(itemId), 1);
    setCookie("items", items, 3000);
    setCookie("itemIds", Ids, 3000);
  } else if (operation > 0) {
    console.log(items.indexOf(itemName));
    document.getElementById(itemName).textContent = quantity + 1;
    var newPrice = itemTotal + individualPrice;
    var newTotal = totalPrice + individualPrice;
    document.getElementById(itemName + itemPrice).textContent = "£" + newPrice.toFixed(2);
    document.getElementById("TotalPrice").textContent = "£" + newTotal.toFixed(2);
    document.getElementById("TotalQuantity").textContent = totalQuantity + 1;
    Ids.push(itemId);
    items.push(itemName);
    items.push(individualPrice);
    setCookie("items", items, 3000);
    setCookie("itemIds", Ids, 3000);
  }
}
