import json
data = [json.loads(line) for line in open('farmers-protest-tweets-2021-03-5.json','r')]

def top10MasRetweeted():
    data.sort(key=lambda x: x['retweetCount'], reverse=True)
    top10 = [tweets["user"]["description"] for tweets in data[:10]]
    print("Top 10 mas retweeted:\n")
    for tweet in range(len(top10)):
        print(tweet, top10[tweet])


if __name__ == "__main__":
    top10MasRetweeted()