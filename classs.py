import requests
from cache import cache
from config import config
import json, time


class caiyun():
    cache = cache()
    key = config().CAIYUN_KEY
    local = "112.9583,28.2329"

    skycon = {
        "CLEAR_DAY": ["晴", "/img/icon-weather/100d.png"],
        "CLEAR_NIGHT": ["晴", "/img/icon-weather/100n.png"],
        "PARTLY_CLOUDY_DAY": ["多云", "/img/icon-weather/101d.png"],
        "PARTLY_CLOUDY_NIGHT": ["多云", "/img/icon-weather/101n.png"],
        "CLOUDY": ["阴", "/img/icon-weather/104d.png"],
        "LIGHT_HAZE": ["轻度雾霾", "/img/icon-weather/502d.png"],
        "MODERATE_HAZE": ["中度雾霾", "/img/icon-weather/511d.png"],
        "HEAVY_HAZE": ["重度雾霾", "/img/icon-weather/512d.png"],
        "LIGHT_RAIN": ["小雨", "/img/icon-weather/305d.png"],
        "MODERATE_RAIN": ["中雨", "/img/icon-weather/306d.png"],
        "HEAVY_RAIN": ["大雨", "/img/icon-weather/307d.png"],
        "STORM_RAIN": ["暴雨", "/img/icon-weather/310d.png"],
        "FOG": ["雾", "/img/icon-weather/501d.png"],
        "LIGHT_SNOW": ["小雪", "/img/icon-weather/400d.png"],
        "MODERATE_SNOW": ["中雪", "/img/icon-weather/401d.png"],
        "HEAVY_SNOW": ["大雪", "/img/icon-weather/402d.png"],
        "STORM_SNOW": ["暴雪", "/img/icon-weather/403d.png"],
        "DUST": ["浮尘", "/img/icon-weather/504d.png"],
        "SAND": ["沙尘", "/img/icon-weather/507d.png"],
        "WIND": ["大风", "/img/icon-weather/207d.png"]
    }

    #local = "109.9578,27.5406"

    #获取数据
    def get_json_data(self):
        r = requests.get('https://api.caiyunapp.com/v2.5/' + self.key + '/' +
                         self.local + '/weather.json?alert=true')
        if r.status_code != 200:
            return false
            pass
        return r.json()

    #获取预警信息
    def get_alert(self, sources=None, cache=True):
        if sources == None:
            r = requests.get('https://api.caiyunapp.com/v2.5/' + self.key +
                             '/' + self.local + '/weather.json?alert=true')
            if r.status_code != 200:
                return false
                pass
            sources = r.json()
            pass

        #判断是否有预警信息
        if sources["result"]["alert"]["content"]:
            #有预警信息
            result = sources["result"]["alert"]["content"][0]
            if cache == True:
                self.cache.save("weather_alert", json.dumps(result))
                pass
            return result
            pass

        return False

    #获取实时天气数据
    def get_now_weather(self, sources=None, cache=True):
        if sources == None:
            r = requests.get('https://api.caiyunapp.com/v2.5/' + self.key +
                             '/' + self.local + '/weather.json?alert=true')
            if r.status_code != 200:
                return false
                pass
            sources = r.json()
            pass
        result = sources["result"]["realtime"]
        result["cnname"] = self.skycon[result["skycon"]][0]
        result["icon"] = self.skycon[result["skycon"]][1]
        result["humidity"] = format(result["humidity"], '.0%')
        result["temperature"] = str(round(result["temperature"])) + "°"
        result["rain_description"] = sources["result"]["minutely"][
            "description"]

        if cache == True:
            self.cache.save("now_weather", json.dumps(result))
            pass
        return result

    #获取未来天气预报数据
    def get_futrue_weather(self, sources=None, cache=True):
        if sources == None:
            r = requests.get('https://api.caiyunapp.com/v2.5/' + self.key +
                             '/' + self.local + '/weather.json?alert=true')
            if r.status_code != 200:
                return false
                pass
            sources = r.json()
            pass
        temperature = sources["result"]["daily"]["temperature"]
        skycon = sources["result"]["daily"]["skycon"]

        result = [
            {
                "temperature":
                str(round(temperature[0]["min"])) + "°~" +
                str(round(temperature[0]["max"])) + "°",
                "cnname":
                self.skycon[skycon[0]["value"]][0],
                "icon":
                self.skycon[skycon[0]["value"]][1]
            },
            {
                "temperature":
                str(round(temperature[1]["min"])) + "°~" +
                str(round(temperature[1]["max"])) + "°",
                "cnname":
                self.skycon[skycon[1]["value"]][0],
                "icon":
                self.skycon[skycon[1]["value"]][1]
            },
            {
                "temperature":
                str(round(temperature[2]["min"])) + "°~" +
                str(round(temperature[2]["max"])) + "°",
                "cnname":
                self.skycon[skycon[2]["value"]][0],
                "icon":
                self.skycon[skycon[2]["value"]][1]
            },
            {
                "temperature":
                str(round(temperature[3]["min"])) + "°~" +
                str(round(temperature[3]["max"])) + "°",
                "cnname":
                self.skycon[skycon[3]["value"]][0],
                "icon":
                self.skycon[skycon[3]["value"]][1]
            },
        ]

        if cache == True:
            self.cache.save("future_weather", json.dumps(result))
            pass
        return result


class bmap():
    cache = cache()
    key = config().BMAP_KEY

    def dest(self):
        home_point = "28.238791,112.964822"
        bf_point = "28.214646,112.99186"
        xj_point = "28.202384,112.91111"

        #泊富预计时间
        payload1 = {
            'origin': home_point,
            'destination': bf_point,
            'ak': self.key,
            'tactics_incity': 0,
            'page_size': 1
        }

        r = requests.get("http://api.map.baidu.com/direction/v2/transit",
                         params=payload1)
        if r.status_code != 200:
            return false
            pass
        result = r.json()
        arrive_time = {}
        struct_time = time.strptime(
            result['result']['routes'][0]['arrive_time'], "%Y-%m-%d %H:%M:%S")
        arrive_time['bf'] = time.strftime('%H:%M', struct_time)

        #湘江集团预计时间
        payload2 = {
            'origin': home_point,
            'destination': xj_point,
            'ak': self.key,
            'tactics_incity': 0,
            'page_size': 1
        }

        r = requests.get("http://api.map.baidu.com/direction/v2/transit",
                         params=payload2)
        if r.status_code != 200:
            return false
            pass
        result = r.json()
        struct_time = time.strptime(
            result['result']['routes'][0]['arrive_time'], "%Y-%m-%d %H:%M:%S")
        arrive_time['xj'] = time.strftime('%H:%M', struct_time)
        self.cache.save("arrive_time", json.dumps(arrive_time))

        return arrive_time
