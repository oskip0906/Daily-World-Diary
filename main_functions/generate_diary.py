import os 
import datetime
from openai import OpenAI
from dotenv import load_dotenv
import scrape_google_news 


load_dotenv()

client = OpenAI(
    api_key=os.environ.get("secret_api_key")
)

chatgpt_model = os.getenv("chatgpt_model")


def process_articles(news_articles):

    content = ""
    
    for article in news_articles:
        content += "\nEvent 1: " + article.title + "\n" + article.summary

    return content


def generate():

    scraped_articles = scrape_google_news.scrape()

    setup = "Write a diary for the world starting with 'Dear Diary', covering all events listed below in a formal but creative tone (Do not use any characters other than punctuation, letters, and numbers): "
    prompt = setup + process_articles(scraped_articles)

    completion = client.chat.completions.create(
        messages = [
            {"role": "system", "content": "Your name is World-Diary-GPT. You are responsible for writing diaries about the world everyday."},
            {"role": "user", "content": prompt}
        ],
        model = chatgpt_model,
        max_tokens = 1000,
        temperature = 0.5
    )

    output = completion.choices[0].message.content

    output += "\n\nSources (not all might have been used):"

    for article in scraped_articles:
        output += "\n" + f'<a href="{article.link}" target="_blank">{article.title}</a>'

    file_path = f"daily_diaries/{datetime.date.today()}.txt"
    
    with open(file_path, 'w') as file:
        file.write(output)


generate()