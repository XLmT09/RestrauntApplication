function popup(name, price) {
  console.log("yes");
  document.getElementById("menuBox").style.zIndex = -1;
  document.getElementById("menuBox").style.opacity = 0.2;
  document.getElementById("orderBox").style.zIndex = 1;
  document.getElementById("orderBox").style.opacity = 1;
  document.getElementById("name").innerHTML = name;
  document.getElementById("price").innerHTML = price;
}

function exitpopup() {
  document.getElementById("menuBox").style.zIndex = 1;
  document.getElementById("menuBox").style.opacity = 1;
  document.getElementById("orderBox").style.zIndex = -1;
  document.getElementById("orderBox").style.opacity = 0;
}

function addItem(id, addSubtract) {
  var element = document.getElementById(id);
  var text = element.textContent;
  var numberOfItems = parseInt(text);
  console.log(numberOfItems);
  if (numberOfItems > 0 && addSubtract < 0) {
    numberOfItems = numberOfItems - 1;
    element.innerHTML = numberOfItems;
  } else if (addSubtract > 0) {
    console.log("yes");
    numberOfItems = numberOfItems + 1;
    element.innerHTML = numberOfItems;
  }
}
