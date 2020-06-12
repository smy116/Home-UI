from cache import cache
import json
x = cache()

result = {}
print(x.get("now_weather"))
result['now_weather'] = (x.get("now_weather")
result['future_weather'] = x.get("future_weather")
result['arrive_time'] = x.get("arrive_time")

result['last_update'] = x.get("last_update")

print(result)