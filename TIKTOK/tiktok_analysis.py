import os
from TikTokApi import TikTokApi as tiktok
import json

# create authenticator
tiktok_cookie = os.environ.get("TikTokCookie")

# Create a tiktok instance
api = tiktok.get_instance(custom_verifyFp=tiktok_cookie, use_test_endpoints=True)

# Querry some tiktok data (Trending abt python by hashtag)
request = api.by_hashtag("Python")
print(request)
