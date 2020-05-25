# Data Fest 2020
## Install
Follow the instruction here: https://github.com/DocNow/twarc

## Usage
` python dataobtainer.py [InputFileName] [OutputFileName] [tweets_num(OPTIONAL)]`

现在读取的attribute:
```
["id", "created_at", "full_text", "retweets_count", "favorite_count", "reply_count", "quote_count", ["user", "id"],
 ["entities", "hashtags"], ["entities", "user_mentions"]]
 ```
 
 所有attribute: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
