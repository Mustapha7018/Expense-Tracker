const inputField = document.getElementById('inputField');

        inputField.addEventListener('focus', () => {
            inputField.classList.add('active');
        });

        inputField.addEventListener('blur', () => {
            if (!inputField.value) {
                inputField.classList.remove('active');
            }
        });