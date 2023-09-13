import openai
import scrape_google_news 
import datetime

openai.api_key = "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"


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
        model = "gpt-3.5-turbo",
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