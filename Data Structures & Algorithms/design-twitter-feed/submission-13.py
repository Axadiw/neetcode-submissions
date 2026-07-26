class Tweet:
    def __init__(self, userId: int, tweetId: int):
        self.userId = userId
        self.tweetId = tweetId
    
    def __eq__(self, other):
        return (self.userId, self.tweetId) == (other.userId, other.tweetId)

    def __hash__(self):
        return hash((self.userId, self.tweetId))

class Twitter:
    def __init__(self):
        self.tweets = deque()
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft(Tweet(userId=userId, tweetId=tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followed_people = set(list((self.follows[userId] if userId in self.follows else [])))
        followed_people.add(userId)
        print(f"{userId} follows: {followed_people}")
        return [x.tweetId for x in self.tweets if x.userId in followed_people][:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.follows:
            self.follows[followerId] = set()
        
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
        
