alert("Welcome to NRIIT Learning Management System")
let heading = document.getElementById("welcome");
heading.innerHTML = "Welcome Future software engineers"
console.log("Heading element: ", heading)
let msg = document.getElementById("message")
msg.innerHTML = "Javascript is fun"
console.Log("Message element:", msg)
function showmessage() {
    alert("Welcome to NRIIT Learning Management System")
}
function changeHeading() {
    document.getElementById("Welcome").innerHTML = "Welcome Python Fullstack Developers"
}
let heading1=document.querySelection("#welcome");
console.log("Heading element:",heading1)
let button = document.getElementById("btnGreeting");
button.addEventListener("click", function() {
    alert("Welcome to javascript Event Handling");
});
let registerForm = document.getElementById("registerForm");
function (event) {
    event.preventDefault(); // prevent form submision
    let name = document.getElementById("name").Value;
    let email = document.getElementById("email").Value;
    let password = document.getElementById("password").Value;
    if (!name || !email || !password){
        alert("please fill in all iels.:");
        return; 
    }
    alert("Registration succesfull");
    //perform