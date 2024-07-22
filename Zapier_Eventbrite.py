base_url = "https://www.eventbriteapi.com/v3/events/940135790457/attendees/{}/?token=LYA5DQXXE34VBSMWBGQB" 
ids = input_data["attendees_ids"].split(",")
emails = {}

urls = [base_url.format(att_id) for att_id in ids]

for url in urls:
    response = requests.get(url)
    data = response.json()
    email = data['profile']['email']
    if email in emails:
        emails[email] += 1
    else:
        emails[email] = 1

num_of_uniqe_email = len(emails.keys())
num_of_attendees = len(ids)

if num_of_uniqe_email == num_of_attendees:
    output = True
else:
    output = False

output = {"output":output}
