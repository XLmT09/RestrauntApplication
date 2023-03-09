// Grab the relevent box the user wants to rotate by id
function rotate(boxid) {
    const orderBoxOuter = document.getElementById(boxid);
    console.log("hi");
    if (orderBoxOuter.classList.contains('rotate')) {
        // remove the class to deactivate the rotation
        orderBoxOuter.classList.remove('rotate');
      } else {
        // add the class to activate the rotation
        orderBoxOuter.classList.add('rotate');
      }
}