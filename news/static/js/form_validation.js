function validateForm() {
    let title = document.forms.postForm.title.value;
    let content = document.forms.postForm.content.value;
    if (title === "" || content === "") {
        alert("Both title and content must be filled out");
        return false;
    }
    return true;
}
