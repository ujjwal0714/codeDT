document.addEventListener("DOMContentLoaded", function() {
    // Set "Email" option as default selected option
    document.getElementById("selectedOptionText").innerText = "Email";
});

// Function to toggle the dropdown menu
function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Function to select an option from the dropdown menu
function selectOption(option) {
    document.getElementById("myDropdown").classList.remove("show");
    document.getElementById("selectedOptionText").innerText = option;
}

// Function to copy the selected option's text to clipboard
function copyToClipboard() {
    var inputElement = document.getElementById("clipboardInput");
    var selectedOption = document.getElementById("selectedOptionText").innerText;
    switch (selectedOption) {
        case "Email":
            inputElement.value = "ujjwalomar0714@gmail.com";
            break;
        case "Phone Number":
            inputElement.value = "8858042468";
            break;
        case "Application Number":
            inputElement.value = "220105063";
            break;
        default:
            inputElement.value = "";
            break;
    }
    inputElement.select();
    inputElement.setSelectionRange(0, 99999);
    document.execCommand("copy");
    
}

// Function to get the current time in 12-hour format
function getCurrentTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    hours = hours % 12;
    hours = hours ? hours : 12;
    hours = formatTime(hours);
    minutes = formatTime(minutes);
    seconds = formatTime(seconds);
    return hours + ":" + minutes + ":" + seconds;
}

// Function to get the current date
function getCurrentDate() {
    var date = new Date();
    var options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString(undefined, options);
}

// Function to get the current day
function getCurrentDay() {
    var date = new Date();
    var options = { weekday: 'long' };
    return date.toLocaleDateString(undefined, options);
}

// Function to format time values with leading zeros
function formatTime(value) {
    if (value < 10) {
        value = "0" + value;
    }
    return value;
}

// Function to update the clock display
function updateClock() {
    var timeElement = document.getElementById("time");
    var dateElement = document.getElementById("date");
    var dayElement = document.getElementById("day");
    if (timeElement && dateElement && dayElement) {
        timeElement.innerHTML = getCurrentTime();
        dateElement.innerHTML = getCurrentDate();
        dayElement.innerHTML = getCurrentDay();
        timeElement.classList.add("time-animation");
        setTimeout(function () {
            timeElement.classList.remove("time-animation");
        }, 500);
    }
}

// Update the clock initially and every 1 second
updateClock();
setInterval(updateClock, 1000);