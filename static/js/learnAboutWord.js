function applyFormatting(text) {
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>'); // Жирное начертание
    text = text.replace(/`(.*?)`/g, '<code>$1</code>'); // Моноширинный шрифт
    text = text.replace(/__(.*?)__/g, '<u>$1</u>'); // Подчеркивание
    text = text.replace(/####/g, '&emsp;&emsp;'); // Отступ
    console.log(text)
    return text;
}

function sendRequest(path) {
    const userInput = getUserInput();
    showLoadingIndicator();
    fetchData(path, userInput)
        .then(data => {
            const formattedData = applyFormatting(data.user_message);
            renderCard(formattedData);
        })
        .catch(error => {
            handleError(error);
        })
        .finally(() => {
            hideLoadingIndicator();
        });
}

function getUserInput() {
    return document.getElementById('userInput').value;
}

function showLoadingIndicator() {
    const buttonGroup = document.querySelector('.button-big-group');
    const loadElement = document.querySelector('.load-element');
    buttonGroup.style.display = 'none';
    loadElement.style.display = 'block';
}

function fetchData(path, userInput) {
    return fetch(path, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.csrfToken,
        },
        body: JSON.stringify({ user_message: userInput }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    });
}

function renderCard(formattedData) {
    const resultElement = document.querySelector('.answer-box');
    const cardHtml = `
        <div class="card w-75 mb-3 ${getRandomBootstrapBorderColor()} bg-dark text-white">
            <div class="card-body answer">${formattedData}</div>
        </div>
    `;
    resultElement.innerHTML = cardHtml + resultElement.innerHTML;
}

function getRandomBootstrapBorderColor() {
    const bootstrapBorderColors = ['border-primary', 'border-secondary', 'border-success', 'border-danger', 'border-warning', 'border-info', 'border-light'];
    return bootstrapBorderColors[Math.floor(Math.random() * bootstrapBorderColors.length)];
}

function handleError(error) {
    console.error('Error:', error);
}

function hideLoadingIndicator() {
    const buttonGroup = document.querySelector('.button-big-group');
    const loadElement = document.querySelector('.load-element');
    buttonGroup.style.display = 'block';
    loadElement.style.display = 'none';
}

function usageInContext() {
    console.log('DONE')
    sendRequest('/magic_hat/word/usageInContext/');
}

function toPronounceWord() {
    sendRequest('/magic_hat/word/toPronounceWord/');
}

function articleAndPlural() {
    sendRequest('/magic_hat/word/articleAndPlural/');
}

function meaningOfWord() {
    sendRequest('/magic_hat/word/meaningOfWord/');
}

function howToMemorize() {
    sendRequest('/magic_hat/word/howToMemorize/');
}

function historyOfWord() {
    sendRequest('/magic_hat/word/historyOfWord/');
}


