const currentDate = new Date();
const year = currentDate.getFullYear();
const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); 
const day = currentDate.getDate().toString().padStart(2, '0'); 

const file = `daily_diaries/${year}-${month}-${day}.txt`;

async function fetchFileContent(file) {
    const response = await fetch(file); 
    const text = await response.text(); 
    return text;
}

async function insertFileContent() {
    const diary = document.getElementById('diary');
    const text = await fetchFileContent(file); 
    const textWithLineBreaks = text.replace(/\n/g, '<br>');
    diary.innerHTML = `<br><h1>${year}-${month}-${day}</h1><br>` + textWithLineBreaks;
}

window.addEventListener('load', insertFileContent);