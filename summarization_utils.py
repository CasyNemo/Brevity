import datetime
import requests
from transformers import BartTokenizer, BartForConditionalGeneration

def get_news_articles(query, days=1, lang='en'):
    api_key = 'uevYdrdRm2rGj6LGLTLGRkWSf4e5f4GJ5aKbG97MqPY'
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days)
    url = f'https://api.newscatcherapi.com/v2/search?q={query}&lang={lang}&sort_by=relevancy&from={start_date}&to={end_date}&page=1'

    headers = {
        'x-api-key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['articles']
    else:
        print(
            f"Error fetching news articles for {query}. Status code: {response.status_code}, Content: {response.content}")
        return None

def refined_summarize_text(text, read_time, tokenizer, model):
    max_length_dict = {1: 50, 3: 75, 5: 100, 10: 200}
    max_length = max_length_dict[read_time]
    min_length = int(max_length * 0.8)  # You can adjust this factor to control the minimum summary length

    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(
        inputs['input_ids'],
        num_beams=4,
        max_length=max_length,
        min_length=min_length,
        early_stopping=True
    )
    summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]

    return summary[0]

def main():
    read_time = int(input("Enter your preferred read time (1, 3, 5 or 10 minutes): "))

    if read_time not in [1, 3, 5, 10]:
        print("Invalid read time. Choose 1, 3, 5 or 10 minutes.")
        return

    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    topics = ['Finance', 'Sport', 'Technology', 'Entertainment', 'Politics', 'Health', 'Stocks', 'World News']

    for topic in topics:
        print(f'\n{topic}')
        query = topic.lower()
        articles = get_news_articles(query)

        if articles is None:
            print("Error fetching news articles.")
            return

        combined_text = ' '.join([article['summary'] for article in articles])
        summary = refined_summarize_text(combined_text, read_time, tokenizer, model)

        if not summary:
            summary = "Not enough content to generate a summary for this topic."

        print(summary)

def get_summaries(read_time):
    if read_time not in [1, 3, 5, 10]:
        return "Invalid read time. Choose 1, 3, 5, or 10 minutes."

    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    topics = ['Finance', 'Sport', 'Technology', 'Entertainment', 'Politics', 'Health', 'Stocks', 'World News']
    summaries = {}

    for topic in topics:
        query = topic.lower()
        articles = get_news_articles(query)

        if articles is None:
            summaries[topic] = "Error fetching news articles."
            continue

        combined_text = ' '.join([article['summary'] for article in articles])
        summary = refined_summarize_text(combined_text, read_time, tokenizer, model)

        if not summary:
            summary = "Not enough content to generate a summary for this topic."

        summaries[topic] = summary

    return summaries
