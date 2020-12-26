from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from cache import cache
from config import config
import json

app = FastAPI()


@app.get("/get_home_data")
def get_home_data():
    x = cache()

    result = {}

    result['DISPLAY_MODE'] = config().DISPLAY_MODE

    result['now_weather'] = x.get("now_weather")
    result['future_weather'] = x.get("future_weather")
    result['arrive_time'] = x.get("arrive_time")

    result['last_update'] = x.get("last_update")
    result['route_info'] = x.get("route_info")

    alert = x.get("weather_alert")

    if alert != None:
        result['weather_alert'] = alert
        pass

    return result


app.mount("/",
          StaticFiles(directory="static", html="index.html"),
          name="static")