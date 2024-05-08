function updateUrlParams(form, url) {
    new FormData(form).forEach((value, key) => {
        if (value) { // Only add parameter if it has a value
            url.searchParams.append(key, value);
        }
    });

    form.querySelectorAll('select').forEach(select => {
        if (select.value) { // Only add parameter if it has a value
            url.searchParams.append(select.name, select.value);
        }
    });
}

document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        let url = new URL(this.action);
        document.querySelectorAll('form').forEach(form => {
            updateUrlParams(form, url);
        });
        console.log(url.toString());
        window.location.href = url.toString();
    });
});

function submitFormWithFilterParams(form) {
    event.preventDefault();
    let url = new URL(window.location.href);
    updateUrlParams(form, url);
    window.location.href = url.toString();
}