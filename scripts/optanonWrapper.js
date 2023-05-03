function OptanonWrapper() {
    const t = window.OnetrustActiveGroups && window.OnetrustActiveGroups.includes("C0004");
    localStorage.setItem("GACookiesAccepted", t);
    const e = document.getElementById("one-trust-initial-load-btn");
    if (e && t) {
        e.click();
        e.parentElement.removeChild(e)
    }
}