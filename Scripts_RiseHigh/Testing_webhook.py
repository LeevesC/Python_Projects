import requests

def send_email_to_webhook(email):
    # Define the webhook URL
    webhook_url = 'https://hooks.zapier.com/hooks/catch/19254774/22e8kae/'
    
    # Data to send in the POST request
    data = {
        "docId": email,
    }
    
    # Send the POST request to the webhook
    response = requests.post(webhook_url, json=data)
    
    # Print the response from the webhook
    if response.status_code == 200:
        print(f"Webhook executed successfully for {email}.")
        try:
            print("Response:", response.json())
        except ValueError:  # In case json decoding fails
            print("Response:", response.text)
    else:
        print(f"Failed to execute webhook for {email}.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)


send_email_to_webhook('1cpe9b-dS7cC7iKU6RJyFcLTypeaiolQMxdagM7RcVLk')
