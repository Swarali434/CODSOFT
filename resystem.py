# Sample user-item ratings data
user_ratings = {
    'User1': {'Movie1': 4, 'Movie2': 5, 'Movie3': 3, 'Movie4': 2},
    'User2': {'Movie1': 3, 'Movie2': 4, 'Movie3': 2, 'Movie4': 1},
    'User3': {'Movie1': 5, 'Movie2': 2, 'Movie3': 4, 'Movie4': 3},
    'User4': {'Movie1': 2, 'Movie2': 3, 'Movie3': 1, 'Movie4': 5},
}

# Function to calculate similarity between users
def cosine_similarity(user1_ratings, user2_ratings):
    common_movies = set(user1_ratings.keys()) & set(user2_ratings.keys())
    if len(common_movies) == 0:
        return 0  # No common items
    dot_product = sum(user1_ratings[movie] * user2_ratings[movie] for movie in common_movies)
    user1_norm = sum(rating ** 2 for rating in user1_ratings.values()) ** 0.5
    user2_norm = sum(rating ** 2 for rating in user2_ratings.values()) ** 0.5
    return dot_product / (user1_norm * user2_norm)

# Function to recommend items to a user
def recommend(user, user_ratings):
    # Calculate similarities between the target user and all other users
    similarities = {other_user: cosine_similarity(user_ratings[user], user_ratings[other_user]) 
                    for other_user in user_ratings if other_user != user}
    # Sort users by similarity in descending order
    sorted_users = sorted(similarities, key=similarities.get, reverse=True)
    # Find items that the user hasn't rated yet
    recommendations = {}
    for other_user in sorted_users:
        for movie in user_ratings[other_user]:
            if movie not in user_ratings[user]:
                if movie not in recommendations:
                    recommendations[movie] = similarities[other_user]
                else:
                    recommendations[movie] += similarities[other_user]
    # Sort recommendations by score in descending order
    sorted_recommendations = sorted(recommendations, key=recommendations.get, reverse=True)
    return sorted_recommendations

# Example usage
user = 'User1'
recommended_movies = recommend(user, user_ratings)
print(f"Recommended movies for {user}: {recommended_movies}")
