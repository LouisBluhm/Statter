import tweepy

consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#api.update_status('Sent from StatterApp')

search_user = raw_input('\nEnter Twitter username: ')

data = api.get_user(str(search_user))

print('\nFollowers: ' + str(data.followers_count))
print('Following: ' + str(data.friends_count))
print('Tweets: ' + str(data.statuses_count))
print('\nWriting data to data.txt\n')

file = open('data.txt', 'w')
file.write('Username: ' + search_user)
file.write('\nFollowers: ' + str(data.followers_count))
file.write('\nTweets: ' + str(data.statuses_count))