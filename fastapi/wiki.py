import requests
from logger import logging
from fastapi import HTTPException, status


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Wiki():
    __baseURL = 'https://en.wikipedia.org/w/api.php?'
    __baseURLheaders = {'User-Agent': 'FastAPI-TestClient/1.0'}

    @staticmethod
    def get_article_text(article_name):
        url = Wiki.__baseURL + f'action=query&prop=extracts&titles={article_name}&explaintext=True&format=json'
        logger.info(f'Processing with URL: {url}')

        response = requests.get(url, headers=Wiki.__baseURLheaders)
        response.raise_for_status()
        data = response.json()

        try:
            page_id = list(data['query']['pages'].keys())[0]
            article_text = data['query']['pages'][page_id]['extract']
        except Exception as e:
            logger.error('Incorrect page title was given')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        
        return article_text
    
    @staticmethod
    def search_articles(query):
        url = Wiki.__baseURL + f'action=query&list=search&srsearch={query}&format=json'

        response = requests.get(url, headers=Wiki.__baseURLheaders)
        response.raise_for_status()
        search_data = response.json()
        
        pages_id = list()

        for page in search_data['query']['search']:
            pages_id.append(page['pageid'])


        articles_response = requests.get(Wiki.__baseURL + f'action=query&format=json&pageids={'|'.join(map(str, pages_id))}', headers=Wiki.__baseURLheaders)
        articles_response.raise_for_status()

        articles_data = articles_response.json()
        articles = list()

        for article in articles_data['query']['pages'].values():
            articles.append(article['title'])
        
        return articles
        