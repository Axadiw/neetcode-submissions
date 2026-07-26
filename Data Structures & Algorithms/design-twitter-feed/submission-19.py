class Tweet:
    def __init__(self, userId: int, tweetId: int, time: int):
        self.userId = userId
        self.tweetId = tweetId
        self.time=time
    
    def __eq__(self, other):
        return (self.userId, self.tweetId) == (other.userId, other.tweetId)

    def __lt__(self, other):
        return self.time > other.time    

    def __hash__(self):
        return hash((self.userId, self.tweetId))

    def __repr__(self):
        return f"time: {self.time} userId: {self.userId} tweetId: {self.tweetId}"

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.tweets:
            self.tweets[userId] = deque()

        self.tweets[userId].appendleft(Tweet(userId=userId, tweetId=tweetId, time=self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        followeds = set(list((self.follows[userId] if userId in self.follows else [])))
        followeds.add(userId)
        for followed_person in followeds:
            if followed_person in self.tweets:
                tweets.append(self.tweets[followed_person])

        return_tweets = []
        for tweets_from_single_person in tweets:
            for tweet in tweets_from_single_person:
                heapq.heappush(return_tweets, tweet)
        

        return [x.tweetId for x in heapq.nsmallest(10,return_tweets)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.follows:
            self.follows[followerId] = set()
        
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
        
