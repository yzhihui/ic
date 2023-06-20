import json
import requests

def send_message(result):

    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/cd0788f5-55e1-4747-884a-15b975a119cc'
    payload = {"msg_type":"text","content":
        {"text":"用例总数：" + str(result['all'])+"\n" +
                "成功用例：" + str(result['success'])+"\n" +
                "失败用例：" + str(result['fail'])+"\n" +
                "错误用例：" + str(result['error']) + "\n" +
                "跳过用例：" + str(result['skip']) + "\n" +
                "测试报告：qareport.alphalawyer.cn"}}
    headers = {'Content-Type': 'application/json'}

    res = requests.post(url=url,data=json.dumps(payload),headers=headers)

    return res


# 调试
if __name__ == '__main__':
    result = {'success': 0, 'all': 6, 'fail': 0, 'skip': 0, 'error': 6}
    send_message(result)