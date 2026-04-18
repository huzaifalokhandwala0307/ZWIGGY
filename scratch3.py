import os
import shutil
import re

template_dir = 'templates'

# 1. Rename index.html to predict.html
index_path = os.path.join(template_dir, 'index.html')
predict_path = os.path.join(template_dir, 'predict.html')
if os.path.exists(index_path):
    shutil.move(index_path, predict_path)

# 2. Create home.html with the original landing page content
home_content = """{% extends "base.html" %}

{% block content %}
<!-- ── Hero / Welcome ── -->
    <header class="hero">
        <p class="welcome">Welcome to</p>
        <h1 class="brand-name">Zwiggy</h1>
        <p class="hero-sub">Order from your favourite restaurants, delivered fast.</p>
    </header>

    <!-- ── Restaurant Listing ── -->
    <main class="orderpage">
        <h2 class="section-title">Choose Your Restaurant</h2>

        <div class="restaurant-gallery">

            <a href="/dominos" class="restaurant-card">
                <div class="card-img-wrap">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Dominos_pizza_logo.svg" alt="Dominos logo">
                </div>
                <p class="card-name">Dominos</p>
                <span class="card-tag">Pizza · Fast Food</span>
            </a>

            <a href="/kfc" class="restaurant-card">
                <div class="card-img-wrap">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/KFC_logo.svg" alt="KFC logo">
                </div>
                <p class="card-name">KFC</p>
                <span class="card-tag">Chicken · Fast Food</span>
            </a>

            <a href="/mcdonalds" class="restaurant-card">
                <div class="card-img-wrap">
                   <img src="{{ url_for('static', filename='mcdonalds.svg') }}">
                </div>
                <p class="card-name">McDonald's</p>
                <span class="card-tag">Burgers · Fast Food</span>
            </a>

            <a href="/subway" class="restaurant-card">
                <div class="card-img-wrap">
                    <img src="{{ url_for('static', filename='subway.svg') }}">
                </div>
                <p class="card-name">Subway</p>
                <span class="card-tag">Sandwiches · Healthy</span>
            </a>

            <a href="/localcafe" class="restaurant-card">
                <div class="card-img-wrap">
                    <img src="https://cdn-icons-png.flaticon.com/512/1046/1046784.png" alt="Local Cafe">
                </div>
                <p class="card-name">Local Cafe</p>
                <span class="card-tag">Cafe · Beverages</span>
            </a>

        </div>
    </main>

    <!-- ── Our Services ── -->
    <section class="ourservices">
        <h2 class="section-title">Our Services</h2>
        <ul class="services-list">
            <li class="service-item">
                <a href="/home">
                    <span class="service-icon">🛵</span>
                    <p>Delivery App</p>
                </a>
            </li>
            <li class="service-item">
                <a href="/support">
                    <span class="service-icon">🎧</span>
                    <p>Customer Support</p>
                </a>
            </li>
            <li class="service-item">
                <a href="/predict">
                    <span class="service-icon">⏱️</span>
                    <p>Predict Delivery Time</p>
                </a>
            </li>
        </ul>
    </section>
{% endblock %}
"""
home_path = os.path.join(template_dir, 'home.html')
with open(home_path, 'w', encoding='utf-8') as f:
    f.write(home_content)

# 3. Clean base.html
# Need to remove the hero/restaurant sections if they are still there
base_path = os.path.join(template_dir, 'base.html')
with open(base_path, 'r', encoding='utf-8') as f:
    base_content = f.read()

# I will replace the block content area completely
base_content = re.sub(r'{% block content %}.*?{% endblock %}', '{% block content %}{% endblock %}', base_content, flags=re.DOTALL)

# Update navbar links in base.html
base_content = base_content.replace('<li><a href="/">Home</a></li>', '<li><a href="/home">Home</a></li>')
base_content = base_content.replace('<li><a href="/home">Predict Time</a></li>', '<li><a href="/predict">Predict Time</a></li>')

with open(base_path, 'w', encoding='utf-8') as f:
    f.write(base_content)

print("Done creating home.html, renaming index.html to predict.html, and cleaning base.html")
