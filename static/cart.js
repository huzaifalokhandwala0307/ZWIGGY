// ================================
//   ZWIGGY — CART.JS (merged)
//   Works on both menu pages
//   and the cart page
// ================================

const CART_KEY     = "cart"
const DELIVERY_FEE = 29

// ── Get cart ──
function getCart () {
  return JSON.parse(localStorage.getItem(CART_KEY)) || []
}

// ── Save cart ──
function saveCart (cart) {
  localStorage.setItem(CART_KEY, JSON.stringify(cart))
}

// ────────────────────────────────
//   MENU PAGE FUNCTIONS
// ────────────────────────────────

function addToCart (name, price, btn) {
  const cart     = getCart()
  const existing = cart.find(i => i.name === name)
  if (existing) { existing.qty++ }
  else { cart.push({ name, price: parseInt(price), qty: 1 }) }
  saveCart(cart)
  updateCartBadge()
  animateBtn(btn)
  showToast(name + " added to cart!")
}

function animateBtn (btn) {
  if (!btn) return
  btn.textContent = '✓ Added'
  btn.style.background = '#FC8019'
  btn.style.color = '#fff'
  btn.style.borderColor = '#FC8019'
  setTimeout(() => {
    btn.textContent = 'Add +'
    btn.style.background = ''
    btn.style.color = ''
    btn.style.borderColor = ''
  }, 1200)
}

function goToCart () {
  window.location.href = "/cart"
}

function updateCartBadge () {
  const cart  = getCart()
  const count = cart.reduce((s, i) => s + i.qty, 0)
  let badge   = document.getElementById('cartBadge')

  if (!badge) {
    const navbar = document.querySelector('.nav-links')
    if (!navbar) return
    const li = document.createElement('li')
    li.innerHTML = `
      <a href="/cart" style="position:relative;">
        🛒 Cart
        <span id="cartBadge" style="
          position:absolute; top:-4px; right:-4px;
          background:#FC8019; color:white;
          font-size:0.6rem; font-weight:800;
          width:16px; height:16px; border-radius:50%;
          display:flex; align-items:center; justify-content:center;
        ">${count}</span>
      </a>
    `
    navbar.appendChild(li)
    badge = document.getElementById('cartBadge')
  }

  badge.textContent = count
  badge.style.display = count > 0 ? 'flex' : 'none'
}

function initAddButtons () {
  document.querySelectorAll('.menu-card').forEach(card => {
    const btn     = card.querySelector('.add-btn')
    const nameEl  = card.querySelector('.menu-name')
    const priceEl = card.querySelector('.menu-price')
    if (!btn || !nameEl || !priceEl) return
    const name  = nameEl.textContent.trim()
    const price = parseInt(priceEl.textContent.replace(/[^0-9]/g, ''))
    btn.addEventListener('click', () => addToCart(name, price, btn))
  })
}

// ────────────────────────────────
//   CART PAGE FUNCTIONS
// ────────────────────────────────

function loadCart () {
  const cart    = getCart()
  const cartDiv = document.getElementById("cartItems")
  const totalEl = document.getElementById("total")
  const emptyEl = document.getElementById("cartEmpty")

  if (!cartDiv) return

  let subtotal = 0
  cartDiv.innerHTML = ""

  if (cart.length === 0) {
    if (emptyEl) emptyEl.classList.add('visible')
    if (totalEl) totalEl.innerText = "Total: ₹0"
    updateSummary(0)
    return
  }

  if (emptyEl) emptyEl.classList.remove('visible')

  cart.forEach((item, i) => {
    const itemTotal = item.price * item.qty
    subtotal += itemTotal
    cartDiv.innerHTML += `
      <div class="cart-item" id="item-${i}">
        <div>
          <p class="item-name">${item.name}</p>
          <p class="item-unit-price">₹${item.price} each</p>
        </div>
        <div class="item-controls">
          <button class="qty-btn" onclick="changeQty(${i}, -1)">−</button>
          <span class="qty-num">${item.qty}</span>
          <button class="qty-btn plus" onclick="changeQty(${i}, 1)">+</button>
          <span class="item-total">₹${itemTotal}</span>
          <button class="remove-btn" onclick="removeItem(${i})" title="Remove">✕</button>
        </div>
      </div>
    `
  })

  if (totalEl) totalEl.innerText = "Total: ₹" + subtotal
  updateSummary(subtotal)
}

function updateSummary (subtotal) {
  const taxes = Math.round(subtotal * 0.05)
  const total = subtotal === 0 ? 0 : subtotal + DELIVERY_FEE + taxes
  const set = (id, val) => { const el = document.getElementById(id); if (el) el.textContent = val }
  set('subtotal',    `₹${subtotal}`)
  set('deliveryFee', subtotal === 0 ? '₹0' : `₹${DELIVERY_FEE}`)
  set('taxes',       `₹${taxes}`)
  set('total',       `₹${total}`)
}

function changeQty (index, delta) {
  const cart = getCart()
  cart[index].qty += delta
  if (cart[index].qty <= 0) cart.splice(index, 1)
  saveCart(cart)
  loadCart()
}

function removeItem (index) {
  const cart = getCart()
  cart.splice(index, 1)
  saveCart(cart)
  loadCart()
}

function placeOrder () {
  const cart = getCart()
  if (cart.length === 0) { showToast("Cart is empty!"); return }
  showToast("Order placed! Redirecting...")
  localStorage.removeItem(CART_KEY)
  setTimeout(() => { window.location.href = "/home" }, 1800)
}

// ────────────────────────────────
//   SHARED UTILITIES
// ────────────────────────────────

function showToast (message) {
  let toast = document.getElementById('zwiggyToast')
  if (!toast) {
    toast = document.createElement('div')
    toast.id = 'zwiggyToast'
    toast.style.cssText = `
      position:fixed; bottom:28px; left:50%;
      transform:translateX(-50%) translateY(80px);
      background:linear-gradient(135deg,#FC8019,#F4531C);
      color:white; font-family:Nunito,sans-serif;
      font-size:0.88rem; font-weight:700;
      padding:12px 24px; border-radius:100px;
      box-shadow:0 8px 24px rgba(252,128,25,0.4);
      z-index:9999; opacity:0; white-space:nowrap;
      transition:transform 0.3s cubic-bezier(0.22,1,0.36,1),opacity 0.3s;
    `
    document.body.appendChild(toast)
  }
  toast.textContent = '🛵 ' + message
  toast.style.transform = 'translateX(-50%) translateY(0)'
  toast.style.opacity = '1'
  clearTimeout(toast._timeout)
  toast._timeout = setTimeout(() => {
    toast.style.transform = 'translateX(-50%) translateY(80px)'
    toast.style.opacity = '0'
  }, 2200)
}

// ────────────────────────────────
//   INIT
// ────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  loadCart()
  initAddButtons()
  updateCartBadge()
})