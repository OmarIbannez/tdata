# coding=utf-8
import json

import config
import requests

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept-Language": "fr;q=1, en;q=0.9, de;q=0.8, zh-Hans;q=0.7, zh-Hant;q=0.6, ja;q=0.5",
    "User-Agent": "Tinder/3.0.4 (iPhone; iOS 7.1; Scale/2.00)",
    "os_version": "700001",
    "Accept": "*/*",
    "platform": "ios",
    "Connection": "keep-alive",
    "app_version": "3",
    "Accept-Encoding": "gzip, deflate",
}


def get_auth_token():
    url = config.host + "/v2/auth/login/facebook"
    req = requests.post(
        url,
        headers=headers,
        data=json.dumps({"token": config.fb_access_token, "facebook_id": config.fb_user_id}),
    )
    try:
        tinder_auth_token = req.json()["data"]["api_token"]
        headers.update({"X-Auth-Token": tinder_auth_token})
        return tinder_auth_token
    except Exception as e:
        raise e


def get_recommendations():
    try:
        r = requests.get("https://api.gotinder.com/user/recs", headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e


def update_location(lat, lon):
    try:
        url = config.host + "/passport/user/travel"
        r = requests.post(
            url, headers=headers, data=json.dumps({"lat": lat, "lon": lon})
        )
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e


def reset_real_location():
    try:
        url = config.host + "/passport/user/reset"
        r = requests.post(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e


def like(person_id):
    try:
        url = config.host + "/like/%s" % person_id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e


def dislike(person_id):
    try:
        url = config.host + "/pass/%s" % person_id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e
