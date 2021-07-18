import requests
#作业3  通过迭代器的天气抓取
class WeatherOutput:
    """输出天气信息"""
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        try:
            r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
            data = r.json()['data']['forecast'][0]
            return '{0}: {1}, {2}'.format(city, data['low'], data['high'])
        except:
            print("获取天气信息失败")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

for x in WeatherOutput(['北京', '上海', '武汉', '深圳']):
    print(x)
