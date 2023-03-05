import requests
import time
import math
#tbh if u fail to install the 3 requests without a readme your mentailly retarted

randomhook = "your_webhook"
while True:
  try:
      useheaders = {
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
      }
      bans = requests.get("https://api.plancke.io/hypixel/v1/punishmentStats", headers=useheaders).json()
      dog = bans["record"]["watchdog_rollingDaily"]
      staff = bans["record"]["staff_rollingDaily"]
      bans2 = requests.get("https://api.plancke.io/hypixel/v1/punishmentStats", headers=useheaders).json()
      dog2 = bans2["record"]["watchdog_rollingDaily"]
      staff2 = bans2["record"]["staff_rollingDaily"]
      if dog2 == dog:
          pass
      elif dog2 < dog:
          pass
      else:
          diff = dog2 - dog
          requests.post(randomhook, data={"content": f"{diff} Retard Got **Dogged** Smh <t:{math.floor(time.time())}:R>"})
      if staff == staff2:
          pass
      elif staff2 < staff:
          pass
      else:
          diff = staff2 - staff
          requests.post(randomhook, data={"content": f"{diff} Bozo Got **Staffed** FFS <t:{math.floor(time.time())}:R>"})
  except Exception as e:
      requests.post(randomhook, data={"content": f"ERROR ```{e}```"})
