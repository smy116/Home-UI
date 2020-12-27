import requests
from cache import cache
from config import config
import json, time


class caiyun():
    cache = cache()
    key = config().CAIYUN_KEY
    local = "112.9583,28.2329"  #金域国际

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

    alert = {
        "0101": ["台风蓝色预警", "/img/icon-alert/0101.png"],
        "0201": ["暴雨蓝色预警", "/img/icon-alert/0201.png"],
        "0301": ["暴雪蓝色预警", "/img/icon-alert/0301.png"],
        "0401": ["寒潮蓝色预警", "/img/icon-alert/0401.png"],
        "0501": ["大风蓝色预警", "/img/icon-alert/0501.png"],
        "0601": ["沙尘暴蓝色预警", "/img/icon-alert/0601.png"],
        "0701": ["高温蓝色预警", "/img/icon-alert/0701.png"],
        "0801": ["干旱蓝色预警", "/img/icon-alert/0801.png"],
        "0901": ["雷电蓝色预警", "/img/icon-alert/0901.png"],
        "1001": ["冰雹蓝色预警", "/img/icon-alert/1001.png"],
        "1101": ["霜冻蓝色预警", "/img/icon-alert/1101.png"],
        "1201": ["大雾蓝色预警", "/img/icon-alert/1201.png"],
        "1301": ["霾蓝色预警", "/img/icon-alert/1301.png"],
        "1401": ["道路结冰蓝色预警", "/img/icon-alert/1401.png"],
        "1501": ["森林火灾蓝色预警", "/img/icon-alert/1501.png"],
        "1601": ["雷雨大风蓝色预警", "/img/icon-alert/1601.png"],
        "0102": ["台风黄色预警", "/img/icon-alert/0102.png"],
        "0202": ["暴雨黄色预警", "/img/icon-alert/0202.png"],
        "0302": ["暴雪黄色预警", "/img/icon-alert/0302.png"],
        "0402": ["寒潮黄色预警", "/img/icon-alert/0402.png"],
        "0502": ["大风黄色预警", "/img/icon-alert/0502.png"],
        "0602": ["沙尘暴黄色预警", "/img/icon-alert/0602.png"],
        "0702": ["高温黄色预警", "/img/icon-alert/0702.png"],
        "0802": ["干旱黄色预警", "/img/icon-alert/0802.png"],
        "0902": ["雷电黄色预警", "/img/icon-alert/0902.png"],
        "1002": ["冰雹黄色预警", "/img/icon-alert/1002.png"],
        "1102": ["霜冻黄色预警", "/img/icon-alert/1102.png"],
        "1202": ["大雾黄色预警", "/img/icon-alert/1202.png"],
        "1302": ["霾黄色预警", "/img/icon-alert/1302.png"],
        "1402": ["道路结冰黄色预警", "/img/icon-alert/1402.png"],
        "1502": ["森林火灾黄色预警", "/img/icon-alert/1502.png"],
        "1602": ["雷雨大风黄色预警", "/img/icon-alert/1602.png"],
        "0103": ["台风橙色预警", "/img/icon-alert/0103.png"],
        "0203": ["暴雨橙色预警", "/img/icon-alert/0203.png"],
        "0303": ["暴雪橙色预警", "/img/icon-alert/0303.png"],
        "0403": ["寒潮橙色预警", "/img/icon-alert/0403.png"],
        "0503": ["大风橙色预警", "/img/icon-alert/0503.png"],
        "0603": ["沙尘暴橙色预警", "/img/icon-alert/0603.png"],
        "0703": ["高温橙色预警", "/img/icon-alert/0703.png"],
        "0803": ["干旱橙色预警", "/img/icon-alert/0803.png"],
        "0903": ["雷电橙色预警", "/img/icon-alert/0903.png"],
        "1003": ["冰雹橙色预警", "/img/icon-alert/1003.png"],
        "1103": ["霜冻橙色预警", "/img/icon-alert/1103.png"],
        "1203": ["大雾橙色预警", "/img/icon-alert/1203.png"],
        "1303": ["霾橙色预警", "/img/icon-alert/1303.png"],
        "1403": ["道路结冰橙色预警", "/img/icon-alert/1403.png"],
        "1503": ["森林火灾橙色预警", "/img/icon-alert/1503.png"],
        "1603": ["雷雨大风橙色预警", "/img/icon-alert/1603.png"],
        "0104": ["台风红色预警", "/img/icon-alert/0104.png"],
        "0204": ["暴雨红色预警", "/img/icon-alert/0204.png"],
        "0304": ["暴雪红色预警", "/img/icon-alert/0304.png"],
        "0404": ["寒潮红色预警", "/img/icon-alert/0404.png"],
        "0504": ["大风红色预警", "/img/icon-alert/0504.png"],
        "0604": ["沙尘暴红色预警", "/img/icon-alert/0604.png"],
        "0704": ["高温红色预警", "/img/icon-alert/0704.png"],
        "0804": ["干旱红色预警", "/img/icon-alert/0804.png"],
        "0904": ["雷电红色预警", "/img/icon-alert/0904.png"],
        "1004": ["冰雹红色预警", "/img/icon-alert/1004.png"],
        "1104": ["霜冻红色预警", "/img/icon-alert/1104.png"],
        "1204": ["大雾红色预警", "/img/icon-alert/1204.png"],
        "1304": ["霾红色预警", "/img/icon-alert/1304.png"],
        "1404": ["道路结冰红色预警", "/img/icon-alert/1404.png"],
        "1504": ["森林火灾红色预警", "/img/icon-alert/1504.png"],
        "1604": ["雷雨大风红色预警", "/img/icon-alert/1604.png"]
    }

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
            result = sources["result"]["alert"]["content"]

            #遍历添加预警图标
            for i in range(len(result)):
                result[i]["name"] = self.alert[result[i]["code"]][0]
                result[i]["icon"] = self.alert[result[i]["code"]][1]

            if cache == True:
                self.cache.save("weather_alert", result)
                pass
            return result
            pass
        #删除原有预警信息
        self.cache.save("weather_alert", None)
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
            self.cache.save("now_weather", result)
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
            self.cache.save("future_weather", result)
            pass
        return result


class bmap():
    cache = cache()
    key = config().BMAP_KEY

    def dest(self):

        # 金隅国际经纬度
        home_point = "28.238791,112.964822"
        # 泊富广场经纬度
        bf_point = "28.214646,112.99186"
        # 金茂大厦经纬度
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
        self.cache.save("arrive_time", arrive_time)

        return arrive_time


class route():
    cache = cache()
    #过滤智能家居设备MAC
    filter_list = config().ROUTE_MAC_Filter

    def get_all(self):
        #实例化session
        session = requests.session()
        #目标url
        url = 'http://192.168.99.1'

        form_data = {
            'luci_username': config().ROUTE_USER,
            'luci_password': config().ROUTE_PASS
        }

        #使用session发起请求
        response = session.post(url, data=form_data)

        if response.status_code == 200:

            r = session.get("http://192.168.99.1/cgi-bin/luci/?status=1")
            result = r.json()

            device_list = []

            #遍历剔除设备列表中的智能设备
            for i in range(len(result['leases'])):

                if result['leases'][i]["macaddr"] not in self.filter_list:
                    device_list.append(result['leases'][i])
                    pass

            result['leases'] = device_list

            self.cache.save("route_info", result)

            return result
            pass
        else:
            return False
            pass
