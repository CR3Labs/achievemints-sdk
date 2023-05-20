# Achievemints SDK

## Unity SDK

The Unity SDK comes in the form of a Unity package. The Achievemints Unity SDK has everything needed to connect web3 via metamask or similar wallet to your Unity Game. 

**Unity SDK Setup**

**1. Change Build Settings to WebGL**

`File > Build Settings > WebGL > Build and Run`

**2. Change to Achievemints WebGL Template**

`Edit > Project Settings > Player > Resolution and Presentation > Achievemints-2020x`

**NOTE: It may be required to add the Newtonsoft.json package to your project**

`Package Manager Window > Add Package from GIT URL > com.unity.nuget.newtonsoft-json`

**3. Set required Web3 settings**

`Window > Achievemints Settings`

To obtain a `Game ID`, register at https://beta.achievemints.xyz.

## Python SDK

The Achievemints Python SDK is a simple client to handle interactions with https://beta.achievemints.xyz.

The Achievemints SDK is paired with the Achievemints Unity Package to enable Unity<>EVM interactions.
The primary use case is to retrieve information about your players blockchain interactions associated to your Unity game.

To obtain an API Key, register at https://beta.achievemints.xyz.

**See: example.py for example usage**

```python
# Setup SDK
key = os.environ.get('API_KEY')
sdk = AchievemintsSDK(api_key=key)

# Return a list of your games
games = sdk.make_request('/game') # will send a GET request to the games endpoint
logger.info("Get games:\n{}".format(games))

# Enable an integration
#  This ensures on-chain events are watched for a specific type of integration
# TODO: currently, this can only be accomplished in the UI

# create a subscription
# to listen to your game events
game_id = games[0]['id']
subscription = sdk.subscribe(game_id)
for event in subscription.events():
        pprint.pprint(json.loads(event.data))
```
