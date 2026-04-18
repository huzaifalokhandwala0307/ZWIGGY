import os

template_dir = 'templates'
files = ['localcafe.html', 'kfc.html', 'dominos.html', 'mcdonald.html', 'subway.html']

btn_html = '\n<div style="text-align: right; padding: 20px 40px 0;"><button onclick="goToCart()" class="cart-btn" style="background: #FC8019; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 10px rgba(252, 128, 25, 0.2);">🛒 View Cart</button></div>\n'

for filename in files:
    filepath = os.path.join(template_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'goToCart()' not in content:
            content = content.replace('{% block content %}', '{% block content %}' + btn_html)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
print("Added View Cart buttons!")
