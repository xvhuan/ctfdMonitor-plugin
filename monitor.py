import json
import requests
from urllib import parse
from CTFd.utils.user import get_current_user


def Monitor(challenge_id):
    robot = "xxxx"
    group = "xxxx"
    domain = "192.168.137.106:8000"
    api = "1x.x5.2x.5x:9452"
    token = "xxxx"
    user_name = get_current_user().name
    acToken = "cff874aeb1b52d547a5833bba381c851c950bdf14cc113b052eae07cf5e7aeb8"
    aim = requests.get(url="http://{}/api/v1/challenges/".format(domain) + str(challenge_id) + "/solves",
                       headers={
                           "Authorization": "Token {}".format(acToken),
                           "Content-Type": "application/json"}).content.decode()
    json_aim = json.loads(aim)
    aim_name = requests.get(
        url="http://{}".format(domain) + "/api/v1/challenges/" + str(challenge_id),
        headers={
            "Authorization": "Token {}".format(acToken),
            "Content-Type": "application/json"}).content.decode()
    json_name = json.loads(aim_name)["data"]["name"]
    if len(json_aim["data"]) < 3:
        if len(json_aim["data"]) == 0:
            name = parse.quote("恭喜" + user_name + "拿下《" + json_name + "》一血！！！太强啦~")
            json_d = {"sessionKey": token, "target": int(group),
                    "messageChain": [{"type": "Plain", "text": parse.unquote(name)}]}
            requests.post(url="http://{}/sendGroupMessage".format(api), json=json_d)
        if len(json_aim["data"]) == 1:
            name = parse.quote("恭喜" + user_name + "拿下《" + json_name + "》二血！！太秀啦~")
            json_d = {"sessionKey": token, "target": int(group),
                    "messageChain": [{"type": "Plain", "text": parse.unquote(name)}]}
            requests.post(url="http://{}/sendGroupMessage".format(api), json=json_d)
        if len(json_aim["data"]) == 2:
            name = parse.quote("恭喜" + user_name + "拿下《" + json_name + "》三血！666")
            json_d = {"sessionKey": token, "target": int(group),
                    "messageChain": [{"type": "Plain", "text": parse.unquote(name)}]}
            requests.post(url="http://{}/sendGroupMessage".format(api), json=json_d)
        if 3 < len(json_aim["data"]) < 5:
            name = parse.quote("恭喜" + user_name + "拿下《" + json_name + "》，太强啦~")
            json_d = {"sessionKey": token, "target": int(group),
                    "messageChain": [{"type": "Plain", "text": parse.unquote(name)}]}
            requests.post(url="http://{}/sendGroupMessage".format(api), json=json_d)
