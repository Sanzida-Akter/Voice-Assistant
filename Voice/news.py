import requests

api_address = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-04-01&'
       # 'to=2024-04-01&'
       'sortBy=publishedAt&'
       'language=en&'
       'apiKey=1adb75e001834fdc93c06e137497cb12')

json_data = requests.get(api_address).json()

ar=[]

def news():
    articles = json_data.get("articles", [])  # Get the list of articles, or an empty list if not found
    sorted_articles = sorted(articles, key=lambda x: x["publishedAt"], reverse=True)  # Sort articles by published timestamp
    for i in range(min(3, len(sorted_articles))):  # Ensure you iterate up to the minimum of 3 or the length of sorted_articles
        ar.append("Number"+str(i+1)+":" + sorted_articles[i]["title"]+".")

    return ar

# arr=news()
#
# print(arr)
