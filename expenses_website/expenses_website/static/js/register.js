const usernameField = document.querySelector('#usernameField');
const feedbackField = document.querySelector('.invalid-feedback');

usernameField.addEventListener("keyup", (e) => {
    const usernameValue = e.target.value;

    if (usernameValue.length > 0) {
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
                feedbackField.innerHTML = `<p>${data.username_error}</p>`;
                feedbackField.style.display = 'block';
            } else {
                usernameField.classList.remove("is-invalid");
                feedbackField.style.display = 'none';
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
});
