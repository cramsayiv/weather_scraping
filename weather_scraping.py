import requests
from bs4 import BeautifulSoup

url = "https://weather.com/en-IN/weather/tenday/l/7236e98ce24e4d3e6cddf4483c624d1c0d70766a1a42c354605d12f5e275f48e"
try:
    my_page = requests.get(url)
except:
    print("Could not connect to " + url)
    exit()
soup = BeautifulSoup(my_page.text, 'html.parser')

all = soup.find("div", {"class": "locations-title ten-day-page-title"}).find("h1").text
table = soup.find_all("table", {"class": "twc-table"})
l = []
full_weekdays = {
                "Today" : "Today",
                "Mon": "Monday",
                "Tue": "Tuesday",
                "Wed": "Wednseday",
                "Thu": "Thursday",
                "Fri": "Friday",
                "Sat": "Saturday",
                "Sun": "Sunday"}
a_vs_an = {
    "10%": "a",
    "20%": "a",
    "30%": "a",
    "40%": "a",
    "50%": "a",
    "60%": "a",
    "70%": "a",
    "80%": "an",
    "90%": "a",
    "100%": "a"
}
for items in table:
    for i in range(len(items.find_all("tr")) - 1):
        d = {}
        d["day"] = items.find_all("span", {"class": "date-time"})[i].text
        d["temp"] = items.find_all("td", {"class": "temp"})[i].text
        d["precip"] = items.find_all("td", {"class": "precip"})[i].text
        d["wind"] = items.find_all("td", {"class": "wind"})[i].text
        d["humidity"] = items.find_all("td", {"class": "humidity"})[i].text
        l.append(d)
today = l[0]
mytmp_list = list(today["temp"])
temp_tmp = today["temp"]
in_temp = mytmp_list.index("°")
tmp_high_index = temp_tmp[0:in_temp + 1].index("°")
if temp_tmp[:1] == "--":
    high = "--"
    tmp_high_index = 2
else:
    high = str(int(round(9.0 / 5.0 * int(temp_tmp[:in_temp]) + 32)))
low = str(int(round(9.0 / 5.0 * int(temp_tmp[in_temp + 1:in_temp + tmp_high_index + 1]) + 32)))
print(full_weekdays[today["day"]] + "there is " + a_vs_an[today["precip"]] + " " +
      today["precip"] + " chance of precipitation. The high today will be " + high + " and the low will be " + low)
tmw = l[1]
mytmp_list = list(today["temp"])
temp_tmp = tmw["temp"]
in_temp = mytmp_list.index("°")
tmp_high_index = temp_tmp[0:in_temp + 1].index("°")
high = str(int(round(9.0 / 5.0 * int(temp_tmp[:in_temp]) + 32)))
low = str(int(round(9.0 / 5.0 * int(temp_tmp[in_temp + 1:in_temp + tmp_high_index + 1]) + 32)))
print("On " + full_weekdays[tmw["day"]] + " there is " + a_vs_an[tmw["precip"]] + " " +
      tmw["precip"] + " chance of precipitation and the high will be " + high + " while the low will be " + low)