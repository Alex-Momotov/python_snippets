import requests

# Status codes
#   2XX     OK
#   3XX     Redirect
#   4XX     Client errors - e.g. trying to access page that you don't have permission to view
#   5XX     Server error

# Authentication methods
# Basic-auth    Website requests username and password in a pop-up dialog. Programmatically, you provide username and password as part of request.

# ______________________________________________________________________________________________________________________
# Cheat sheet

# HTTP methods
requests.get('https://httpbin.org/')    # GET
requests.post('https://httpbin.org/')   # POST
requests.put('https://httpbin.org/')    # PUT
requests.delete('https://httpbin.org/') # DELETE

# Response object
resp = requests.get('https://httpbin.org/get')

resp.json()         # Python dict from json response
resp.text           # text of response      (use for HTLM, or json)
resp.content        # bytes of response     (use for images)

resp.headers        # Headers
resp.url            # URL that we requested

resp.status_code    # Status code
resp.ok             # Status code is less than 400 (redirect, or okay)

# URL Query Params
resp = requests.get('https://httpbin.org/get', params={'page': 5, 'count': 25})

# Request Body
resp = requests.get('https://httpbin.org/post', data={'username' : 'Alex', 'password' : 'testing'})

# Basic Auth
resp = requests.get('https://httpbin.org/basic-auth/alex/testing', auth=('alex', 'testing'))

# Timeout
resp = requests.get('https://httpbin.org/delay/4', timeout=2)       # Returns ReadTimeout if timeout reached

# ______________________________________________________________________________________________________________________
# Examples

# GET - query params
q_params = {'page': 5, 'count': 25}
resp = requests.get('https://httpbin.org/get', params=q_params)

resp.url            # our query params were added to the url we requested
print(resp.text)    # this particular website reflects back to us our query params



# GET image and save to .png file
resp = requests.get('https://imgs.xkcd.com/comics/python.png')
resp.content        # bytes of image
with open('learning_requests/python_comic.png', 'wb') as f:       # 'wb' since we're writing bytes
    f.write(resp.content)


# POST - with body
payload = {'username' : 'Alex', 'password' : 'testing'}
resp = requests.post('https://httpbin.org/post', data=payload)

print(resp.text)

