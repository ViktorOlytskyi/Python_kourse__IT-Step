const books = document.querySelectorAll('.books ul li');

books.forEach((item, index) => {
    item.addEventListener('click', e => {
        function removeBg() {
            books.forEach(item => {
                item.classList.remove('orange');
            });
        }

        function selectShift(index2 = 0, index1) {
            if (index1 < index2) {
                let temp = 0;
                temp = index1;
                index1 = index2;
                index2 = temp;
            }

            for (let i = index2; i <= index1; i++) {
                books[i].classList.add('orange');
            }
        }



        if (e.ctrlKey) {
            if (item.classList.contains('orange')) {
                item.classList.remove('orange');
            } else {
                item.classList.add('orange');
            }
        } else if (e.shiftKey) {
            let index2 = 0;
            books.forEach((item, indexI) => {
                if (item.classList.contains('orange')) {
                    index2 = indexI
                }
            });
            selectShift(index2, index);
            window.getSelection().removeAllRanges();
        } else {
            removeBg();
            item.classList.add('orange');
        }
    });
})

