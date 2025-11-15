from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from wiki import Wiki

app = FastAPI()


@app.get("/article/{article_name}")
async def get_article(article_name):
    article_text = Wiki.get_article_text(article_name)

    return article_text


@app.get("/search/{query}")
async def search_articles(query: str, count: int = 5):
    articles = Wiki.search_articles(query, count)

    return articles


client = TestClient(app)

print(client.get('/article/earth').json())
print(client.get('/search/earth?count=1').json())