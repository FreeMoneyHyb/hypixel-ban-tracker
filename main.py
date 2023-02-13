import requests
import time
import math

randomhook = "your_hook"
while True:
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
      requests.post(randomhook, data={"content": f"Some Retard Got Dogged Smh <t:{math.floor(time.time())}:R>"})
  if staff == staff2:
      pass
  elif staff2 < staff:
      pass
  else:
      requests.post(randomhook, data={"content": f"Some Bozo Got Staffed FFS <t:{math.floor(time.time())}:R>"})
