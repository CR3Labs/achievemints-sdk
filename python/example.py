import os
from achievemints import AchievemintsSDK, logger, pprint, json

# Setup SDK
key = os.environ.get('API_KEY')
sdk = AchievemintsSDK(api_key=key)

# Return a list of your games
resources = sdk.make_request('/game') # will send a GET request to the resources endpoint
logger.info("Get resources:\n{}".format(resources))

# Enable an integration
#  This ensures on-chain events are watched for a specific type of integration
# TBD: needs to be done in the UI

# create a subscription
# to listen to your game events
game_id = resources[0]['id']
subscription = sdk.subscribe(game_id)
for event in subscription.events():
        pprint.pprint(json.loads(event.data))
        