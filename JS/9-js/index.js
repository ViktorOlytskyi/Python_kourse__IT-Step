
btn.addEventListener('click', () => {
    if (login.value && password.value) {
        if (check.checked) {
            alert(`Hello ${form.login.value}! I remember you.`)
        } else {
            alert(`Hello ${form.login.value}! I do not remember you.`)
        }
    }
    alert("Enter values");
})