
import requests

def get_user_list():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        res = requests.get(url, timeout=5)
        assert res.status_code == 200, "查询用户失败"
        users = res.json()
        print("=== 查询到用户数量：", len(users))
        print("第一个用户名称：", users[0]["name"])
    except Exception as e:
        print("GET 请求出错：", e)

def create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    data = {
        "name": "我是测试用户",
        "username": "testaccount",
        "email": "test@test.com"
    }

    try:
        res = requests.post(url, json=data, timeout=5)

        assert res.status_code == 201, "创建用户失败"

        result = res.json()
        print("\n=== 创建成功！返回信息：")
        print("用户ID：", result["id"])
        print("用户名：", result["name"])

    except Exception as e:
        print("POST 请求出错：", e)

if __name__ == "__main__":
    get_user_list()
    create_user()
