import time

from tcollector.models import Human

import tinder_api

tinder_api.get_auth_token()
LOCATIONS = [
    {
        "lat": "48.8589507",
        "lon": "2.2770205",
        "label": "Paris (48.8589507, 2.2770205)",
        "visited": True,
    },
]
LIKE_SLEEP_TIME = 10
EXISTS = 0
CURRENT_LOCATION = ""
loop = 0

while True:
    loop += 1
    print(loop)
    if EXISTS <= 0:
        if all([location["visited"] for location in LOCATIONS]):
            print("un-visiting locations...")
            for location in LOCATIONS:
                location["visited"] = False
        for location in LOCATIONS:
            if not location["visited"]:
                print("Moving to {0}".format(location["label"]))
                tinder_api.update_location(location["lat"], location["lon"])
                location["visited"] = True
                EXISTS = 5
                CURRENT_LOCATION = location["label"]
                break
    r = tinder_api.get_recommendations()
    try:
        recommendations = r["results"]
    except KeyError as e:
        print(r)
        raise e
    print("Fetching {0} recommendations".format(len(recommendations)))
    for recommendation in recommendations:
        recommendation["t_id"] = recommendation.pop("_id")
        try:
            Human.objects.get(t_id=recommendation["t_id"])
        except Human.DoesNotExist:
            try:
                human = Human(**recommendation)
            except Exception as e:
                raise e
            human.label = CURRENT_LOCATION
            human.save()
            tinder_api.like(human.t_id)
            print("Like {0}".format(human.name))
            print("Sleeping {0} seconds...".format(LIKE_SLEEP_TIME))
            time.sleep(LIKE_SLEEP_TIME)
        else:
            EXISTS -= 1
