const usernameField = document.querySelector('#usernameField');
const emailField = document.querySelector('#emailField');
const usernameFeedbackField = document.querySelector('.username-invalid-feedback');
const emailFeedbackField = document.querySelector('.email-invalid-feedback');
const passwordField = document.querySelector('#passwordField');
const togglePassword = document.querySelector('#togglePassword');
const submitButton = document.querySelector('.submit-btn')

function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            func.apply(null, args);
        }, delay);
    };
}

const validateUsername = debounce((usernameValue) => {
    fetch("/authentication/validate-username", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: usernameValue })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        if (data.username_error) {
            usernameField.classList.add("is-invalid");
            usernameFeedbackField.innerHTML = `<p>${data.username_error}</p>`;
            usernameFeedbackField.style.display = 'block';
            submitButton.disabled = true;


        } else {
            usernameField.classList.remove("is-invalid");
            usernameFeedbackField.style.display = 'none';
            submitButton.disabled = false;

        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}, 500);

const validateEmail = debounce((emailValue) => {
    fetch("/authentication/validate-email", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: emailValue })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        if (data.email_error) {
            emailField.classList.add("is-invalid");
            emailFeedbackField.innerHTML = `<p>${data.email_error}</p>`;
            emailFeedbackField.style.display = 'block';
            submitButton.disabled = true;


        } else {
            emailField.classList.remove("is-invalid");
            emailFeedbackField.style.display = 'none';
            submitButton.disabled = false;

        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}, 500);

usernameField.addEventListener("keyup", (e) => {
    const usernameValue = e.target.value;
    if (usernameValue.length > 0) {
        validateUsername(usernameValue);
    } else {
        usernameFeedbackField.style.display = 'none';
    }
});

emailField.addEventListener("keyup", (e) => {
    const emailValue = e.target.value;
    if (emailValue.length > 0) {
        validateEmail(emailValue);
    } else {
        emailFeedbackField.style.display = 'none';
    }
});


togglePassword.addEventListener('click', function () {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    this.textContent = type === 'password' ? 'Show' : 'Hide';
});