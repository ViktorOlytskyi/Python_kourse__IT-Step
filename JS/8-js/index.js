
document.oncopy = function() {
var bodyElement = document.body;
var selection = getSelection();
// console.log(selection);
var href = document.location.href;
// console.log(href);
var date = new Date();
let outputDate = String(date.getDate()).padStart(2, '0') + '/' + String(date.getMonth() + 1).padStart(2, '0') + '/' + date.getFullYear();
let outputTime = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();

var copyright = "<br><br>Information copied from site: "+ href+"<br><br>" + outputDate+" "+outputTime;
var text = selection + copyright;
var divElement = document.createElement('div');
divElement.style.position = 'absolute';
divElement.style.left = '-99999px';
divElement.innerHTML = text.toString().replace(/\n/g,'<br />');
bodyElement.appendChild(divElement);
selection.selectAllChildren(divElement);
setTimeout(function() {
bodyElement.removeChild(divElement);
}, 0);
};
