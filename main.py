from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from cache import cache
import json

app = FastAPI()


@app.get("/get_home_data")
def get_home_data():
    x = cache()

    result = {}

    result['now_weather'] = x.get("now_weather")
    result['future_weather'] = x.get("future_weather")
    result['arrive_time'] = x.get("arrive_time")

    result['last_update'] = x.get("last_update")

    alert = x.get("weather_alert")

    if alert != None:
        result['weather_alert'] = alert
        pass

    return result


app.mount("/",
          StaticFiles(directory="static", html="index.html"),
          name="static")