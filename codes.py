from bs4 import BeautifulSoup
import requests
import re
import os

# Replace with your PAT or OAuth credentials
token = os.environ.get('TOKEN')
username = os.environ.get('USER')


# url = "https://api.github.com/repos/overmind-xyz/jpeg-jackpot-clmdpmkw20000jt083z0y186x/blob/main/sources/nft_lottery.move"
url = "https://github.com/Ovodo/pool/blob/main/jackpot.move"
page = requests.get(url)


def format_article(article_html):
    # Parse the HTML content
    soup = BeautifulSoup(article_html, 'html.parser')
    
    # Find the <article> tag
    target_id = "read-only-cursor-text-area"

    article_tag = soup.body.div.find("div", class_="application-main").div.main.find("turbo-frame").script.text
    # print(article_tag)
    
    # if article_tag:
    #     # Find all <h1>, <h2>, <h3>, <h4>, <h5>, <h6> tags within the <article> tag and wrap them in double asterisks
    #     for header in article_tag.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    #         header.string = f"**{header.text}**\n"
        
    #     # Find all <p> tags within the <article> 
    #     for p_tag in article_tag.find_all('p'):
    #         p_tag.string = f"{p_tag.text}\n"
            
    #     # Find all <strong> tags within the <article> tag and wrap them in double asterisks
    #     for strong_tag in article_tag.find_all('strong'):
    #         strong_tag.string = f"**{strong_tag.text}**\n"
        
    #     # Find all <em> tags within the <article> tag and wrap them in single asterisks
    #     for em_tag in article_tag.find_all('em'):
    #         em_tag.string = f"*{em_tag.text}*\n"
        
    #     # Find all <ul> and <ol> tags within the <article> tag and replace them with a list representation
    #     for ul_tag in article_tag.find_all('ul'):
    #         list_items = ul_tag.find_all('li')
    #         ul_tag.replace_with('\n'.join([f"- {item.text}\n" for item in list_items]))
        
    #     for ol_tag in article_tag.find_all('ol'):
    #         list_items = ol_tag.find_all('li')
    #         # ol_tag.replace_with('\n'.join([f"1. {item.text}\n" for item in list_items]))
    #         ol_tag.replace_with(''.join([f"{counter}. {item.text}\n" for counter, item in enumerate(list_items, 1)]))

        
    #     # Find all <code> tags within the <article> tag and wrap them in triple backticks
    #     for code_tag in article_tag.find_all('pre'):
    #         code_tag.string = f"````{code_tag.text}````\n"
        
    #     # Extract text content from the <article> tag and return it without extra spaces
    #     formatted_article = ''.join([str(tag.text) for tag in article_tag.contents])
    # else:
    #     formatted_article = "No <article> tag found in the HTML content."
    
    return article_tag


# Example usage
article_html = """
<html>
  <body>
    <article>
      <h1>This is a heading</h1>
      <p>This is a paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
      <ul>
        <li>List item 1</li>
        <li>List item 2</li>
      </ul>
      <ol>
        <li>List item A</li>
        <li>List item B</li>
      </ol>
      <code>This is a code block</code>
    </article>
  </body>
</html>
"""

formatted_article = format_article(page.text)
print(formatted_article)



