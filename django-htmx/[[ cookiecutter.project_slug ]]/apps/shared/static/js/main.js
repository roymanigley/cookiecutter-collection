function showModal(selector) {
    document.querySelector(selector).showModal()
}

function hideModal(selector, delay = 0) {
    setTimeout(() => {
        document.querySelector(selector).close();
    }, delay)
}

function hideModalAndReload(selector, delay = 0) {
    setTimeout(() => {
        document.querySelector(selector).close();
        htmx.trigger('body', 'reload');
    }, delay)
}

document.addEventListener("DOMContentLoaded", function () {
    htmx.trigger('body', 'reload');
});

