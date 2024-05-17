window.onload = function() {
    var url = new URL(window.location.href);
    var params = new URLSearchParams(url.search);

    for (var key of params.keys()) {
        if (params.get(key) === "") {
            params.delete(key);
        }
    }

    window.history.replaceState({}, '', `${url.pathname}?${params}`);
}