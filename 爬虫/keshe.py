import requests
import time
from urllib.parse import quote

#网页地址、保存地址、关键词
keyword=input("请输入关键词:")
keyword=quote(keyword)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48'
}
url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=20132692&is=&' \
    'fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=ut' \
    'f-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&w' \
    'ord={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=' \
    '&nc=1&fr=&expermode=&nojc=&cg=head&pn={}&rn=30&gsm=3c&1623944229318='.format(keyword,keyword,30)
root="./picture/"


#爬取网页，获取图片地址
html=requests.get(url=url,headers=headers,timeout=10)
time.sleep(2)
img=html.json()['data']
img_url=[]
for i in img:
    img_url.append(i.get('thumbURL'))


#爬取图片并保存
headers['Referer']='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1557124645631_R&pv=&ic=&nc=1&z=&hd=1&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word={}'.format(keyword)
for i in range(30):
    with open(root+str(i+1)+'.jpg','wb') as f:
        f.write(requests.get(url=img_url[i],headers=headers).content)
    time.sleep(1)
    print("第{}张打印完毕".format(i+1))


