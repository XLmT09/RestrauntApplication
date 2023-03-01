function LuhnsAlgorithm() {
  var cardNumber = document.getElementById("cardNumber").value;

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
  console.log((evenPosition + oddPosition) % 10 == 0);
  console.log(cardNumber.length >= 16 && cardNumber.length <= 19);
  if (
    !(
      (evenPosition + oddPosition) % 10 == 0 &&
      cardNumber.length >= 16 &&
      cardNumber.length <= 19
    )
  ) {
    document.getElementById("numberError").textContent = "Invalid card number";
    return false;
  } else {
    document.getElementById("numberError").textContent = "";
    return true;
  }
}

function checkName() {
  var name = document.getElementById("name").value;

  if (name == "" || /^[A-Za-z]*$/.test(name) == false) {
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
  var validCardNumber = LuhnsAlgorithm();
  var ValidName = checkName();
  var ValidsecurityCode = checkSecurity();

  if (validCardNumber && ValidName && ValidsecurityCode) {
    window.location.href = "/completePayment/";
  }
}
