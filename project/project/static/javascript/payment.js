function LuhnsAlgorithm(cardNumber) {
  // characters at even position
  var evenPosition = 0;
  // characters at odd position
  var oddPosition = 0;
  for (let i = 0; i < cardNumber.length; i++) {
    // checks if character is at even position
    if (i % 2 == 0) {
      // converts character into int and multiplies it by two
      var product = parseInt(cardNumber.charAt(i)) * 2;
      if (product > 9) {
        // finds modulus 10 of int
        // adds result to evenPosition
        evenPosition += 1 + (product % 10);
      } else {
        evenPosition += product;
      }
    } else {
      // adds result to oddPosition
      oddPosition += parseInt(cardNumber.charAt(i));
    }
  }
  // checks whether evnPosition and oddPosition added is a multiple of 10
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

function checkName(name) {
  if (name == "" || /^[A-Za-z]*$/.test(name) == false) {
    document.getElementById("nameError").textContent = "Inavlid name";
    return false;
  } else {
    document.getElementById("nameError").textContent = "";
    return true;
  }
}

function checkSecurity(security) {
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
  var cardNumber = document.getElementById("cardNumber").value;
  var validCardNumber = LuhnsAlgorithm(cardNumber);
  var name = document.getElementById("name").value;
  var ValidName = checkName(name);
  var security = document.getElementById("security").value;
  var ValidsecurityCode = checkSecurity(security);

  if (validCardNumber && ValidName && ValidsecurityCode) {
    window.location.href = "/completePayment/";
  }
}

function testCardNumbers() {
  // test invalid length (too little)
  if (LuhnsAlgorithm(222) == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid set of numbers valid length
  if (LuhnsAlgorithm(4003600000000013) == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid length (too many )
  if (LuhnsAlgorithm(4003600000000013555555555555) == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid set of numbers valid length
  if (LuhnsAlgorithm(4003600000000014) == true) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
}

function testSecurityCode() {
  // test valid security code
  if (checkSecurity(222) == true) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid length (too little)
  if (checkSecurity(22) == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid length (too little)
  if (checkSecurity(2222) == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
}

function testNames() {
  // test valid name
  if (checkName("Test") == true) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid name(contains numerics)
  if (checkName("Test1") == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid length (too little)
  if (checkName("t") == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
  // test invalid length (no name input)
  if (checkName("") == false) {
    console.log("Passed");
  } else {
    console.log("Failed");
  }
}
