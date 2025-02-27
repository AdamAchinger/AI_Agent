function sendText() {
    let inputText = document.getElementById("inputBox").value;
    fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputBox").value = data.corrected_text;
    })
    .catch(error => console.error("Błąd:", error));
}

function changeAgent(agent) {
    fetch("/change_agent", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ agent: agent })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputBox").value = data.example_output;
    })
    .catch(error => console.error("Błąd:", error));

    document.querySelectorAll(".change-button").forEach(btn => btn.classList.remove("active"));
    document.getElementById(agent).classList.add("active");
}




function copyToClipboard() {
    let outputBox = document.getElementById("outputBox");
    if (outputBox.value.trim() === "") {
        //alert("Brak tekstu do skopiowania!");
        return;
    }

    navigator.clipboard.writeText(outputBox.value)
    .then(() => {
        //alert("Tekst skopiowany do schowka!");
    })
    .catch(err => {
        console.error("Błąd kopiowania:", err);
    });
}


function useAsPrompt() {
    let outputText = document.getElementById("outputBox").value;
    if (outputText.trim() !== "") {
        document.getElementById("inputBox").value = outputText;
    }
}

function updateValue(spanId, value) {
    document.getElementById(spanId).textContent = value;
}

function sendText() {
    let inputText = document.getElementById("inputBox").value;
    let temperature = parseFloat(document.getElementById("temperature").value);
    let maxTokens = parseInt(document.getElementById("maxTokens").value);

    fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            text: inputText,
            temperature: temperature,
            max_output_tokens: maxTokens
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputBox").value = data.corrected_text;
    })
    .catch(error => console.error("Błąd:", error));
}

