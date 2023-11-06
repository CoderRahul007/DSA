# I had this interview question that need to recommend song
# Question:
# the historical data
# User 1 has liked A, B, C, D
# User 2 has liked A, C, D
# User 3 has liked B, C, E

# Now we have a user that liked C, D
# As user1 and user 2 both like C and D, so their liked song will be recommend.
# The system should recommend the user song A, B
# ( A should appear first, as user1 and user2 both liked A)

class SongDetails:
    def __init__(self , songId , likedUserIds ):
        self.songId = songId
        self.likedUserIds = likedUserIds

class UserDetails:
    def __init__(self , userId , songIds ):
        self.userId = userId
        self.songIds = songIds

