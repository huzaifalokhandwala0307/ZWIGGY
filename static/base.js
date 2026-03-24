// ================================
//   ZWIGGY — BASE.JS
//   Restaurant listing page
// ================================

// ── Restaurant card hover ripple effect ──
document.querySelectorAll('.restaurant-card').forEach(card => {
  card.addEventListener('mouseenter', function () {
    this.style.cursor = 'pointer'
  })

  // Click ripple
  card.addEventListener('click', function (e) {
    const ripple = document.createElement('span')
    const rect   = this.getBoundingClientRect()
    const size   = Math.max(rect.width, rect.height)

    ripple.style.cssText = `
      position: absolute;
      width: ${size}px;
      height: ${size}px;
      left: ${e.clientX - rect.left - size / 2}px;
      top: ${e.clientY - rect.top - size / 2}px;
      background: rgba(252,128,25,0.15);
      border-radius: 50%;
      transform: scale(0);
      animation: rippleAnim 0.5s ease-out forwards;
      pointer-events: none;
      z-index: 10;
    `

    this.style.position = 'relative'
    this.style.overflow = 'hidden'
    this.appendChild(ripple)
    setTimeout(() => ripple.remove(), 500)
  })
})

// ── Add ripple keyframe to page ──
const style = document.createElement('style')
style.textContent = `
  @keyframes rippleAnim {
    to { transform: scale(2.5); opacity: 0; }
  }
  .restaurant-card { text-decoration: none !important; }
`
document.head.appendChild(style)

// ── Service items counter animation ──
function animateCount (el, target, suffix = '') {
  let count = 0
  const step = Math.ceil(target / 40)
  const timer = setInterval(() => {
    count += step
    if (count >= target) {
      count = target
      clearInterval(timer)
    }
    el.textContent = count + suffix
  }, 30)
}

// ── Intersection observer for service section ──
const servicesSection = document.querySelector('.ourservices')
if (servicesSection) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('.service-item').forEach((item, i) => {
          setTimeout(() => {
            item.style.transform = 'translateY(0)'
            item.style.opacity = '1'
          }, i * 120)
        })
        observer.unobserve(entry.target)
      }
    })
  }, { threshold: 0.3 })

  observer.observe(servicesSection)
}
