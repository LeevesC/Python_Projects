import requests

# Your Eventbrite API token
api_token = 'QAC47QFYASR63LEKRI5N'
# Your Event ID
event_id = '767463803897'

# URL to get orders for the event
url = f'https://www.eventbriteapi.com/v3/events/{event_id}/orders/'

# Headers for authentication
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Make the GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    orders = response.json()['orders']
    cancelled_orders = [order for order in orders if order['status'] == 'canceled']
    # for order in cancelled_orders:
    #     print(f"Order ID: {order['id']}, Buyer: {order['email']}, Status: {order['status']}")
    print(len(orders))
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.text)
