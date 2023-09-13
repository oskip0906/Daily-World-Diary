import openai
import scrape_google_news 

openai.api_key = "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"


def process_articles(news_articles):

    content = ""
    
    for article in news_articles:
        content += "\nEvent 1: " + article.title + "\n" + article.summary

    return content


def generate():

    setup = "You are now 'Diary-GPT'. Using the following major news events that happened in the world today, write a diary for the world today in a slightly formal but creative tone (starting with 'Dear World Diary:'): "
    prompt = setup + process_articles(scrape_google_news.scrape())

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    output = completion.choices[0].message.content

    file_path = "diary.txt"
    
    with open(file_path, 'w') as file:
        file.write(output)


generate()