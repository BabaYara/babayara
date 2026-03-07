import re, html

with open('codex_spec.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<div class="code"><pre><code>(.*?)</code></pre></div>', content, re.DOTALL)
if match:
    code = html.unescape(match.group(1))
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Success")
else:
    print("Not found")
