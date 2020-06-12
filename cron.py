
from cache import cache
from classs import caiyun,bmap
import time

print("update caiyun!")
caiyun = caiyun()
json = caiyun.get_json_data()
caiyun.get_alert(sources=json, cache=True)
caiyun.get_now_weather(sources=json, cache=True)
caiyun.get_futrue_weather(sources=json, cache=True)

print("update dest!")
bmap = bmap()
bmap.dest()

x = cache()
nowtime = time.time()
x.save("last_update",str(round(nowtime * 1000)))