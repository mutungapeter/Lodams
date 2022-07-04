var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("btn");
var header = document.getElementById("header").innerHTML = "HEALTH CARE ERP SIGNUP/LOGIN";
function register(){
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "110px";
}
const login = () => {
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0";
}
