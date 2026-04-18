import os
import re

template_dir = 'templates'

# 1. Update base.html
base_path = os.path.join(template_dir, 'base.html')
with open(base_path, 'r', encoding='utf-8') as f:
    base_content = f.read()

# Wrap lines between </nav> and <footer class="footer"> with {% block content %}
base_content = re.sub(
    r'(</nav>\s*)(<!-- ── Hero.*?)(<!-- ── Footer ── -->)',
    r'\1\n{% block content %}\n\2\n{% endblock %}\n\n\3',
    base_content,
    flags=re.DOTALL
)

with open(base_path, 'w', encoding='utf-8') as f:
    f.write(base_content)

# 2. Update other HTML files
files_to_update = [
    'index.html', 'dominos.html', 'kfc.html', 'localcafe.html', 
    'subway.html', 'support.html', 'login.html', 'payment.html', 'mcdonald.html'
]

for filename in files_to_update:
    filepath = os.path.join(template_dir, filename)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract body content (between <body> and scripts)
    # Match everything between <body> and the first <script or </body>
    body_match = re.search(r'<body[^>]*>(.*?)(?:<script|</body>)', content, flags=re.DOTALL | re.IGNORECASE)
    
    if body_match:
        page_content = body_match.group(1).strip()
    else:
        # Fallback if no <body> tag is found
        page_content = content.strip()

    # Remove any stray <script> tags from the extracted content
    page_content = re.sub(r'<script.*?</script>', '', page_content, flags=re.DOTALL | re.IGNORECASE)
    
    new_content = f'{{% extends "base.html" %}}\n\n{{% block content %}}\n{page_content}\n{{% endblock %}}\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Done updating templates!")
