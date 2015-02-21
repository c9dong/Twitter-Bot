import tweepy

auth = tweepy.OAuthHandler("lgHnhvQExLozd24dliMg1jAlG", "iesymLrCGhL8HcTLqyo0KSmYvZrxcfolqmi1Q06lnj5beHQEcU")
auth.set_access_token("3050210471-Ka1iB255E90jNpOVFLFIymGwqXVdQKEw8YgpNlk", "I67LL9hhAmcWobFD8qPaAY7YEKs2gdHlaL0IoOx3ggSmw")

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

mentions = api.mentions_timeline(count=20)

for mention in mentions:
    print mention.text
    print mention.user.screen_name