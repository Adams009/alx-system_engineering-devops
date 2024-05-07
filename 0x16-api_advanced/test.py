import requests

def number_of_subscribers(subreddit):
    # Construct the URL for the subreddit's API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Reddit API Test Client'}
    
    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response is successful (status code 200) and has valid JSON
    if response.status_code == 200 and 'json' in response.headers.get('Content-Type'):
        # Parse the JSON response
        data = response.json()
        
        # Extract the number of subscribers from the JSON data
        subscribers = data['data']['subscribers']
        
        # Return the number of subscribers
        return subscribers
    else:
        # If the subreddit is invalid or there is an error, return 0
        return 0

# Example usage:
subreddit = "learnprogramming"  # Change this to the subreddit you want to query
print(number_of_subscribers(subreddit))

