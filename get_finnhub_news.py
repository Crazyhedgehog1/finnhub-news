import finnhub
import pandas as pd
from datetime import datetime

# Prompt the user for a comma-separated list of symbols
symbol_list = input("Enter a comma-separated list of symbols (e.g. AAPL,GOOG,MSFT): ")

# Split the user input into a list of symbols
symbols = [s.strip() for s in symbol_list.split(',')]

# Prompt the user for the start and end dates
start_date = input("Enter the start date (yyyy-mm-dd): ")
end_date = input("Enter the end date (yyyy-mm-dd): ")

# Create an empty list to store the news articles
news_articles = []

# Loop over each ticker symbol in the list
for symbol in symbols:
    # Finnhub API Key
    finnhub_client = finnhub.Client(api_key="chs7oahr01ql90jcnj2gchs7oahr01ql90jcnj30")

    # Get the news articles for the current ticker symbol
    symbol_news = finnhub_client.company_news(symbol, _from=start_date, to=end_date)

    # Add the news articles to the list
    news_articles.extend(symbol_news)

# Create a DataFrame from the news articles
df = pd.DataFrame(news_articles, columns=['category', 'datetime', 'headline', 'id', 'image', 'related', 'source', 'summary', 'url'])

# Format the datetime column as "year/month/day"
df['datetime'] = df['datetime'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d'))

# Prompt the user for the output file name
output_file = input("Enter the output file name (e.g. news.xlsx): ")

# Write the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Saved news articles to {output_file}.")
