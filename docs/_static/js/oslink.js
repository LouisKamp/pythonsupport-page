document.addEventListener("DOMContentLoaded", () => {
    let platform = navigator.platform.toLowerCase();
    if (platform.includes("win")) {
        osClassName = "os-windows"
    } else if (platform.includes("mac")) {
        osClassName = "os-macos"
    } else {
        osClassName = "os-linux"
    }

    let el1 = document.getElementsByClassName(osClassName)
    let el2 = document.getElementsByClassName("oslink-show")

    for (let i = 0; i < el2.length; i++) {
        el2[i].classList.toggle('oslink-hide');
        el2[i].classList.toggle("oslink-show");
    }

    for (let i = 0; i < el1.length; i++) {
        el1[i].classList.toggle('oslink-hide');
        el1[i].classList.toggle("oslink-show");
    }

})