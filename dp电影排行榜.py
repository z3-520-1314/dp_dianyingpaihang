"""
代码拉跨，大佬请路过
"""
import os
try:
    import requests # 导入requests模块
except ImportError: 
    # 如果没有安装requests模块，就安装requests模块
    # 使用清华大学的镜像网站安装requests模块
    os.system('pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple')
    import requests

def main(stat:int = 0， end:int = 5):
    """
    :stat : 作品开始数
    :end : 从开始到结束有多少个作品
    :return : 默认取前5个热度排名作品
    """
    # 查找范围内的数据
    if stat > end :
        print('请输入正确的开始数和结束数')
        exit()
    else:
        if stat == 0:
            stat = 1
        if end == 0:
            end = 1
        
        end = end -1 - stat + 1
    
    
    # 目标网址（ 在f12里面的网络工具中，滚动网页发现个这玩意，start=0&limit=10 代表查看前10名作品）
    url = f'https://movie.douban.com/j/chart/top_list?type=1&interval_id=100%3A90&action=&start={stat-1}&limit={end+1}'

    # 头部用于模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }

    # 设置会话
    session = requests.Session()
    html = session.get(url,headers=headers)

    # 图片地址_json数据
    img_url = []
    for i in html.json():
        img_url.append(i['cover_url'])

    # 作品名_json数据
    zp_title = []
    for i in html.json():
        zp_title.append(i['title'])

    # 作品对应的热度排名_json数据
    rank = []
    for i in html.json():
        rank.append(i['rank'])
    
    # 影片地址_json数据
    zp_url = []
    for i in html.json():
        zp_url.append(i['url'])

    # 把数据组合在一区
    for img,name,r,zp in zip(img_url，zp_title,rank,zp_url):
        # 组合为一个变量，方便使用
        payload = f"图片地址,{img}\n作品名,{name}\n作品对应的热度排名,{r}\n作品地址,{zp}"
        print(payload)
        print('\n')
        # # 用gb2312编码保存到csv文件，如果是Linux系统改为utf-8
        # rank_csv = open('排行.csv'，'a+',encoding='gb2312')
        # rank_csv.write(f"{payload}\n\n")
        # rank_csv.close()

if __name__ == '__main__':
    main()
