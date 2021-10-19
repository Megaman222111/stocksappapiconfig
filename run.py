import styvio

data = styvio.get_data('HKG: 9988')

companyDescription = data['companyDescription']

logoURL = data['logoURL']

currentPrice = data['currentPrice']

newsArticle1 = data["newsArticle1"]
newsArticle2 = data["newsArticle2"]
newsArticle3 = data["newsArticle3"]

newsLink1 = data["newsLink1"]
newsLink2 = data["newsLink2"]
newsLink3 = data["newsLink3"]

print(companyDescription, "\n")

print(logoURL, "\n")

print(newsArticle1, "\n")
print(newsArticle2, "\n")
print(newsArticle3, "\n")

print(newsLink1, "\n")
print(newsLink2, "\n")
print(newsLink3, "\n")

print(currentPrice, "\n")
