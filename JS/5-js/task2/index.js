// Задание 2
// Создать html-страницу с кнопкой Открыть и модальным
// окном. На модальном окне должен быть текст и кнопка Закрыть.
// Изначально модальное окно не отображается. При клике на
// кнопку Открыть появляется модальное окно, на кнопку Закрыть –
// исчезает.

function modalWindow(){
    let div = document.querySelector('#modal');
    
    let openBtn = document.createElement('button');
    let window = document.createElement('div');
    let closeBtn = document.createElement('button');
    
    openBtn.innerHTML = 'Open modal';
    window.innerHTML = 'Hello from modal window!';
    window.style.width='200px';
    window.style.height='100px';
    window.style.background='#c4e0ff';
    closeBtn.innerHTML = 'Close';
    window.style.display = 'none';
    
    div.append(openBtn);
    div.append(window);
    window.append(closeBtn);
    
    
    openBtn.onclick = () => window.style.display = 'block';
    closeBtn.onclick = ()=> window.style.display = 'none';
    
  };
  
  modalWindow();