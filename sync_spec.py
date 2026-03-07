import re, html, os

codex_path = os.path.join("c:\\", "Users", "fababa", "Dropbox", "Tenure", "Website", "codex_spec.html")
index_path = os.path.join("c:\\", "Users", "fababa", "Dropbox", "Tenure", "Website", "index.html")

with open(index_path, 'r', encoding='utf-8') as f:
    idx_content = f.read()

escaped_idx = html.escape(idx_content)

with open(codex_path, 'r', encoding='utf-8') as f:
    codex_content = f.read()

def replacer(match):
    return match.group(1) + escaped_idx + match.group(3)

new_codex = re.sub(
    r'(<div class="code"><pre><code>)(.*?)(</code></pre></div>)',
    replacer,
    codex_content,
    flags=re.DOTALL
)

with open(codex_path, 'w', encoding='utf-8') as f:
    f.write(new_codex)

print("Synchronized index.html back into codex_spec.html.")
