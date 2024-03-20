from unlp_news.reader import read_news
from unlp_news.view import as_table

def main():
    news = read_news()
    as_table(news)

if __name__ == "__main__":
    main()

