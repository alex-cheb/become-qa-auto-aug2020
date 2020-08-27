import requests

url = "http://0.0.0.0:5002"
sep = "/"

# Entry points for the homework
entry_points = ["query", "body", "headers"]

# Parameters to be sent
request_params = {"content-type":"json"}

# Create set od scripts that sends: 
# /headers, /query, /body requests with corresponding info


# Sends get request with given parameters and prints text of the response
def print_get_response(entry, par = ""):
    response = requests.get(entry, params = par)
    print(response.text)

# Sends post request and prints text of the response
def print_post_response(entry, par = ""):
    response = requests.post(entry)
    print(response.text)


print_get_response(sep.join((url, entry_points[0])), request_params)

print_post_response(sep.join((url, entry_points[1])))

print_get_response(sep.join((url, entry_points[2])))