from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from cache import cache
import json

app = FastAPI()


@app.get("/get_home_data")
def get_home_data():
    x = cache()

    result = {}

    result['now_weather'] = json.loads(x.get("now_weather"))
    result['future_weather'] = json.loads(x.get("future_weather"))
    result['arrive_time'] = json.loads(x.get("arrive_time"))

    result['last_update'] = x.get("last_update")

    return result


app.mount("/",
          StaticFiles(directory="static", html="index.html"),
          name="static")