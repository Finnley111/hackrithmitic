const switchButton = document.getElementById("switch");
const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const button3 = document.getElementById("button3");

switchButton.addEventListener("change", function() {
    if (switchButton.checked) {
        // Enable the buttons
        button1.disabled = false;
        button2.disabled = false;
        button3.disabled = false;
    } else {
        // Disable the buttons
        button1.disabled = true;
        button2.disabled = true;
        button3.disabled = true;
    }
});

button1.addEventListener("click", function() {
    console.log("Button 1 clicked");
});

button2.addEventListener("click", function() {
    console.log("Button 2 clicked");
});

button3.addEventListener("click", function() {
    console.log("Button 3 clicked");
});
 