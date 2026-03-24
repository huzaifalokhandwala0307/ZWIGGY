// ================================
//   ZWIGGY — SUPPORT.JS
//   Chat chips, typing indicator,
//   auto-scroll, char counter
// ================================

const input    = document.getElementById('userInput')
const chatBox  = document.getElementById('chatBox')
const form     = document.querySelector('.chat-form')

// ── Chip click → fills input ──
document.querySelectorAll('.chip').forEach(chip => {
  chip.addEventListener('click', function () {
    input.value = this.textContent.trim()
    input.focus()

    // Highlight selected chip
    document.querySelectorAll('.chip').forEach(c => c.classList.remove('chip-active'))
    this.classList.add('chip-active')
  })
})

// ── Auto scroll chat to bottom ──
function scrollToBottom () {
  if (chatBox) {
    chatBox.scrollTop = chatBox.scrollHeight
  }
}

scrollToBottom()

// ── Show typing indicator before submit ──
form && form.addEventListener('submit', function (e) {
  const userText = input.value.trim()
  if (!userText) return

  // Add user bubble instantly
  const userMsg = document.createElement('div')
  userMsg.className = 'message user-message'
  userMsg.innerHTML = `
    <span class="avatar">You</span>
    <div class="bubble">${userText}</div>
  `
  chatBox.appendChild(userMsg)

  // Add typing indicator
  const typing = document.createElement('div')
  typing.className = 'message bot-message'
  typing.id = 'typingIndicator'
  typing.innerHTML = `
    <span class="avatar">🛵</span>
    <div class="bubble typing-bubble">
      <span class="dot"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>
  `
  chatBox.appendChild(typing)
  scrollToBottom()
})

// ── Input character counter ──
input && input.addEventListener('input', function () {
  const max = 200
  const remaining = max - this.value.length
  let counter = document.getElementById('charCounter')

  if (!counter) {
    counter = document.createElement('p')
    counter.id = 'charCounter'
    counter.style.cssText = `
      font-size: 0.7rem;
      color: #A0A0A0;
      text-align: right;
      margin-top: 4px;
      font-family: Nunito, sans-serif;
    `
    this.parentElement.appendChild(counter)
  }

  counter.textContent = `${remaining} characters left`
  counter.style.color = remaining < 20 ? '#FC8019' : '#A0A0A0'

  if (this.value.length > max) {
    this.value = this.value.substring(0, max)
  }
})

// ── Send button arrow animation on hover ──
const sendBtn = document.querySelector('.chat-send-btn')
sendBtn && sendBtn.addEventListener('mouseenter', () => {
  const icon = sendBtn.querySelector('.btn-icon')
  if (icon) icon.style.transform = 'translateX(5px)'
})
sendBtn && sendBtn.addEventListener('mouseleave', () => {
  const icon = sendBtn.querySelector('.btn-icon')
  if (icon) icon.style.transform = 'translateX(0)'
})
