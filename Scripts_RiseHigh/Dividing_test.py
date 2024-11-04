import requests

url = 'https://pdf-temp-files.s3.us-west-2.amazonaws.com/TKKPKP3IBVH0Q7C2ZESX1DBQO99YV4GK/U4FPl-o_eESMZD7WTnCqtg.txt?X-Amz-Expires=3600&X-Amz-Security-Token=FwoGZXIvYXdzEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDDoKYWh67s%2FBnu7a0yKCAdQBPVtKeZeISOuV1TgAgDvwzhh4JH3qdMRV91Nf5eRCtu8of6XDgd0u2UfqHQD2F6CEI7dj9QidRXTGl4FXUMCKbMk69Fuv%2BFtn8H8DxfEa9H0yhgE4BiPwFy0farHqUJ1aFklq9HsGraYoGteLwUe2%2FmO7HiiE8zkqZqOw7PGy8kool9nvtQYyKGM11qkKCjt1IZoPu9pypBx4b1B%2BdCdfTSb6hMxPYNDK6j%2BSpRDLPIc%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA4NRRSZPHHM744572/20240814/us-west-2/s3/aws4_request&X-Amz-Date=20240814T034935Z&X-Amz-SignedHeaders=host&X-Amz-Signature=2c9bc3a983d100e6450b14fa7812080370d96225be9fa1a5c6d062631561000d'

response = requests.get(url)
text_content = response.text

# divided into three segments
markers = ['$278,170.00', 'Confirming Your Ability to Meet The New Loan Repayments', 'Reasons Why Lender and Product Was Selected', 'EMAIL TEMPLATES']
segments = {}
positions = {marker: text_content.find(marker) for marker in markers}

segments['loan_details'] = text_content[positions['$278,170.00'] + len('$278,170.00'):positions['Confirming Your Ability to Meet The New Loan Repayments']].strip()
cache = text_content[positions['Confirming Your Ability to Meet The New Loan Repayments'] + len('Confirming Your Ability to Meet The New Loan Repayments'):positions['Reasons Why Lender and Product Was Selected']].strip()
segments['reasons'] = text_content[positions['Reasons Why Lender and Product Was Selected'] + len('Reasons Why Lender and Product Was Selected'):positions['EMAIL TEMPLATES']].strip()

# divided cache into three segments
cache_markers = ['Living Expenses', 'Fees and Charges']
cache_positions = {cache_marker: cache.find(cache_marker) for cache_marker in cache_markers}
segments['confirming_ability'] = cache[:cache_positions['Living Expenses']].strip()
segments['living_expenses'] = cache[cache_positions['Living Expenses'] + len('Living Expenses'):cache_positions['Fees and Charges']].strip()
segments['fees_charge'] = cache[cache_positions['Fees and Charges'] + len('Fees and Charges'):].strip()

print(segments)