
# User ratings data
user_ratings = {
    'User1': {'Movie1': 4, 'Movie2': 5, 'Movie3': 3, 'Movie4': 2},
    'User2': {'Movie1': 3, 'Movie2': 4, 'Movie3': 2, 'Movie4': 1},
    'User3': {'Movie1': 5, 'Movie2': 2, 'Movie3': 4, 'Movie4': 3},
    'User4': {'Movie1': 2, 'Movie2': 3, 'Movie3': 1, 'Movie4': 5},
}

# Function to recommend movies to a user
def recommend_movies(user, user_ratings):
    similar_users = {}
    for other_user in user_ratings:
        if other_user != user:
            similarity_score = 0
            for movie in user_ratings[user]:
                if movie in user_ratings[other_user]:
                    similarity_score += user_ratings[user][movie] * user_ratings[other_user][movie]
            similar_users[other_user] = similarity_score
    recommended_users = sorted(similar_users, key=similar_users.get, reverse=True)
    return recommended_users

# Example usage
user = 'User1'
recommended_movies = recommend_movies(user, user_ratings)
print(f"Recommended movies for {user}: {recommended_movies}")
