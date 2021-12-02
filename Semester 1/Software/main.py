#this function will make a get request to the api and return the data, use a common user agent and make it appear like a real user
def get_data(url):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response

print(get_data('https://www.argos.co.uk/product/9462539'))