import requests


#curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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

r = requests.post('https://hooks.slack.com/services/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', data = {'text':'Where is the sensor?'})
# from slackclient import SlackClient

# slack_token = "jEpNRpOqMLiyUWbJYJO7J96B"
# sc = SlackClient(slack_token)

# sc.api_call(
#   "chat.postMessage",
#   channel="slack_test",
#   text="New Message"
# )
