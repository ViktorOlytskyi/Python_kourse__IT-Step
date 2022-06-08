const insideList = document.querySelectorAll('.inside_list');
const openList = document.querySelectorAll('.open_list');

openList.forEach((item, index) => {
    item.addEventListener('click', e => {
        if (e.target.nodeName === 'LI') {
            if (window.getComputedStyle(insideList[index]).display === 'none') {
                insideList[index].style.display = 'block';
            } else {
                insideList[index].style.display = 'none';
            }
        }
    });
});
