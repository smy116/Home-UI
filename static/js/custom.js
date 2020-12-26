var app = new Vue({
    el: '#app',
    data: {
        commute_dest: "泊富广场",
        active_tab: "",
        map_dest_time: "",
        now_time: "",
        now_date: "",
        now_temp: "",
        now_weather: "",
        now_weather_icon: "",
        now_humidity: "",
        now_rain_description: "",
        alert_list: "",
        last_update: "",
        double_element: "",
        deivce_table_title: [{
                title: '设备名称',
                key: 'hostname'
            },
            {
                title: 'IP地址',
                key: 'ipaddr',
                width: 150
            },
            {
                title: 'MAC地址',
                key: 'macaddr',
                width: 150
            }
        ],
    }
})

var update_home = setInterval(update_home_data, 30000);

function update_home_data() {
    var json
    axios.get('/get_home_data')
        .then(function (response) {
            json = response.data;

            //实时天气
            app.now_temp = json['now_weather']['temperature'];
            app.now_weather = json['now_weather']['cnname'];
            app.now_humidity = json['now_weather']['humidity'];
            app.now_weather_icon = json['now_weather']['icon'];
            app.now_rain_description = json['now_weather']['rain_description'];

            //未来天气
            app.d1_icon = json["future_weather"][0]["icon"];
            app.d1_weather = json["future_weather"][0]["cnname"];
            app.d1_temp = json["future_weather"][0]["temperature"];

            app.d2_icon = json["future_weather"][1]["icon"];
            app.d2_weather = json["future_weather"][1]["cnname"];
            app.d2_temp = json["future_weather"][1]["temperature"];

            app.d3_icon = json["future_weather"][2]["icon"];
            app.d3_weather = json["future_weather"][2]["cnname"];
            app.d3_temp = json["future_weather"][2]["temperature"];

            app.d4_icon = json["future_weather"][3]["icon"];
            app.d4_weather = json["future_weather"][3]["cnname"];
            app.d4_temp = json["future_weather"][3]["temperature"];
            app.alert_list = json["weather_alert"];

            //预计到达时间
            app.arrive_bf = json['arrive_time']['bf'];
            app.arrive_xj = json['arrive_time']['xj'];

            //数据更新时间
            app.last_update = Number(json['last_update']);

            //设备在线列表
            app.deivce_table_data = json['route_info']['leases'];

            //切换显示模式
            double_MODE = document.getElementsByClassName("double_element");
            if (json['DISPLAY_MODE'] == "double") {
                app.double_element = {}
            } else {
                app.double_element = {
                    "display": 'none'
                }
            }

        });

}


var update_clock = setInterval(function () {
        var myDate = new Date;
        var year = myDate.getFullYear(); //获取当前年
        var mon = myDate.getMonth() + 1; //获取当前月
        var day = myDate.getDate(); //获取当前日
        var h = myDate.getHours(); //获取当前小时数(0-23)
        var m = myDate.getMinutes(); //获取当前分钟数(0-59)
        var s = myDate.getSeconds(); //获取当前秒'
        app.now_date = year + "年" + mon + "月" + day + "日";
        app.now_time = p(h) + ":" + p(m) + ":" + p(s);
    },
    1000);
var map
window.onload = function () {
    init_commute_map()
    update_home_data()
}

function init_commute_map() {
    if (app.active_tab != "commute") {
        return false
    }
    map = new BMap.Map("map-container", {
        enableBizAuthLogo: false,
        enableMapClick: false
    });

    var searchComplete = function (results) {

        var plan = results.getPlan(0).getDuration(false);

        var dest_time = new Date(new Date().getTime() + plan * 1000)
        app.map_dest_time = p(dest_time.getHours()) + ":" + p(dest_time.getMinutes());
    }

    map.centerAndZoom(new BMap.Point(112.964822, 28.238791), 14);

    map.addTileLayer(new BMap.TrafficLayer());

    var transit = new BMap.TransitRoute(map, {
        renderOptions: {
            map: map,
            autoViewport: true

        },
        TransitPolicy: BMAP_TRANSIT_POLICY_RECOMMEND,
        onSearchComplete: searchComplete,
    });
    if (app.commute_dest == "泊富广场") {
        var end = new BMap.Point(112.99186, 28.214646);
    } else {
        var end = new BMap.Point(112.91111, 28.202384);
    }

    var start = new BMap.Point(112.964822, 28.238791);


    transit.search(start, end);
}

//创建补0函数
function p(s) {
    return s < 10 ? '0' + s : s;
}