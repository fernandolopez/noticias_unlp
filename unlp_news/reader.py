import requests
import bs4


def get_news():
    response = requests.get("https://www.info.unlp.edu.ar/novedades/")
    return response.text


def parse_titles(html):
    content = bs4.BeautifulSoup(html, "html.parser")
    return [
        {
            "title": anchor.text.strip(),
            "link": anchor.get("href"),
        }
        for result in content.find_all("ul", class_="lcp_catlist")
        for anchor in result.find_all("a")
    ]


def parse_content(html):
    content = bs4.BeautifulSoup(html, "html.parser")
    return content.find("div", class_="entry-inner").text.strip()


def add_content(titles):
    return [
        {
            "title": title["title"],
            "link": title["link"],
            "content": parse_content(requests.get(title["link"]).text),
        }
        for title in titles
    ]


def read_news():
    news_html = get_news()
    titles = parse_titles(news_html)
    return add_content(titles)
