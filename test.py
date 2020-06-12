from cache import cache
import json
x = cache()

result = {}
print(x.get("now_weather"))
result['now_weather'] = json.loads(x.get("now_weather"))
result['future_weather'] = json.loads(x.get("future_weather"))
result['arrive_time'] = json.loads(x.get("arrive_time"))

result['last_update'] = x.get("last_update")

print(result)