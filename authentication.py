import tweepy

auth = tweepy.OAuthHandler("lgHnhvQExLozd24dliMg1jAlG", "iesymLrCGhL8HcTLqyo0KSmYvZrxcfolqmi1Q06lnj5beHQEcU")
auth.set_access_token("3050210471-FnVA5ACLtsDoaGqQeDcRuAB0ps05MipZNIP3cEI", "9KCNgCxcvyHgPKbPoUgjOzEAl9BuiOeSgYn7O4RWXekgb")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text