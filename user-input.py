import requests
url = input("Please enter your URL: ")

# Request the above URL
r = requests.get(url)

# Inspect the returned status code
# print(r.status_code)

# Inspect the returned URL
# print(r.url)

# Inspect the history
# print(r.history)

# Show step-by-step history:
r.history

for i, response in enumerate(r.history, 1): 
	print(i,response.url,response.status_code)

print("Complete: ",r.url,r.status_code)

