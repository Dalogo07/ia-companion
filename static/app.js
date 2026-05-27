const input = document.getElementById("input");
const chat = document.getElementById("chat");

async function send() {
    const message = input.value.trim();
    if (!message) return;

    input.value = "";
    input.style.height = "38px";

    chat.innerHTML += `<div class="msg-user">${message}</div>`;
    scrollToBottom();

    // 🟡 typing indicator
    const typingId = "typing-" + Date.now();
    chat.innerHTML += `
        <div class="msg-ai" id="${typingId}">
            Escribiendo<span id="${typingId}-dots">.</span>
        </div>
    `;
    scrollToBottom();

    animateDots(typingId + "-dots");

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await res.json();

    // quitar typing
    document.getElementById(typingId).remove();

    chat.innerHTML += `<div class="msg-ai">${data.response}</div>`;
    scrollToBottom();
}

/* ENTER */
input.addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        send();
    }
});

/* auto resize */
input.addEventListener("input", function () {
    this.style.height = "38px";
    this.style.height = Math.min(this.scrollHeight, 120) + "px";
});

/* scroll */
function scrollToBottom() {
    chat.scrollTop = chat.scrollHeight;
}

/* animación puntos */
function animateDots(id) {
    let el = document.getElementById(id);
    let count = 0;

    setInterval(() => {
        if (!el) return;

        count = (count + 1) % 4;

        if (count === 0) el.innerText = "";
        else el.innerText = ".".repeat(count);
    }, 400);
}