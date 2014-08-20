from twython import Twython

APP_KEY='<API key>'
APP_SECRET='<API secret>'
OAUTH_TOKEN='<Access token>'
OAUTH_TOKEN_SECRET='<Access token secret>'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.update_status(status='This is a test of the Weatherbot service.')
