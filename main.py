import json
data = [json.loads(line) for line in open('farmers-protest-tweets-2021-03-5.json','r')]

def top10MasRetweeted():
    data.sort(key=lambda x: x['retweetCount'], reverse=True)
    top10 = [tweets["content"] for tweets in data[:10]]
    print("Top 10 mas retweeted:\n")
    for tweet in range(len(top10)):
        print(tweet, top10[tweet])

def top10Usuarios():
    users = {}
    for tweets in data:
        if(tweets["user"]["username"] not in users):
            users[tweets["user"]["username"]] = 1
        else:
            users[tweets["user"]["username"]] += 1
    users = sorted(users.items(), key=lambda x: x[1], reverse=True)
    print("Los top 10 usuarios en función de la cantidad de tweets que emitieron.:\n")
    for user in range(10):
        print(user, users[user])

def top10Dias():
    dias = {}
    for tweets in data:
        dia = tweets["date"][:10]
        if(dia not in dias):
            dias[dia] = 1
        else:
            dias[dia] += 1
    dias = sorted(dias.items(), key=lambda x: x[1], reverse=True)
    print("Los top 10 días donde hay más tweets.:\n")
    for dia in range(10):
        print(dia, dias[dia])

def top10hashtag():
    hashtags = {}
    i=0
    for tweets in data:
        content = tweets["content"]
        if("#" not in content):
            continue
        content = content.split("\n")
        for content2 in content:
            content2 = content2.split(" ")
            for content3 in content2:
                if("#" in content3):
                    if(content3 not in hashtags):
                        hashtags[content3] = 1
                    else:
                        hashtags[content3] += 1
    hashtags = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    print("Los top 10 hashtags en función de la cantidad de tweets que contienen.:\n")
    for hashtag in range(10):
        print(hashtag, hashtags[hashtag])

if __name__ == "__main__":
    top10MasRetweeted()
    top10Usuarios()
    top10Dias()
    top10hashtag()