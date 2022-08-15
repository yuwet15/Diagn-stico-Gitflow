import json
data = [json.loads(line) for line in open('farmers-protest-tweets-2021-03-5.json','r')]

def top10MasRetweeted():
    data.sort(key=lambda x: x['retweetCount'], reverse=True)
    top10 = [tweets["user"]["description"] for tweets in data[:10]]
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


if __name__ == "__main__":
    top10MasRetweeted()
    top10Usuarios()