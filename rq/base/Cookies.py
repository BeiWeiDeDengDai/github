import requests

headers = {
    "Cookie": "517437729195%3AWM_TID=fLoWDMaJJv9ARVUUBAN6lGzAqnkbhcM0; _xsrf=4f568ca7-c289-4a7b-a201-9c621a09cde3; "
              "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1660100360,1660189594,1661511522,1661751433; "
              "captcha_session_v2=2|1:0|10:1661771322|18:captcha_session_v2|88"
              ":ajVxSk00UGV0S0NPeXNUM0tOMiswQmIzVzJtaElmTmZRMXQwOGVKU3FNekN3bVAxRmxpQkwyMWwyZWprRTlCOA"
              "==|d2729229a53ca4f8d89654b28d85d6b6ff15bbe13993ec60f153046fd58faca7; "
              "SESSIONID=fp98JnlPqYsJVHIrLoKS2GtTfUqFWUONdLyOLckenBr; "
              "JOID=VV4TAE6Z0A6AESg9LZ0jHgAOJBY9_qAyvllHUXjqiH3PQWJ1X6JLAecSKTgudW2SOu4O8tBczndMJmG86ADScIY=; "
              "osd=V1sTAEib1Q6AFyo4LZ0lHAUOJBA_-6AyuFtCUXjsinjPQWR3WqJLB-UXKTgod2iSOugM99BcyHVJJmG66gXScIA=; "
              "__snaker__id=GbBHQXvXL1eMNC9e; "
              "gdxidpyhxdE=4jGTxj732HQ405cR%5Cofk3IRjXb1dqxzHQmRiMCiepH7RxC2d02nQkH7bCM0UwD5Z"
              "%2FyZf6uuZxntlmgCaVmNe9fy4%5C9pbYB%5CwVcaSCo5ALPB5oV5opUWhG9abMsocrKHwm1kk%2FXd%5CSIMMZ8mpk"
              "%5CYgXeGr2qhMpb%5CwRqDytcCBuY%2F7aLnJ%3A1661772223150; "
              "YD00517437729195%3AWM_NI=7sg2HwwZBmxDjdj46QRAabtnMeSca5yoCZwR%2FkzodoSHVH1"
              "%2FSwiYxTFuTemAzxApDj3hzuoaH6VBJWqFVuHxM6PLBl2HN%2FMKugGyNVlm8LXM6%2B2xy49Xfro2SWFl2J64eTQ%3D; "
              "YD00517437729195%3AWM_NIKE"
              "=9ca17ae2e6ffcda170e2e6eeaeb43994b2faa6d35bf6928ab6c84b878a8a83c854a6a68cabd96498b886d1f02af0fea7c3b92af5ada9d3cb7db5868e8efb50aabca6d5b55b929faf83f7668fbb9d84e43fbbb18dbbf65aedb5b690e76591989aa9b42591a9a7bafb6086ab9c86f04bbaa88f91c762f1b8b696ee6b8cea9aa3c95db39a9a96cb748feaa0adc168f29882d0d041b7b9899acd5eb0b3f8addb47f6f5fe99fc40fb88aa93ee3a91898a8db142f6ecabb5d437e2a3; o_act=login; utm_source=google; ref_source=other_https://www.zhihu.com/signin?next=/; expire_in=15552000; z_c0=2|1:0|10:1661771350|4:z_c0|92:Mi4xdFlGcUR3QUFBQUFBc0o0TE9qRldGUmNBQUFCZ0FsVk5WdXo1WXdBLWh4NV8yNUlvaHBJb3BYWGRvdEVvUGliWDF3|50bb76bf431afd12678a85135be7fab77172b92c74c9f537f91e831569ff4152; q_c1=71f6ab26b6da4cf19787d300ae73ddd0|1661771350000|1661771350000; NOT_UNREGISTER_WAITING=1; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1661771360|1661771320; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1661771362",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.0.0 Safari/537.36 ",

}
resp = requests.get("https://www.zhihu.com/", headers=headers)
resp.encoding = "utf-8"
print(resp.text)
