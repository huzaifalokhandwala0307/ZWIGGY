import os
import re

template_dir = 'templates'
files_to_update = [
    'index.html', 'dominos.html', 'kfc.html', 'localcafe.html', 
    'subway.html', 'support.html', 'mcdonald.html'
]

for filename in files_to_update:
    filepath = os.path.join(template_dir, filename)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove navbar
    new_content = re.sub(r'<!-- ── Navbar ── -->\s*<nav class="navbar">.*?</nav>', '', content, flags=re.DOTALL)
    # Remove footer
    new_content = re.sub(r'<!-- ── Footer ── -->\s*<footer class="footer">.*?</footer>', '', new_content, flags=re.DOTALL)
    # Also strip stray footers and navbars without comments just in case
    new_content = re.sub(r'<nav class="navbar">.*?</nav>', '', new_content, flags=re.DOTALL)
    new_content = re.sub(r'<footer class="footer">.*?</footer>', '', new_content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Done stripping extra navbars and footers!")
