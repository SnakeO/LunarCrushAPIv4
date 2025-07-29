import time
import datetime
import requests
import urllib.parse
from lunarcrush.base import LunarCrushABC


class LunarCrushV4(LunarCrushABC):
    _BASE_URL = 'https://lunarcrush.com/api4'

    def __init__(self, api_key):
        super().__init__(api_key)

    @staticmethod
    def _parse_kwargs(kwargs):
        req_params = {}
        for param, value in kwargs.items():
            if isinstance(value, list):
                req_params[param] = ','.join(value)
            elif isinstance(value, datetime.datetime):
                req_params[param] = str(int(time.mktime(value.timetuple())))
            elif isinstance(value, bool):
                req_params[param] = str(value.real)
            elif value is not None:
                req_params[param] = value
        return req_params

    def _gen_url(self, endpoint, **kwargs):
        url = self._BASE_URL + endpoint
        if kwargs:
            url += '?' + urllib.parse.urlencode(kwargs)
        return url

    def _request(self, endpoint, **kwargs):
        kwargs = self._parse_kwargs(kwargs)
        url = self._gen_url(endpoint, **kwargs)
        headers = {'Authorization': f'Bearer {self._api_key}'}
        return requests.get(url, headers=headers).json()

    # Topics endpoints
    def get_topics_list(self) -> dict:
        """
        Get a list of trending social topics.
        """
        return self._request('/public/topics/list/v1')

    def get_topic_whatsup(self, topic: str) -> dict:
        """
        Generate an AI summary of the hottest news and social posts for a specific topic.

        :param str topic: Provide the topic to get a summary for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $.
        """
        return self._request(f'/public/topic/{topic}/whatsup/v1')

    def get_topic(self, topic: str) -> dict:
        """
        Get summary information for a social topic. The output is a 24 hour aggregation social activity with metrics
        comparing the latest 24 hours to the previous 24 hours.

        :param str topic: Provide the topic to get details for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $. You can also look up a topic by the coin/nft/stock
                          numeric id like coins:1 for bitcoin or stocks:7056 for nVidia.
        """
        return self._request(f'/public/topic/{topic}/v1')

    def get_topic_time_series_v2(self, topic: str, bucket: str = None) -> dict:
        """
        Get historical time series data for a social topic.

        :param str topic: Provide the topic to get details for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $.
        :param str bucket: Leave blank (default) for the most week aggregated by hour, specify hour for full historical
                           data available in hourly aggregation, specify day for full historical data available in
                           daily aggregation.
        """
        return self._request(f'/public/topic/{topic}/time-series/v2', bucket=bucket)

    def get_topic_time_series(self, topic: str, bucket: str = None, interval: str = None,
                              start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get historical time series data for a social topic.

        :param str topic: Provide the topic to get details for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $.
        :param str bucket: bucket time series data into hours or days. default is hours.
        :param str interval: Use interval to specify the start and end time automatically for convenience.
                             If "start" or "end" parameters are provided this parameter is ignored.
        :param datetime.datetime start: The start time (unix timestamp) to go back to.
        :param datetime.datetime end: The end time (unix timestamp) to stop at.
        """
        return self._request(f'/public/topic/{topic}/time-series/v1',
                             bucket=bucket, interval=interval, start=start, end=end)

    def get_topic_posts(self, topic: str, start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get the top posts for a social topic. If start time is provided the result will be the top posts by
        interactions for the time range. If start is not provided it will be the most recent top posts by
        interactions from the last 24 hours.

        :param str topic: Provide the topic to get details for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $.
        :param datetime.datetime start: The start time (unix timestamp) to start at. Will be rounded to the beginning
                                        of the day. If the end parameter is not provided it will just be the top posts
                                        for this day.
        :param datetime.datetime end: (Optional) The end time (unix timestamp) to stop at. Will be rounded to the end
                                      of the day.
        """
        return self._request(f'/public/topic/{topic}/posts/v1', start=start, end=end)

    def get_topic_news(self, topic: str) -> dict:
        """
        Get the top news posts for a social topic. Top news is determined by the metrics related to the social posts
        that mention the news posts.

        :param str topic: Provide the topic to get details for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $.
        """
        return self._request(f'/public/topic/{topic}/news/v1')

    def get_topic_creators(self, topic: str) -> dict:
        """
        Get the top creators for a social topic.

        :param str topic: Provide the topic to get details for. A topic must be all lower case and can only include
                          letters, numbers, spaces, # and $.
        """
        return self._request(f'/public/topic/{topic}/creators/v1')

    # Categories endpoints
    def get_category(self, category: str) -> dict:
        """
        Get summary information for a social category.

        :param str category: Provide the category to get details for. A category must be all lower case and can only
                             include letters, numbers, and spaces. A category is the aggregation of all posts for all
                             topics within the category.
        """
        return self._request(f'/public/category/{category}/v1')

    def get_category_topics(self, category: str) -> dict:
        """
        Get the top topics for a social category.

        :param str category: Provide the topic to get details for. A topic must be all lower case and can only include
                             letters, numbers, spaces, # and $.
        """
        return self._request(f'/public/category/{category}/topics/v1')

    def get_category_time_series(self, category: str, bucket: str = None, interval: str = None,
                                  start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get historical time series data for a social category.

        :param str category: Provide the category to get details for. A category must be all lower case and can only
                             include letters, numbers, and spaces.
        :param str bucket: bucket time series data into hours or days. default is hours.
        :param str interval: Use interval to specify the start and end time automatically for convenience.
                             If "start" or "end" parameters are provided this parameter is ignored.
        :param datetime.datetime start: The start time (unix timestamp) to go back to.
        :param datetime.datetime end: The end time (unix timestamp) to stop at.
        """
        return self._request(f'/public/category/{category}/time-series/v1',
                             bucket=bucket, interval=interval, start=start, end=end)

    def get_category_posts(self, category: str, start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get the top posts for a social topic. If start time is provided the result will be the top posts by
        interactions for the time range. If start is not provided it will be the most recent top posts by
        interactions from the last 24 hours.

        :param str category: Provide the category to get details for. A category must be all lower case and can only
                             include letters, numbers, and spaces.
        :param datetime.datetime start: The start time (unix timestamp) to start at. Will be rounded to the beginning
                                        of the day. If the end parameter is not provided it will just be the top posts
                                        for this day.
        :param datetime.datetime end: (Optional) The end time (unix timestamp) to stop at. Will be rounded to the end
                                      of the day.
        """
        return self._request(f'/public/category/{category}/posts/v1', start=start, end=end)

    def get_category_news(self, category: str) -> dict:
        """
        Get the top news posts for a category. Top news is determined by the metrics related to the social posts that
        mention the news posts.

        :param str category: Provide the category to get details for. A category must be all lower case and can only
                             include letters, numbers, and spaces.
        """
        return self._request(f'/public/category/{category}/news/v1')

    def get_category_creators(self, category: str) -> dict:
        """
        Get the top creators for a social category.

        :param str category: Provide the category to get details for. A category must be all lower case and can only
                             include letters, numbers, and spaces.
        """
        return self._request(f'/public/category/{category}/creators/v1')

    def get_categories_list(self) -> dict:
        """
        Get a list of trending social categories.
        """
        return self._request('/public/categories/list/v1')

    # Creators endpoints
    def get_creators_list(self) -> dict:
        """
        Get a list of trending social creators over all of social based on interactions. To get lists of creators by
        category or topic see the topics and categories endpoints.
        """
        return self._request('/public/creators/list/v1')

    def get_creator(self, network: str, id: str) -> dict:
        """
        Get detail information on a specific creator.

        :param str network: Provide the network for the creator. One of twitter, youtube, instagram, reddit, or tiktok
        :param str id: Provide the unique ID or screen name of the creator
        """
        return self._request(f'/public/creator/{network}/{id}/v1')

    def get_creator_time_series(self, network: str, id: str, bucket: str = None, interval: str = None,
                                start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get time series data on a creator.

        :param str network: Influencer social network
        :param str id: The unique id or screen name of the creator
        :param str bucket: bucket time series data into hours or days. default is hours.
        :param str interval: Use interval to specify the start and end time automatically for convenience.
                             If "start" or "end" parameters are provided this parameter is ignored.
        :param datetime.datetime start: The start time (unix timestamp) to go back to.
        :param datetime.datetime end: The end time (unix timestamp) to stop at.
        """
        return self._request(f'/public/creator/{network}/{id}/time-series/v1',
                             bucket=bucket, interval=interval, start=start, end=end)

    def get_creator_posts(self, network: str, id: str, start: datetime.datetime = None,
                          end: datetime.datetime = None) -> dict:
        """
        Get the top posts for a specific creator.

        :param str network: Network for the creator. One of twitter, youtube, instagram, reddit, or tiktok
        :param str id: Unique ID or screen name of the creator
        :param datetime.datetime start: The start time (unix timestamp) to start at. Will be rounded to the beginning
                                        of the day. If the end parameter is not provided it will just be the top posts
                                        for this day.
        :param datetime.datetime end: (Optional) The end time (unix timestamp) to stop at. Will be rounded to the end
                                      of the day.
        """
        return self._request(f'/public/creator/{network}/{id}/posts/v1', start=start, end=end)

    # Posts endpoints
    def get_post(self, post_type: str, post_id: str) -> dict:
        """
        Get details of a post.

        :param str post_type: The post type e.g. tweet, youtube-video, tiktok-video, reddit-post, instagram-post
        :param str post_id: The unique id of a post, for twitter it is a number, youtube it is the id in the url
                            after watch?v=, look in the url for the unique id
        """
        return self._request(f'/public/posts/{post_type}/{post_id}/v1')

    def get_post_time_series(self, post_type: str, post_id: str) -> dict:
        """
        Get interactions over time for a post. If a post is older than 365 days the time series will be returned as
        daily interactions, otherwise it hourly interactions.

        :param str post_type: The post type e.g. tweet, youtube-video, tiktok-video, reddit-post, instagram-post
        :param str post_id: The unique id of a post, for twitter it is a number, youtube it is the id in the url
                            after watch?v=, look in the url for the unique id
        """
        return self._request(f'/public/posts/{post_type}/{post_id}/time-series/v1')

    # Coins endpoints
    def get_coins_list_v2(self, sort: str = None, filter: str = None, limit: int = None,
                          desc: bool = None, page: int = None) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. It is designed as a
        lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each
        other. Metrics include Galaxy Score™, AltRank™, price, volatility, 24h percent change, market cap, social
        mentions, social interactions, social contributors, social dominance, and categories.

        :param str sort: sort the output by metric
        :param str filter: filter by sub categories / sector from the "categories" key. Separate by commas for
                           multiple matches. Available sectors can be found on the sector filters at
                           https://lunarcrush.com/categories/cryptocurrencies
        :param int limit: limit the number of results. Default is 10 maximum is 1000 per page.
        :param bool desc: Pass any value as desc and the output will be reversed (descending)
        :param int page: When using limit, set the page of results to display, pages start at 0
        """
        return self._request('/public/coins/list/v2', sort=sort, filter=filter, limit=limit, desc=desc, page=page)

    def get_coins_list(self, sort: str = None, filter: str = None, limit: int = None,
                       desc: bool = None, page: int = None) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. This version is heavily
        cached and up to 1 hour behind. It is designed as a lightweight mechanism for monitoring the universe of
        available assets, either in aggregate or relative to each other. Use the coins/list/v2 endpoint for data
        updated every few seconds.

        :param str sort: sort the output by metric
        :param str filter: filter by sub categories / sector from the "categories" key. Separate by commas for
                           multiple matches. Available sectors can be found on the sector filters at
                           https://lunarcrush.com/categories/cryptocurrencies
        :param int limit: limit the number of results. Default is 10 maximum is 1000 per page.
        :param bool desc: Pass any value as desc and the output will be reversed (descending)
        :param int page: When using limit, set the page of results to display, pages start at 0
        """
        return self._request('/public/coins/list/v1', sort=sort, filter=filter, limit=limit, desc=desc, page=page)

    def get_coin(self, coin: str or int) -> dict:
        """
        Get market data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol
        of the coin in the input parameter, which can be found by calling the /coins/list endpoint.

        :param str or int coin: provide the numeric id or symbol of the coin or token.
        """
        return self._request(f'/public/coins/{coin}/v1')

    def get_coin_time_series(self, coin: str or int, bucket: str = None, interval: str = None,
                             start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get market time series data on a coin or token. Specify the coin to be queried by providing the numeric ID or
        the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.

        :param str or int coin: provide the numeric id or symbol of the coin or token.
        :param str bucket: bucket time series data into hours or days. default is hours.
        :param str interval: Use interval to specify the start and end time automatically for convenience.
                             If "start" or "end" parameters are provided this parameter is ignored.
        :param datetime.datetime start: The start time (unix timestamp) to go back to.
        :param datetime.datetime end: The end time (unix timestamp) to stop at.
        """
        return self._request(f'/public/coins/{coin}/time-series/v2',
                             bucket=bucket, interval=interval, start=start, end=end)

    def get_coin_meta(self, coin: str or int) -> dict:
        """
        Get meta information for a cryptocurrency project. This includes information such as the website, social media
        links, and other information.

        :param str or int coin: provide the numeric id or symbol of the coin or token.
        """
        return self._request(f'/public/coins/{coin}/meta/v1')

    # Stocks endpoints
    def get_stocks_list_v2(self, sort: str = None, filter: str = None, limit: int = None,
                           desc: bool = None, page: int = None) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked stocks. It is designed as a
        lightweight mechanism for monitoring the universe of available assets.

        :param str sort: sort the output by metric
        :param str filter: filter by sub categories / sector from the "categories" key. Separate by commas for
                           multiple matches.
        :param int limit: limit the number of results. Default is 10 maximum is 1000 per page.
        :param bool desc: Pass any value as desc and the output will be reversed (descending)
        :param int page: When using limit, set the page of results to display, pages start at 0
        """
        return self._request('/public/stocks/list/v2', sort=sort, filter=filter, limit=limit, desc=desc, page=page)

    def get_stocks_list(self, sort: str = None, filter: str = None, limit: int = None,
                        desc: bool = None, page: int = None) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked stocks. This version is heavily
        cached and up to 1 hour behind.

        :param str sort: sort the output by metric
        :param str filter: filter by sub categories / sector from the "categories" key. Separate by commas for
                           multiple matches.
        :param int limit: limit the number of results. Default is 10 maximum is 1000 per page.
        :param bool desc: Pass any value as desc and the output will be reversed (descending)
        :param int page: When using limit, set the page of results to display, pages start at 0
        """
        return self._request('/public/stocks/list/v1', sort=sort, filter=filter, limit=limit, desc=desc, page=page)

    def get_stock(self, stock: str or int) -> dict:
        """
        Get market data on a stock. Specify the stock to be queried by providing the numeric ID or the symbol
        of the stock in the input parameter.

        :param str or int stock: provide the numeric id or symbol of the stock.
        """
        return self._request(f'/public/stocks/{stock}/v1')

    def get_stock_time_series(self, stock: str or int, bucket: str = None, interval: str = None,
                              start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get market time series data on a stock.

        :param str or int stock: provide the numeric id or symbol of the stock.
        :param str bucket: bucket time series data into hours or days. default is hours.
        :param str interval: Use interval to specify the start and end time automatically for convenience.
                             If "start" or "end" parameters are provided this parameter is ignored.
        :param datetime.datetime start: The start time (unix timestamp) to go back to.
        :param datetime.datetime end: The end time (unix timestamp) to stop at.
        """
        return self._request(f'/public/stocks/{stock}/time-series/v2',
                             bucket=bucket, interval=interval, start=start, end=end)

    # NFTs endpoints
    def get_nfts_list_v2(self, sort: str = None, filter: str = None, limit: int = None,
                         desc: bool = None, page: int = None) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked NFT collections.

        :param str sort: sort the output by metric
        :param str filter: filter by sub categories / sector from the "categories" key. Separate by commas for
                           multiple matches.
        :param int limit: limit the number of results. Default is 10 maximum is 1000 per page.
        :param bool desc: Pass any value as desc and the output will be reversed (descending)
        :param int page: When using limit, set the page of results to display, pages start at 0
        """
        return self._request('/public/nfts/list/v2', sort=sort, filter=filter, limit=limit, desc=desc, page=page)

    def get_nfts_list(self, sort: str = None, filter: str = None, limit: int = None,
                      desc: bool = None, page: int = None) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked NFT collections. This version is
        heavily cached and up to 1 hour behind.

        :param str sort: sort the output by metric
        :param str filter: filter by sub categories / sector from the "categories" key. Separate by commas for
                           multiple matches.
        :param int limit: limit the number of results. Default is 10 maximum is 1000 per page.
        :param bool desc: Pass any value as desc and the output will be reversed (descending)
        :param int page: When using limit, set the page of results to display, pages start at 0
        """
        return self._request('/public/nfts/list/v1', sort=sort, filter=filter, limit=limit, desc=desc, page=page)

    def get_nft(self, nft: str or int) -> dict:
        """
        Get data on an NFT collection.

        :param str or int nft: provide the numeric id or symbol of the NFT collection.
        """
        return self._request(f'/public/nfts/{nft}/v1')

    def get_nft_time_series_v2(self, nft: str or int, bucket: str = None) -> dict:
        """
        Get time series data on an NFT collection.

        :param str or int nft: provide the numeric id or symbol of the NFT collection.
        :param str bucket: Leave blank (default) for the most week aggregated by hour, specify hour for full historical
                           data available in hourly aggregation, specify day for full historical data available in
                           daily aggregation.
        """
        return self._request(f'/public/nfts/{nft}/time-series/v2', bucket=bucket)

    def get_nft_time_series(self, nft: str or int, bucket: str = None, interval: str = None,
                            start: datetime.datetime = None, end: datetime.datetime = None) -> dict:
        """
        Get time series data on an NFT collection.

        :param str or int nft: provide the numeric id or symbol of the NFT collection.
        :param str bucket: bucket time series data into hours or days. default is hours.
        :param str interval: Use interval to specify the start and end time automatically for convenience.
                             If "start" or "end" parameters are provided this parameter is ignored.
        :param datetime.datetime start: The start time (unix timestamp) to go back to.
        :param datetime.datetime end: The end time (unix timestamp) to stop at.
        """
        return self._request(f'/public/nfts/{nft}/time-series/v1',
                             bucket=bucket, interval=interval, start=start, end=end)

    # Searches endpoints
    def search(self, term: str = None, search_json: str = None) -> dict:
        """
        Get recently popular social posts matching a single search term or phrase.

        :param str term: Test a single search term or phrase
        :param str search_json: A JSON object (stringified) that defines the search criteria
        """
        return self._request('/public/searches/search', term=term, search_json=search_json)

    def get_searches_list(self) -> dict:
        """
        Get a list of saved searches.
        """
        return self._request('/public/searches/list')

    def create_search(self, name: str, search_json: str, priority: bool = None) -> dict:
        """
        Create a custom search aggregation of topics and search terms.

        :param str name: The name of the custom search aggregation
        :param str search_json: A JSON object (stringified) that defines the search criteria
        :param bool priority: Flag as a high priority search aggregation
        """
        return self._request('/public/searches/create', name=name, search_json=search_json, priority=priority)

    def update_search(self, slug: str, name: str = None, search_json: str = None) -> dict:
        """
        Update a custom search aggregation name or priority. Search terms and configuration cannot be changed once created.

        :param str slug: The ID of the custom search aggregation to update
        :param str name: The new name of the search
        :param str search_json: A JSON object (stringified) that defines the search criteria
        """
        return self._request(f'/public/searches/{slug}/update', name=name, search_json=search_json)

    def delete_search(self, slug: str) -> dict:
        """
        Delete a custom search aggregation.

        :param str slug: The ID of the custom search aggregation to delete
        """
        return self._request(f'/public/searches/{slug}/delete')

    def get_searches(self, slug: str) -> dict:
        """
        See the summary output of a custom search aggregation.
        
        :param str slug: The ID of the custom search aggregation to view.
        """
        return self._request(f'/public/searches/{slug}')

    # Systems endpoints
    def get_system_changes(self) -> dict:
        """
        Get recent system changes.
        """
        return self._request('/public/system/changes')