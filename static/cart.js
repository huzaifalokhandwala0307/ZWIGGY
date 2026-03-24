// ================================
//   ZWIGGY — CART.JS
//   Shared across all menu pages
//   Add/remove items, cart drawer,
//   quantity controls, total
// ================================

// ── Cart state ──
let cart = JSON.parse(localStorage.getItem('zwiggy_cart') || '[]')

// ── Save cart to localStorage ──
function saveCart () {
  localStorage.setItem('zwiggy_cart', JSON.stringify(cart))
}

// ── Get total items in cart ──
function getCartCount () {
  return cart.reduce((sum, item) => sum + item.qty, 0)
}

// ── Get cart total price ──
function getCartTotal () {
  return cart.reduce((sum, item) => sum + (item.price * item.qty), 0)
}

// ── Add item to cart ──
function addToCart (name, price, btn) {
  const existing = cart.find(i => i.name === name)

  if (existing) {
    existing.qty++
  } else {
    cart.push({ name, price, qty: 1 })
  }

  saveCart()
  updateCartBadge()
  animateBtn(btn)
  showToast(`${name} added to cart!`)
}

// ── Remove item from cart ──
function removeFromCart (name) {
  cart = cart.filter(i => i.name !== name)
  saveCart()
  updateCartBadge()
  renderCartItems()
}

// ── Update quantity ──
function updateQty (name, delta) {
  const item = cart.find(i => i.name === name)
  if (!item) return
  item.qty += delta
  if (item.qty <= 0) removeFromCart(name)
  else {
    saveCart()
    renderCartItems()
    updateCartBadge()
  }
}

// ── Animate add button ──
function animateBtn (btn) {
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

// ── Toast notification ──
function showToast (message) {
  let toast = document.getElementById('zwiggyToast')
  if (!toast) {
    toast = document.createElement('div')
    toast.id = 'zwiggyToast'
    toast.style.cssText = `
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: linear-gradient(135deg, #FC8019, #F4531C);
      color: white;
      font-family: Nunito, sans-serif;
      font-size: 0.88rem;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 100px;
      box-shadow: 0 8px 24px rgba(252,128,25,0.4);
      z-index: 9999;
      transition: transform 0.3s cubic-bezier(0.22,1,0.36,1), opacity 0.3s;
      opacity: 0;
      white-space: nowrap;
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

// ── Cart badge on navbar ──
function updateCartBadge () {
  let badge = document.getElementById('cartBadge')
  const count = getCartCount()

  if (!badge) {
    const navbar = document.querySelector('.nav-links')
    if (!navbar) return

    const cartBtn = document.createElement('li')
    cartBtn.innerHTML = `
      <a href="#" id="cartToggle" style="position:relative;">
        🛒 Cart
        <span id="cartBadge" style="
          position: absolute;
          top: -4px; right: -4px;
          background: #FC8019;
          color: white;
          font-size: 0.6rem;
          font-weight: 800;
          width: 16px; height: 16px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          font-family: Syne, sans-serif;
        ">${count}</span>
      </a>
    `
    navbar.appendChild(cartBtn)

    document.getElementById('cartToggle').addEventListener('click', e => {
      e.preventDefault()
      toggleCartDrawer()
    })

    badge = document.getElementById('cartBadge')
  }

  badge.textContent = count
  badge.style.display = count > 0 ? 'flex' : 'none'
}

// ── Cart Drawer ──
function createCartDrawer () {
  if (document.getElementById('cartDrawer')) return

  const drawer = document.createElement('div')
  drawer.id = 'cartDrawer'
  drawer.style.cssText = `
    position: fixed;
    top: 0; right: -380px;
    width: 360px;
    height: 100vh;
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(20px);
    border-left: 1.5px solid #F0E4D9;
    box-shadow: -8px 0 40px rgba(252,128,25,0.12);
    z-index: 999;
    display: flex;
    flex-direction: column;
    transition: right 0.35s cubic-bezier(0.22,1,0.36,1);
    font-family: Nunito, sans-serif;
  `

  drawer.innerHTML = `
    <div style="padding:24px 24px 16px; border-bottom:1.5px solid #F0E4D9; display:flex; justify-content:space-between; align-items:center;">
      <h2 style="font-family:Syne,sans-serif; font-size:1.2rem; font-weight:800; color:#1C1C1C; letter-spacing:-0.3px;">Your Cart 🛒</h2>
      <button id="closeCart" style="background:none; border:none; font-size:1.3rem; cursor:pointer; color:#6B6B6B;">✕</button>
    </div>
    <div id="cartItems" style="flex:1; overflow-y:auto; padding:16px 24px;"></div>
    <div style="padding:20px 24px; border-top:1.5px solid #F0E4D9;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <span style="font-weight:700; color:#6B6B6B; font-size:0.85rem;">TOTAL</span>
        <span id="cartTotal" style="font-family:Syne,sans-serif; font-size:1.3rem; font-weight:800; color:#FC8019;"></span>
      </div>
      <button id="checkoutBtn" style="
        width:100%;
        padding:14px;
        background: linear-gradient(135deg,#FC8019,#F4531C);
        color:white;
        font-family:Nunito,sans-serif;
        font-size:0.9rem;
        font-weight:800;
        border:none;
        border-radius:100px;
        cursor:pointer;
        box-shadow:0 6px 20px rgba(252,128,25,0.35);
        transition: transform 0.2s, box-shadow 0.2s;
      ">Place Order 🛵</button>
    </div>
  `

  document.body.appendChild(drawer)

  // Overlay
  const overlay = document.createElement('div')
  overlay.id = 'cartOverlay'
  overlay.style.cssText = `
    position:fixed; inset:0;
    background:rgba(0,0,0,0.3);
    z-index:998;
    display:none;
    backdrop-filter:blur(2px);
  `
  overlay.addEventListener('click', toggleCartDrawer)
  document.body.appendChild(overlay)

  document.getElementById('closeCart').addEventListener('click', toggleCartDrawer)

  document.getElementById('checkoutBtn').addEventListener('click', () => {
    if (cart.length === 0) {
      showToast('Your cart is empty!')
      return
    }
    showToast('Order placed! Redirecting...')
    setTimeout(() => {
      window.location.href = '/predict-page'
    }, 1500)
  })
}

// ── Toggle cart drawer ──
function toggleCartDrawer () {
  const drawer  = document.getElementById('cartDrawer')
  const overlay = document.getElementById('cartOverlay')
  if (!drawer) return

  const isOpen = drawer.style.right === '0px'
  drawer.style.right  = isOpen ? '-380px' : '0px'
  overlay.style.display = isOpen ? 'none' : 'block'

  if (!isOpen) renderCartItems()
}

// ── Render cart items in drawer ──
function renderCartItems () {
  const container = document.getElementById('cartItems')
  const totalEl   = document.getElementById('cartTotal')
  if (!container) return

  if (cart.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:48px 0; color:#A0A0A0;">
        <div style="font-size:3rem; margin-bottom:12px;">🛒</div>
        <p style="font-weight:600; font-size:0.9rem;">Your cart is empty</p>
        <p style="font-size:0.78rem; margin-top:6px;">Add items from the menu!</p>
      </div>
    `
    if (totalEl) totalEl.textContent = '₹0'
    return
  }

  container.innerHTML = cart.map(item => `
    <div style="display:flex; align-items:center; justify-content:space-between; padding:12px 0; border-bottom:1px solid #F0E4D9;">
      <div style="flex:1;">
        <p style="font-weight:700; font-size:0.88rem; color:#1C1C1C; margin-bottom:2px;">${item.name}</p>
        <p style="font-size:0.78rem; color:#FC8019; font-weight:800; font-family:Syne,sans-serif;">₹${item.price * item.qty}</p>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button onclick="updateQty('${item.name}', -1)" style="
          width:26px; height:26px; border-radius:50%;
          background:#FFF3E8; border:1.5px solid rgba(252,128,25,0.25);
          color:#FC8019; font-weight:800; cursor:pointer; font-size:1rem;
          display:flex; align-items:center; justify-content:center;
        ">−</button>
        <span style="font-weight:800; font-size:0.9rem; min-width:14px; text-align:center;">${item.qty}</span>
        <button onclick="updateQty('${item.name}', 1)" style="
          width:26px; height:26px; border-radius:50%;
          background:#FC8019; border:none;
          color:white; font-weight:800; cursor:pointer; font-size:1rem;
          display:flex; align-items:center; justify-content:center;
        ">+</button>
      </div>
    </div>
  `).join('')

  if (totalEl) totalEl.textContent = `₹${getCartTotal()}`
}

// ── Wire up all Add + buttons on the page ──
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

// ── Init on page load ──
createCartDrawer()
updateCartBadge()
initAddButtons()
