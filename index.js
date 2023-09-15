async function fetchFileContent(file) {

    const response = await fetch(file);

    if (!response.ok) {
        return "The requested diary does not exist.";
    }

    const text = await response.text();
    return text;

}


async function insertFileContent(file, date) {

    const diary = document.getElementById('diary');
    const text = await fetchFileContent(file);
    const textWithLineBreaks = text.replace(/\n/g, '<br>');

    diary.innerHTML = `<br><h1>"${date}"</h1><br>` + textWithLineBreaks;

}


function processDate() {

    var date = document.getElementById("date").value;
    var file = `daily_diaries/${date}.txt`;

    const loadButton = document.getElementById("loadButton");
    loadButton.disabled = true;

    insertFileContent(file, date)
        .then(() => {
            loadButton.disabled = false;
        })

}


function getCurrentDate() {

    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');

    return `${year}-${month}-${day}`;

}


document.addEventListener("DOMContentLoaded", function () {
    const dateContainer = document.getElementById("dateContainer");
    dateContainer.innerHTML = `Current Date: ${getCurrentDate()}`;
});