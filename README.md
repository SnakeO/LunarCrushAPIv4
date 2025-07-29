# LunarCrushAPI
![PyPI version](https://img.shields.io/pypi/v/lunarcrush)

Unofficial LunarCrush API **v2**, **v3**, and **v4** Wrapper for Python. No API key needed for LCv2!

## 💽 Installation
LunarCrushAPI is supported on **Python 3.6+**. You can install this package via pip:
```
pip install lunarcrush
```
## 🔍 Quickstart for LunarCrush API v2
**1.** Create an instance of LunarCrush

```Python
from lunarcrush import LunarCrush

lc = LunarCrush()
```

**2.** Start requesting information!

```Python
eth_1_year_data = lc.get_assets(symbol=['ETH'],
                                data_points=365, interval='day')
```

## 🔍 Quickstart for LunarCrush API v3
**1.** Create an instance of LunarCrushV3

```Python
from lunarcrush import LunarCrushV3

lcv3 = LunarCrushV3('<YOUR API KEY>')
```

**2.** Start requesting information!

```Python
eth_insights = lcv3.get_coin_insights(coin='ETH', metrics='social_volume')
```

## 🔍 Quickstart for LunarCrush API v4
**1.** Create an instance of LunarCrushV4

```Python
from lunarcrush import LunarCrushV4

lcv4 = LunarCrushV4('<YOUR API KEY>')
```

**2.** Start requesting information!

```Python
# Get trending topics
trending_topics = lcv4.get_topics_list()

# Get Bitcoin topic data with social metrics
btc_topic = lcv4.get_topic('bitcoin')
print(f"Bitcoin rank: {btc_topic['data']['topic_rank']}")
print(f"24h interactions: {btc_topic['data']['interactions_24h']:,}")

# Get top posts for a topic
btc_posts = lcv4.get_topic_posts('bitcoin')
for post in btc_posts['data'][:5]:
    print(f"{post['post_type']}: {post['post_title'][:60]}...")

# Get creator analytics
elon = lcv4.get_creator('twitter', 'elonmusk')
print(f"Followers: {elon['data']['creator_followers']:,}")

# Search for posts (Individual tier)
results = lcv4.search(term='ethereum')
```

### 📊 API v4 Tier Requirements

| Feature | Individual | Pro | Enterprise |
|---------|------------|-----|------------|
| Topics, Categories, Creators | ✅ | ✅ | ✅ |
| Posts, Basic Search | ✅ | ✅ | ✅ |
| Time Series Data | ❌ | ✅ | ✅ |
| AI Summaries (whatsup) | ❌ | ❌ | ✅ |
| Advanced Coins/Stocks/NFTs | ❌ | ✅ | ✅ |
| Custom Search Aggregations | ❌ | ✅ | ✅ |

## 📜 API v2 Endpoints
Here is a short description for the LunarCrush API v2 Endpoints.

| Method                                                                | Description                                                                                                                             | Not authorized parameters |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| ```get_assets(symbol, time_series_indicators, change, data_points)``` | Details, overall metrics, and time series metrics for one or multiple assets.                                                           | (*~~start~~*, *~~end~~*)  |
| ```get_market(limit, page, sort)```                                   | Summary information for all supported assets (Markets page) including 5 recent time series values for some metrics.                     |                           |
| ```get_market_pairs(symbol, limit, page)```                           | Provides the exchange information for assets, and the other assets they are being traded for.                                           |                           |
| ```get_global(interval, change, data_points)```                       | Overall aggregated metrics for all supported assets (top of Markets page).                                                              |                           |
| ```get_meta(type)```                                                  | Meta information for all supported assets                                                                                               |                           |
| ```get_exchange(exchange)```                                          | Meta information and market pairs for a single exchange that we track                                                                   |                           |
| ```get_exchanges(limit, order_by)```                                  | Meta information for all exchanges that we track                                                                                        |                           |
| ```get_coin_of_the_day()```                                           | The current coin of the day                                                                                                             |                           |
| ```get_coin_of_the_day_info()```                                      | Provides the history of the coin of the day on LunarCRUSH when it was last changed, and when each coin was last coin of the day         |                           |
| ```get_feeds(sources, page, type, limit)```                           | Social posts, news, and shared links for one or multiple coins.                                                                         | (*~~start~~*, *~~end~~*)  |
| ```get_influencer(id, screen_name, days, page)```                     | Individual influencer details including actual posts.                                                                                   | (*~~limit~~*)             |
| ```get_influencers(symbol, days, num_days, order_by)```               | List of social accounts that have the most influence on different assets based on number of followers, engagements and volume of posts. | (*~~limit~~*)             |

## ⚠️ Warning!
Some parameters might **NOT** work properly for LunarCrush API v2, making the server to response with a *5XX error*.


## 📰 API v3 Endpoints

| Method                                                 | Endpoint                  |
|--------------------------------------------------------|---------------------------|
| ```get_coin_of_the_day()```                            | /coinoftheday             |
| ```get_coin_of_the_day_info()```                       | /coinoftheday/info        |
| ```get_coins(sort, limit, desc)```                     | /coins                    |
| ```get_coin(coin)```                                   | /coins/{coin}             |
| ```get_coin_change(coin, interval)```                  | /coins/{coin}/change      |
| ```get_coin_historical(coin)```                        | /coins/{coin}/historical  |
| ```get_coin_influencers(coin, interval, order)```      | /coins/{coin}/influencers |
| ```get_coin_insights(coin, metrics, limit)```          | /coins/{coin}/insights    |
| ```get_coin_meta(coin)```                              | /coins/{coin}/meta        |
| ```get_coin_time_series(coin, interval, start)```      | /coins/{coin}/time-series |
| ```get_coins_global()```                               | /coins/global             |
| ```get_coins_global_change(interval)```                | /coins/global/change      |
| ```get_coins_global_historical()```                    | /coins/global/historical  |
| ```get_coins_global_insights(metrics, limit)```        | /coins/global/insights    |
| ```get_coins_global_time_series(interval, start)```    | /coins/global/time-series |
| ```get_coins_influencers(interval, order)```           | /coins/influencers        |
| ```get_coins_insights(metrics, limit)```               | /coins/insights           |
| ```get_coins_list()```                                 | /coins/list               |
| ```get_exchanges(order, limit)```                      | /exchanges                |
| ```get_exchange(exchange)```                           | /exchanges/{exchange}     |
| ```get_feeds(limit, since, hours, days, sources)```    | /feeds                    |
| ```get_feed(feed)```                                   | /feeds/{feed}             |
| ```get_influencer(influencer, fast, interval, sort)``` | /influencers/{influencer} |
| ```get_insight(insight, type)```                       | /insights/{insight}       |
| ```get_market_pairs(coin, limit, page, sort)```        | /market-pairs/{coin}      |
| ```get_nft_of_the_day()```                             | /nftoftheday              |
| ```get_nft_of_the_day_info()```                        | /nftoftheday/info         |
| ```get_nfts(sort, limit, desc)```                      | /nfts                     |
| ```get_nft(nft)```                                     | /nft/{nft}                |
| ```get_nft_change(nft, interval)```                    | /nfts/{nft}/change        |
| ```get_nft_historical(nft)```                          | /nfts/{nft}/historical    |
| ```get_nft_influencers(nft, interval, order)```        | /nfts/{nft}/influencers   |
| ```get_nft_insights(nft, metrics, limit)```            | /nfts/{nft}/insights      |
| ```get_nft_time_series(nft, interval, start)```        | /nfts/{nft}/time-series   |
| ```get_nft_tokens(nft, sort)```                        | /nfts/{nft}/tokens        |
| ```get_nfts_global()```                                | /nfts/global              |
| ```get_nfts_global_change(interval)```                 | /nfts/global/change       |
| ```get_nfts_global_historical()```                     | /nfts/global/historical   |
| ```get_nfts_global_insights(metrics, limit)```         | /nfts/global/insights     |
| ```get_nfts_global_time_series(interval, start)```     | /nfts/global/time-series  |
| ```get_nfts_influencers(interval, order)```            | /nfts/influencers         |
| ```get_nfts_insights(metrics, limit)```                | /nfts/insights            |
| ```get_nfts_list()```                                  | /nfts/list                |
| ```get_opinions(context, sort)```                      | /opinions                 |
| ```get_opinions_summary()```                           | /opinions/summary         |
| ```get_spark(spark_id)```                              | /sparks/{spark_id}        |
| ```get_stats_lunrfi()```                               | /stats/lunrfi             |
| ```get_top_mentions(interval, type, market)```         | /top-mentions             |

You can visit [LunarCrush API v3 documentation](https://lunarcrush.com/developers/api/endpoints) for a more detailed description of all the endpoints and parameters.

## 📈 Metrics description
| Metric           | Description                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GALAXY SCORE** | The Galaxy Score™ indicates how healthy a coin is by looking at combined performance indicators across markets and social engagement. Display the real-time Galaxy Score™ of any coin.                                                                                                                                                              |
| **ALT RANK**     | AltRank™ measures a coin's performance VS. all other coins that we actively support. In general, it is a unique measurement that combines ALT coin price performance relative to Bitcoin and other social activity indicators across the entire crypto market. A coin can have a high AltRank of 1 even in a bear market situation.                 |
| **INFLUENCERS**  | View Twitter influencer activity and their impact across all coins and tokens. All influencers are measured by the same metrics, which includes followers, replies, favorites, and retweets. Metrics are evaluated across all collected posts during the timeframe selected. Actual influence will vary over time and will depend on user activity. |
| **CANDLESTICK**  | The incredibly powerful Candlestick widget takes any data point and compares it to price over a specified timeframe.                                                                                                                                                                                                                                |
| **WORD CLOUD**   | Uncover keywords used throughout collected social content for any coin. The Word Cloud is generated from all recent and available social posts from Twitter and Reddit. It looks at frequency of mentions. All data is segmented by either all coins or specific, individual coins.                                                                 |
| **SOCIAL FEED**  | Display social feeds from multiple sources including Twitter, Reddit, news channels and more all at once. Gain unique insights into what's being talked about in real time. All social feeds have been cleaned with spam removed and can be organized by coin.                                                                                      |

## 📰 API v4 Endpoints

### Topics Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_topics_list()` | /public/topics/list/v1 | Get a list of trending social topics |
| `get_topic_whatsup(topic)` | /public/topic/{topic}/whatsup/v1 | AI summary of hottest news and posts for a topic |
| `get_topic(topic)` | /public/topic/{topic}/v1 | Get summary information for a social topic |
| `get_topic_time_series_v2(topic, bucket)` | /public/topic/{topic}/time-series/v2 | Get historical time series data for a topic |
| `get_topic_time_series(topic, bucket, interval, start, end)` | /public/topic/{topic}/time-series/v1 | Get historical time series data for a topic |
| `get_topic_posts(topic, start, end)` | /public/topic/{topic}/posts/v1 | Get top posts for a social topic |
| `get_topic_news(topic)` | /public/topic/{topic}/news/v1 | Get top news posts for a social topic |
| `get_topic_creators(topic)` | /public/topic/{topic}/creators/v1 | Get top creators for a social topic |

### Categories Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_category(category)` | /public/category/{category}/v1 | Get summary information for a social category |
| `get_category_topics(category)` | /public/category/{category}/topics/v1 | Get top topics for a social category |
| `get_category_time_series(category, bucket, interval, start, end)` | /public/category/{category}/time-series/v1 | Get historical time series data for a category |
| `get_category_posts(category, start, end)` | /public/category/{category}/posts/v1 | Get top posts for a social category |
| `get_category_news(category)` | /public/category/{category}/news/v1 | Get top news posts for a category |
| `get_category_creators(category)` | /public/category/{category}/creators/v1 | Get top creators for a social category |
| `get_categories_list()` | /public/categories/list/v1 | Get a list of trending social categories |

### Creators Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_creators_list()` | /public/creators/list/v1 | Get a list of trending social creators |
| `get_creator(network, id)` | /public/creator/{network}/{id}/v1 | Get detail information on a specific creator |
| `get_creator_time_series(network, id, bucket, interval, start, end)` | /public/creator/{network}/{id}/time-series/v1 | Get time series data on a creator |
| `get_creator_posts(network, id, start, end)` | /public/creator/{network}/{id}/posts/v1 | Get top posts for a specific creator |

### Posts Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_post(post_type, post_id)` | /public/posts/{post_type}/{post_id}/v1 | Get details of a post |
| `get_post_time_series(post_type, post_id)` | /public/posts/{post_type}/{post_id}/time-series/v1 | Get interactions over time for a post |

### Coins Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_coins_list_v2(sort, filter, limit, desc, page)` | /public/coins/list/v2 | Get real-time snapshot of tracked coins |
| `get_coins_list(sort, filter, limit, desc, page)` | /public/coins/list/v1 | Get cached snapshot of tracked coins |
| `get_coin(coin)` | /public/coins/{coin}/v1 | Get market data on a coin or token |
| `get_coin_time_series(coin, bucket, interval, start, end)` | /public/coins/{coin}/time-series/v2 | Get market time series data on a coin |
| `get_coin_meta(coin)` | /public/coins/{coin}/meta/v1 | Get meta information for a cryptocurrency |

### Stocks Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_stocks_list_v2(sort, filter, limit, desc, page)` | /public/stocks/list/v2 | Get real-time snapshot of tracked stocks |
| `get_stocks_list(sort, filter, limit, desc, page)` | /public/stocks/list/v1 | Get cached snapshot of tracked stocks |
| `get_stock(stock)` | /public/stocks/{stock}/v1 | Get market data on a stock |
| `get_stock_time_series(stock, bucket, interval, start, end)` | /public/stocks/{stock}/time-series/v1 | Get market time series data on a stock |

### NFTs Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_nfts_list_v2(sort, filter, limit, desc, page)` | /public/nfts/list/v2 | Get real-time snapshot of tracked NFT collections |
| `get_nfts_list(sort, filter, limit, desc, page)` | /public/nfts/list/v1 | Get cached snapshot of tracked NFT collections |
| `get_nft(nft)` | /public/nfts/{nft}/v1 | Get data on an NFT collection |
| `get_nft_time_series_v2(nft, bucket)` | /public/nfts/{nft}/time-series/v2 | Get time series data on an NFT collection |
| `get_nft_time_series(nft, bucket, interval, start, end)` | /public/nfts/{nft}/time-series/v1 | Get time series data on an NFT collection |

### Searches Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `search(term, search_json)` | /public/searches/search | Search for posts matching a term or custom criteria |
| `get_searches_list()` | /public/searches/list | Get a list of saved searches |
| `create_search(name, search_json, priority)` | /public/searches/create | Create a custom search aggregation |
| `update_search(slug, name, search_json)` | /public/searches/{slug}/update | Update a saved search |
| `delete_search(slug)` | /public/searches/{slug}/delete | Delete a saved search |
| `get_searches(slug)` | /public/searches/{slug} | Get summary of a custom search |

### Systems Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_system_changes()` | /public/system/changes | Get recent system changes |

You can visit [LunarCrush API v4 documentation](https://lunarcrush.com/developers/api/authentication) for a more detailed description of all the endpoints and parameters.

### 🔧 API v4 Advanced Examples

#### Working with Topics
```python
# Get AI summary for a topic (Enterprise tier required)
summary = lcv4.get_topic_whatsup('bitcoin')

# Get historical time series (Pro tier required)
btc_history = lcv4.get_topic_time_series('bitcoin', interval='1w')

# Get top creators for a topic
creators = lcv4.get_topic_creators('bitcoin')
for creator in creators['data'][:5]:
    print(f"@{creator['creator_name']} - {creator['interactions_24h']:,} interactions")
```

#### Categories Analysis
```python
# List all categories
categories = lcv4.get_categories_list()

# Get cryptocurrency category metrics
crypto = lcv4.get_category('cryptocurrencies')
print(f"Total posts: {crypto['data']['num_posts']:,}")
print(f"Sentiment: {crypto['data']['types_sentiment']['tweet']}%")

# Get top topics in a category
topics = lcv4.get_category_topics('cryptocurrencies')
```

#### Creator Analytics
```python
# Get creator time series data
elon_history = lcv4.get_creator_time_series('twitter', 'elonmusk', interval='1w')

# Get creator's recent posts
elon_posts = lcv4.get_creator_posts('twitter', 'elonmusk')
```

#### Custom Search (Pro tier)
```python
# Create a custom search aggregation
search_config = {
    "terms": [
        {
            "term": "bitcoin",
            "require": ["price", "bull"],
            "exclude": ["bear", "crash"]
        }
    ]
}
lcv4.create_search("BTC Bull Signals", json.dumps(search_config))

# List your saved searches
my_searches = lcv4.get_searches_list()
```

### ⚠️ Error Handling & Rate Limits

API v4 returns errors in the response instead of raising exceptions:

```python
response = lcv4.get_topic_whatsup('bitcoin')
if 'error' in response:
    print(f"Error: {response['error']}")
    # Common errors:
    # - "Rate limit exceeded (minute)" 
    # - "You must have a Enterprise or API Upgrade subscription to use this endpoint."
else:
    # Process successful response
    print(response['summary'])
```

**Rate Limits by Tier:**
- **Individual**: 60 requests/minute
- **Pro**: 300 requests/minute  
- **Enterprise**: 1000 requests/minute

### 🔄 Migration from v3 to v4

Key differences when upgrading from v3 to v4:

1. **Unified Asset Support**: v4 combines coins, stocks, and NFTs in a unified API
2. **Topics & Categories**: New social analytics based on topics rather than just assets
3. **Creator Analytics**: Enhanced influencer tracking across platforms
4. **AI Integration**: Built-in AI summaries for topics (Enterprise tier)
5. **Better Search**: Custom search aggregations with inclusion/exclusion filters

```python
# v3 approach - coin-focused
coin_data = lcv3.get_coin('BTC')

# v4 approach - topic-focused with richer social data
topic_data = lcv4.get_topic('bitcoin')
coin_data = lcv4.get_coin('BTC')  # Still available for market data
```
