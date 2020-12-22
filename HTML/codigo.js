"use strict";

// Welcome button
const button = document.querySelector(".welcome");

button.onclick = function () {
  let name = prompt("What is your name?");
  alert(
    "Hello " +
      name +
      ", nice to see you here!, you're one step closer to your dreams bike :D"
  );
};

// change theme
const select = document.querySelector("select");
const html = document.querySelector("html");
document.body.style.padding = "10px";

function update(bgColor, textColor) {
  html.style.backgroundColor = bgColor;
  html.style.color = textColor;
}

select.onchange = function () {
  select.value === "black"
    ? update("black", "white")
    : update("white", "black");
};
