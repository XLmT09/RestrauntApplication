var itemsOrdered = [];
function addItem(id, addSubtract, price, name) {
  var element = document.getElementById(id);
  var text = element.textContent;
  var numberOfItems = parseInt(text);

  var basket = document.getElementById("basket");
  var priceText = parseFloat(basket.textContent);
  console.log(typeof priceText);
  var newPrice = parseFloat(price);
  console.log(typeof newPrice);

  var numberOfItems = parseInt(text);

  if (numberOfItems > 0 && addSubtract < 0) {
    numberOfItems = numberOfItems - 1;
    element.innerHTML = numberOfItems;
    basket.innerHTML = parseFloat(priceText) - parseFloat(newPrice);
    var index = itemsOrdered.indexOf([name, price]);
    itemsOrdered.splice(index, 1);
  } else if (addSubtract > 0) {
    numberOfItems = numberOfItems + 1;
    element.innerHTML = numberOfItems;
    basket.innerHTML = parseFloat(priceText) + parseFloat(newPrice);
    itemsOrdered.push([name, price]);
  }

  console.log(itemsOrdered);
}

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + exdays * 3 * 1000);
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function checkout() {
  setCookie("test", itemsOrdered, 3000);
}
