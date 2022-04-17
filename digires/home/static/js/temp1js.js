function copyToClipboard(text) {
    var inputc = document.body.appendChild(document.createElement("input"));
    inputc.value = window.location.href;
    inputc.parentNode.removeChild(inputc);
    alert("URL Copied.");
    }
