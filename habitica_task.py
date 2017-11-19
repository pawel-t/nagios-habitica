import requests
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', help='host name', required=True)
parser.add_argument('-A', '--alarm', help='alarm name', required=True)
parser.add_argument('-SS', '--servicestate', help='service state')
parser.add_argument('-SST', '--servicestatetype', help='service state type')

args = parser.parse_args()


if args.servicestate == "Critical" and agrs.servicestatetype == "HARD":
    headers = {"Content-Type":"application/json", "x-api-user": x-api-user, "x-api-key": x-api-key}
    #r = requests.get('https://habitica.com/api/v3/user', headers=headers)

    payload={'text': args.host + ": " + args.alarm , 'type': 'todo'}
    todo = requests.post("https://habitica.com/api/v3/tasks/user", headers=headers, data=json.dumps(payload))
