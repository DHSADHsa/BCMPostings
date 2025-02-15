import requests
import os
import time

session = requests.session()
#开始备份的帖子id
i_t = 0
while True:
    i = i_t
    print(i)
    time.sleep(0.35)
    if os.path.exists('./bcm论坛/' + str(i_t) + '.txt') == False and os.path.exists('./不存在帖子/' + str(i_t) + '.txt') == False:
        r2 = session.get('https://api.codemao.cn/web/forums/posts/' + str(i) + '/details')
        print(r2.text)
        if r2.text.count("操作过于频繁") < 1:
            if r2.text.count("error_message") < 1:
                print(r2.json())
                bt =  "【" + r2.json()["board_name"] + "】"+ r2.json()["id"] + '-' + r2.json()["title"]
                nrT = r2.json()["content"]
                fq = r2.json()["board_name"]
                if r2.text.count("work_shop_name") == 1 and r2.text.count("work_shop_level") == 1:
                    user = "【" + str(r2.json()["user"]["work_shop_level"]) + "|" + r2.json()["user"]["work_shop_name"] + "】" + r2.json()["user"]["id"] +"|"+ r2.json()["user"]["nickname"]
                elif r2.text.count("work_shop_leve") < 1 and r2.text.count("work_shop_name") == 1:
                    user = "【" + "0" + "|" + r2.json()["user"]["work_shop_name"] + "】" + r2.json()["user"]["id"] + "|" + r2.json()["user"]["nickname"]
                else:
                    user = r2.json()["user"]["id"] + "|" + r2.json()["user"]["nickname"]
                cjsj = r2.json()["created_at"]
                gxsj = r2.json()["updated_at"]
                gks = r2.json()["n_views"]
                dzl = r2.json()["n_replies"] + r2.json()["n_comments"]
                # 确保目录存在
                if not os.path.exists('./bcm论坛'):
                    os.makedirs('./bcm论坛')
                file = open('./bcm论坛/' + r2.json()["id"] + '.txt', "w", encoding='utf-8')
                file.write(bt + '\n' + user + '\n' + "——————————————————————————" + '\n' + nrT + '\n\n' + "创建时间:" + str(cjsj) + "\n" + "更新时间:" + str(gxsj) + "\n" + "观看次数:" + str(gks) + "\n" + "回帖数:" + str(dzl)+ "\n")
                print(f'文件{bt}保存成功！')
                file.close()
                i_t = i_t + 1
            else:
                if not os.path.exists('./不存在帖子'):
                    os.makedirs('./不存在帖子')
                file = open('./不存在帖子/' + str(i_t) + ".txt", "w", encoding='utf-8')
                file.write("id:" + str(i_t) + "\n错误:" + r2.text)
                print(f'错误文件已新建')
                file.close()
                i_t = i_t + 1
        else:
            print("触发了编程猫的太快检测，作品id" + str(i))
            i_t = i
    else:
        print("已经判断过了")
        i_t = i_t + 1