import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def generate_summary(text, sentences, language = "english"):
    summarizer = LexRankSummarizer()
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summary_sentences = summarizer(parser.document, sentences)
    summary = " ".join([str(sentence) for sentence in summary_sentences])
    return summary

class news_article:
    def __init__(self, link, title, content_summary):
        self.link = link
        self.title = title
        self.content_summary = content_summary

google_news = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKRFFTZ0FQAQ?hl=en-CA&gl=CA&ceid=CA%3Aen"

req = requests.get(google_news)
soup = BeautifulSoup(req.text, "html.parser")

news_articles = []
article_links = []

for url in soup.find_all("a"):
    href = url.get("href")
    if href and href.startswith("./articles/"):
        link = href.strip()
        article_links.append("https://news.google.com" + link[1:]);

for link in article_links[:5]:
    article_req = requests.get(link)
    article_soup = BeautifulSoup(article_req.text, "html.parser")
    title = article_soup.find('title')
    paragraphs = article_soup.find_all('p')
    content = " ".join([p.get_text() for p in paragraphs])  
    summary = generate_summary(content, 5)
    article = news_article(link, title.string, summary)
    news_articles.append(article)