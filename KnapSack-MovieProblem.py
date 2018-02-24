"""
Suppose that you are a software engineer who is working on design of an inflight entertainment system with on-demand movie streaming. Users on longer flights like to start each movie right when their previous one ends, but they complain that the plane usually lands before they can see the ending. So you need to build a feature for choosing movies whose total runtimes will equal the exact flight length.
Your input is a flight duration (in minutes) and a list of movie lengths (in minutes). Your algorithm should return a boolean value indicating whether there is a set of movies such that their total length equals the flight duration.
You may assume that users will watch at most three movies during a flight. The algorithm should be as fast as possible.
"""


# Naive Recursive Approach with Knapsack Probelm

# Returns the maximum number of movies that can be watched in a flight duration time "time"
def knapSack(time, movieDurations, val, n):
    if n == 0 or time == 0:
        return 0
    if movieDurations[n - 1] > time:
        return knapSack(time, movieDurations, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(time - movieDurations[n - 1], movieDurations, val, n - 1),
                   knapSack(time, movieDurations, val, n - 1))


# Testing
def isMoviesFit(movieList, movieDurationList, flightDuration):
    n = len(movieList)
    maxMoviesPossible = knapSack(flightDuration, movieDurationsList, movieList, n)
    if maxMoviesPossible > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    movieList = [1, 1, 1]  # Total movies they want to watch =3
    movieDurationsList = [300, 400, 500]  # Set of movies in minutes
    flightDuration = 700  # Total flight duration in minutes
    if(isMoviesFit(movieList, movieDurationsList, flightDuration)):
        print('Yes, you can watch at least one movie completely in this duration')
    else:
        print('No, you cannot watch any movie completely in this duration')
        
