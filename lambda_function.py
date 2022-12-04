import sys
sys.path.insert(1, './lib')
import json
from aocd.models import User
        
def lambda_handler(event, context):
    user = User(token='<SESSION>')
    stats = user.get_stats()
    results = []
    for key in stats:
        result = {}
        (year, day) = key
        result['year'] = year
        result['day'] = day
        result_stats = {}
        for part in stats[key]:
            result_stats[part] = stats[key][part]
            result_stats[part]['time'] = stats[key][part]['time'].total_seconds()
        result['result'] = result_stats
        results.append(result)

    # print(stats)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(results)
    }