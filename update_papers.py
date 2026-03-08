import re
import os

filepath = os.path.join("c:\\", "Users", "fababa", "Dropbox", "Tenure", "Website", "index.html")

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to find each paper article
paper_pattern = re.compile(
    r'(<article class="paper".*?>)\s*<header class="paper__head">\s*<h3 class="paper__title">(.*?)</h3>\s*<p class="paper__meta">(.*?)\s*·\s*<span class="paper__year">(.*?)</span>\s*·\s*<span[^>]*>(.*?)</span>\s*</p>\s*</header>\s*<p class="paper__claim">(.*?)</p>\s*<div class="paper__chips">(.*?)</div>(.*?</article>)',
    re.DOTALL
)

def replace_paper(match):
    article_tag = match.group(1)
    title = match.group(2)
    authors = match.group(3).strip()
    year = match.group(4)
    status = match.group(5)
    claim = match.group(6)
    chips = match.group(7)
    rest_of_article_including_details = match.group(8)
    
    # We also need to fix `.pill` to `.text-link` inside rest_of_article_including_details
    rest_of_article_including_details = rest_of_article_including_details.replace('class="pill"', 'class="text-link"')

    new_html = f'''{article_tag}
          <aside class="paper__meta-col">
            <p class="paper__year">{year}</p>
            <p class="paper__status">{status}</p>
          </aside>

          <div class="paper__content-col">
            <h3 class="paper__title">{title}</h3>
            <p class="paper__authors">{authors}</p>
            <p class="paper__claim">{claim}</p>

            <div class="paper__chips">{chips}</div>
{rest_of_article_including_details}'''
    return new_html

new_html = paper_pattern.sub(replace_paper, html)

# Write back
with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated index.html")
