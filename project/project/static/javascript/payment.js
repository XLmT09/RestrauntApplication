function LuhnsAlgorithm() {
  var cardNumber = document.getElementById("cardNumber").value;
  console.log(typeof cardNumber);
  var evenPosition = 0;
  var oddPosition = 0;
  for (let i = 0; i < cardNumber.length; i++) {
    if (i % 2 == 0) {
      var product = parseInt(cardNumber.charAt(i)) * 2;
      if (product > 9) {
        evenPosition += 1 + (product % 10);
      } else {
        product;
      }
    } else {
      oddPosition += parseInt(cardNumber.charAt(i));
    }
  }
  if (!((evenPosition + oddPosition) % 10 == 0)) {
    document.getElementById("numberError").textContent = "Invalid card number";
    return false;
  } else {
    document.getElementById("numberError").textContent = "";
    return true;
  }
}

function checkName() {
  var name = document.getElementById("name").value;
  console.log(name);

  if (name.length == 0) {
    document.getElementById("nameError").textContent = "Inavlid name";
    return false;
  } else {
    document.getElementById("nameError").textContent = "";
    return true;
  }
}

function checkSecurity() {
  var security = document.getElementById("security").value;
  if (security.length != 3) {
    document.getElementById("inavlidSecurity").textContent =
      "Inavlid security code";
    return false;
  } else {
    document.getElementById("inavlidSecurity").textContent = "";
    return true;
  }
}

function checkInputs() {
  if (LuhnsAlgorithm() && checkName() && checkSecurity()) {
    window.location.href = "/completePayment/";
  }
}
