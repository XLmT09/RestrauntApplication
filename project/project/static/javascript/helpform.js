function openHelpForm(){
    document.getElementById("myHelpForm").style.display = "block";
}


function closeHelpForm(){
    m = document.getElementById("messageEntry").innerText;
    alert("you have entered:", m)
    document.getElementById("myHelpForm").style.display = "none";
}

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + exdays * 3 * 1000);
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
