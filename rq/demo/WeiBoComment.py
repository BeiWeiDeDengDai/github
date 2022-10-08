import requests
import json

url = "https://weibo.com/ajax/statuses/buildComments"
#"https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4821680461975651&is_show_bulletin=2&is_mix=0&count=20&type=feed&uid=7769071152"
#"https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4821680461975651&is_show_bulletin=2&is_mix=0&count=10&uid=7769071152"
params = {
    "flow":0,
    "is_reload": 1,
    "id": 4821680461975651,
    "is_show_bulletin": 2,
    "is_mix": 0,
    "count": 30,
    "uid": 7769071152
}
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# 获取热搜
def get_hot_search():
    # 基础连接
    url = "https://weibo.com/ajax/feed/hottimeline"
    # 请求参数
    params = {
        "since_id": 0,
        "refresh": 0,
        "group_id": 102803, # 热搜
        "containerid": 102803,
        "extparam": "discover|new_feed",
        "max_id": 0,
        "count": 10
    }

    hot_resp = requests.get(url=url, params = params, headers=header)

    if hot_resp.status_code == 200:
        print("热搜请求成功，正在解析数据~")
        for user_card in json.loads(hot_resp.content)['statuses']:
            create_at = user_card['created_at']
            comments_count = user_card['comments_count']
            id = user_card['id']
            title = user_card['text_raw']
            user_id = user_card['user']['id']
            name = user_card['user']['screen_name']
            print("##############################【%s】【%s】评论数【%s】：%s ##################" % (create_at,
                                                                                            name,comments_count, title))

            get_comments(user_id, id)
            print("##############################【结束】##############################\n\n\n")
    else:
        print("抓取失败")



def get_comments(uid,id):
    params['uid'] = uid
    params['id'] = id
    response = requests.get(url, params=params, headers = header)
    response.encoding = "utf-8"
    resp_result = json.loads(response.text)
    cnt = 0
    for res in resp_result['data']:
        cnt += 1
        js = {}
        js['like_counts'] = res['like_counts']
        js['text_raw'] = res['text_raw']
        js['nick'] = res['user']['screen_name']
        js['comments'] = res['total_number']
        print("%s 用户:%s, 评论: %s, 评论回复数: %s, 评论点赞数: %s," % (cnt, js['nick'], js['text_raw'],js['comments'], js['like_counts']))



if __name__ == '__main__':
    get_hot_search()
    # get_comments(7769071152,4821680461975651)