import os 
import openai
import scrape_google_news 
import datetime
from dotenv import load_dotenv, dotenv_values


load_dotenv()

openai.api_key = os.getenv("secret_api_key")
chatgpt_model = os.getenv("chatgpt_model")


def process_articles(news_articles):

    content = ""
    
    for article in news_articles:
        content += "\nEvent 1: " + article.title + "\n" + article.summary

    return content


def generate():

    scraped_articles = scrape_google_news.scrape()

    setup = "You are now 'World-Diary-GPT'. Write a diary for the world today covering all events listed below in a formal but creative tone: "
    prompt = setup + process_articles(scraped_articles)

    completion = openai.ChatCompletion.create(
        model = chatgpt_model,
        messages = [{"role": "user", "content": prompt}]
    )

    output = completion.choices[0].message.content

    output += "\n\nSources (not all might have been used):"

    for article in scraped_articles:
        output += "\n" + f'<a href="{article.link}" target="_blank">{article.title}</a>'

    file_path = f"daily_diaries/{datetime.date.today()}.txt"
    
    with open(file_path, 'w') as file:
        file.write(output)


generate()