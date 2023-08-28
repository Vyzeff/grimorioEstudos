
import re

URLS = re.compile(r"<a href='(.+?)'>(.+?)</a>") 

def html2markdown(html):
    '''Take in html text as input and return markdown'''


    markdown = ' '.join(html.split())

    if re.search("<em>", markdown):
        markdown = markdown.replace("<em>", "*")
        markdown = markdown.replace("</em>", "*")
    
    if re.search("\n", markdown):
        markdown = markdown.replace("\n", "")
    
    if re.search("<p>", markdown):
        markdown = markdown.replace("<p>", "")
        markdown = markdown.replace("</p>", "\n")
    
    markdown = URLS.sub(r"[\2](\1)", markdown)
    print(markdown)
    return 0

if __name__ == "__main__":
    html2markdown("<p><em>issO \né         um     teste</em>\n</p> <a href='something.com'>something link</a>")