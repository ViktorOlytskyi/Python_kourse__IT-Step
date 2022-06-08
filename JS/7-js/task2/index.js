let imageBox = ["1.png", "2.png", "3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png",];
let listLen = imageBox.length - 1;
let i = 0;

container.addEventListener("click", function (e) {
  if (e.target.id == "rightButton") i++;
  if (e.target.id == "leftButton") i--;

  if (i == listLen) {
    rightButton.disabled = true;
    rightButton.style.display="none"
  } else {
    rightButton.disabled = false;
    rightButton.style.display="block";
    rightButton.style.float="right";
  }
  if (i == 0) {
    leftButton.disabled = true;
    leftButton.style.display="none"
  } else {
    leftButton.disabled = false;
    leftButton.style.display="block";
    leftButton.style.float="right";
  }
  imageSlider.src = imageBox[i];
});