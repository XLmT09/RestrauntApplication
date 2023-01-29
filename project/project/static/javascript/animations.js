let about = document.getElementById("about");

let bound = about.getBoundingClientRect();

let menu = document.getElementById("Menu");
console.log(menu);
let bound1 = menu.getBoundingClientRect();

window.addEventListener("scroll", () => {
  if (window.scrollY > bound.top) {
    let element = document.getElementById("aboutText");
    element.style.opacity = "1";
    let image = document.getElementById("aboutImage");
    image.style.backgroundPosition = "center";
    image.style.opacity = "1";
  }
  if (window.scrollY < bound1.top) {
    let element2 = document.getElementById("menuText");
    element2.style.opacity = "1";
    let image = document.getElementById("menuImage");
    image.style.backgroundPosition = "center";
    image.style.opacity = "1";
  }
});

function scrollToAboutUs() {
  document.getElementById("about").scrollIntoView();
  let element = document.getElementById("aboutText");
  element.style.opacity = "1";
  let image = document.getElementById("aboutImage");
  image.style.backgroundPosition = "center";
  image.style.opacity = "1";
}

function scrollToMenu() {
  document.getElementById("Menu").scrollIntoView();
  let element2 = document.getElementById("menuText");
  element2.style.opacity = "1";
  let image = document.getElementById("menuImage");
  image.style.backgroundPosition = "center";
  image.style.opacity = "1";
}
