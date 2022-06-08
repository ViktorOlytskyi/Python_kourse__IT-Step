const editWrapper = document.querySelector('.edit-wrapper');

addEventListener('keydown', e => {
    const content = document.querySelector('.edit');
    const textArea = document.querySelector('#edit-content');
    let data = '';

    if(e.ctrlKey === true && e.code === 'KeyE'){
        data = content.innerHTML.split(' ').filter(word => {
            if(word !== false){
                return word.replace(/\n/ig, '');
            }
        });

        console.log(data);
        content.classList.add('content-hide');
        content.classList.remove('content-show');

        textArea.classList.add('content-show');
        textArea.classList.remove('content-hide');
        textArea.value = data.join(' ');
    
        e.preventDefault();
    }

    if(e.ctrlKey === true && e.code === 'KeyS'){
        data = textArea.value;
        content.innerHTML = data;

        content.classList.add('content-show');
        content.classList.remove('content-hide');

        textArea.classList.add('content-hide');
        textArea.classList.remove('content-show');

        e.preventDefault();
    }
});