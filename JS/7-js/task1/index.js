let resize = false;
bar.addEventListener("mousedown", function (e) {
    if ((e.pageX >= 40) && (e.pageX <= 530)) { resize = true };
})
document.addEventListener("mouseup", function () { resize = false })
document.addEventListener("mousemove", function (e) {
    if ((e.pageX >= 40) && (e.pageX <= 480) && resize) {
        bar.style.left = (e.pageX - 10) + "px";
    }
    else if (e.pageX > 480) {
        bar.style.left = 480 + "px";
    } else if (e.pageX < 40) {
        bar.style.left = 40 + "px";
    }
})    

