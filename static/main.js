// ================================
//   ZWIGGY — MAIN.JS
//   Shared across all pages
// ================================

// ── Highlight active nav link ──
document.querySelectorAll('.nav-links a').forEach(link => {
  if (link.href === window.location.href) {
    link.style.color = '#FC8019'
    link.style.background = '#FFF3E8'
  }
})

// ── Navbar shadow on scroll ──
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar')
  if (!navbar) return
  if (window.scrollY > 10) {
    navbar.style.boxShadow = '0 4px 28px rgba(252,128,25,0.18)'
  } else {
    navbar.style.boxShadow = '0 2px 20px rgba(252,128,25,0.07)'
  }
})

// ── Smooth scroll for anchor links ──
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute('href'))
    if (target) target.scrollIntoView({ behavior: 'smooth' })
  })
})
