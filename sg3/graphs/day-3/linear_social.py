import random
from collections import deque
import time

class Queue:
    def __init__(self):
        self.storage = deque()

    def size(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
            return self.storage.popleft()


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraphSlow(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i}')
        # Create friendships
        possible_friendships = []
        # Generate all possible friendship combinations
        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.lastID + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for the first N pairs of the list
        # N is determined by the formula numUsers * avgFriendships // 2
        # Need to divide by 2 because addFriendship creates two friendships
        for i in range(numUsers * avgFriendships // 2):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def populateGraph(self, numUsers, avgFriendships):
        """
        add two new variables to count the total number of friendships and the collisions
        pick 2 random numbers between 1 and the last user ID
        try to create that friendship
        if it succeeds (addFriendship returns True), increment the friendship counter
        if not, increment collisions
        keep repeating until the target number of friendships is created
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i}')
        # Create friendships
        target_friendships = numUsers * avgFriendships
        total_friendships = 0
        collisions = 0
        possible_friendships = []
        while total_friendships < target_friendships:
            # generate two random ids for a friend pair
            user_id = random.randint(1, self.lastID)
            friend_id = random.randint(1, self.lastID)
            # try to add the friendship
            if (self.addFriendship(user_id, friend_id)):
                total_friendships += 2
            else: 
                collisions += 1
        print(f'COLLISIONS: {collisions}')

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # add our starting user id to the queue
        q.enqueue([userID])
        # while our queue is not empty
        while q.size() > 0:
            # dequeue our first path
            path = q.dequeue()
            # grab the last id from our path
            current_id = path[-1]
            # if it has not been visited
            if current_id not in visited:
                # when we hit an unvisited user add them to the visited dictionary
                visited[current_id] = path
                # enqueue the paths to to each of its neighbors
                for neighbor in self.friendships[current_id]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    numUsers = 3000
    avgFriendships = 5
    start_time = time.time()
    sg.populateGraph(numUsers, avgFriendships)
    # print(sg.friendships)
    end_time = time.time()
    print (f"Linear runtime: {end_time - start_time} seconds")
    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraphSlow(numUsers, avgFriendships)
    end_time = time.time()
    print (f"Quadratic runtime: {end_time - start_time} seconds")
