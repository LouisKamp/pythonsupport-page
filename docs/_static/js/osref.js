// Wait for the full HTML document to be completely loaded and parsed
document.addEventListener("DOMContentLoaded", () => {
    // Although deprecated, navigator.platform is still supported in most major browsers
    // Reference: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/platform#browser_compatibility
    let platform = navigator.platform.toLowerCase(); // Get the user's platform (OS) in lowercase
    
    // Initialize found os 
    let osClassName = "os-not-included";
    
    // Determine the OS-specific class name based on the platform string
    if (platform.includes("win")) {
        osClassName = "os-windows"; // Windows OS detected
    } else if (platform.includes("mac")) {
        osClassName = "os-macos"; // macOS detected
    } else if (platform.includes("linux")) {
        osClassName = "os-linux"; // Linux OS detected
    }

    // Get all elements that have a class matching the OS-specific class
    let el1 = document.getElementsByClassName(osClassName);
    // Get all elements with class "osref-show" (intended to be toggled off)
    let el2 = document.getElementsByClassName("osref-show");

    // Hide all elements that were previously visible to everyone
    for (let i = 0; i < el2.length; i++) {
        el2[i].classList.toggle('osref-hide'); // Add the 'osref-hide' class
        el2[i].classList.toggle("osref-show"); // Remove the 'osref-show' class
    }

    // Show only the elements related to the detected OS
    for (let i = 0; i < el1.length; i++) {
        el1[i].classList.toggle('osref-hide'); // Remove 'osref-hide' if present
        el1[i].classList.toggle("osref-show"); // Add 'osref-show' class
    }
});