import requests

url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

params = {
    'pageNum' : '1',
    'rangetype' : 'All',
    'orderBy' : 'sim',
    'keyword' : 'python',
}

response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=params)

print(response.status_code)
print(response.url) 