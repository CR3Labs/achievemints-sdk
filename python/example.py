import os
from achievemints import AchievemintsSDK, logger, pprint, json

# Setup SDK
key = os.environ.get('API_KEY')
sdk = AchievemintsSDK(api_key=key)

# Return a list of your games
resources = sdk.make_request('/game') # will send a GET request to the resources endpoint
logger.info("Get resources:\n{}".format(resources))

# Add a player to a game
#  This ensures on-chain events are watched for this player/game combination
game_id = resources[0]['id']
player = sdk.make_request('/game/{}/player'.format(game_id), method="POST", body={"wallet": "0x0"})

# create a subscription
# to listen to your game events
subscription = sdk.subscribe("fdd74c25-e7bf-42da-b6e7-d4b5f9ec95d1")
for event in subscription.events():
        pprint.pprint(json.loads(event.data))