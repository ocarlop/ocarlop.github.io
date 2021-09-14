from pathlib import Path
from mailchimp_marketing import Client

# print(Path('mailchimp.apikey').read_text())

mailchimp = Client()
mailchimp.set_config({
  "api_key": Path('mailchimp.apikey').read_text().replace('\n',''),
  "server": "us5"
})

response = mailchimp.ping.get()
print(response)

except ApiClientError as error:
  print(error)