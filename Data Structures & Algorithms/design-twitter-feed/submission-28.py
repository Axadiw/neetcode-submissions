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
        # print('---getNewsFeed---')
        tweets = []
        followeds = set(list((self.follows[userId] if userId in self.follows else [])))
        followeds.add(userId)
        for followed_person in followeds:
            if followed_person in self.tweets:
                tweets.append([self.tweets[followed_person],0])
        # print(f'tweets: {tweets} followeds: {followeds} all tweets: {self.tweets}')
        return_tweets = []
        while len(return_tweets) < 10 and len(tweets) > 0:
            maximal_queue = None
            maximal_queue_idx = None
            for idx, tweets_from_single_person in enumerate(tweets):
                if not maximal_queue or tweets_from_single_person[0][tweets_from_single_person[1]].time > maximal_queue[0][maximal_queue[1]].time:
                    maximal_queue = tweets_from_single_person
                    maximal_queue_idx = idx
            
            
            if maximal_queue:
                # print(f"counters: {counters} maximal_queue_idx: {maximal_queue_idx}")
                tweet = maximal_queue[0][maximal_queue[1]]
                maximal_queue[1] += 1
                # print(f"adding tweet: {tweet} maximal_queue{maximal_queue}")
                if maximal_queue[1] > len(maximal_queue[0])-1:
                    # print(f"befr queue empty tweets {tweets}")
                    tweets.pop(maximal_queue_idx)
                    # print(f"aftr queue empty tweets {tweets}")

                heapq.heappush(return_tweets, tweet)
        

        return [x.tweetId for x in heapq.nsmallest(10,return_tweets)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.follows:
            self.follows[followerId] = set()
        
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
        
