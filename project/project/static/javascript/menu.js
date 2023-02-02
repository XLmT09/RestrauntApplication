function addItem(id, addSubtract, price) {
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
  } else if (addSubtract > 0) {
    numberOfItems = numberOfItems + 1;
    element.innerHTML = numberOfItems;
    basket.innerHTML = parseFloat(priceText) + parseFloat(newPrice);
  }
}
