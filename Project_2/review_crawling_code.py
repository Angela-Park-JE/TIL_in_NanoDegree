# crawling code by team member Mina, Jaein


### import library
import pandas as pd
import requests 
from bs4 import BeautifulSoup as bs


### page info
movie_code = {movie_code}
url=f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"    
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
response=requests.get(url,headers=headers) 
html = bs(response.text,'lxml')


### crawling the end of page 
# bringing the total review number
total = html.select('div.score_total > strong.total > em')
cnt = int(total[0].text.replace(',',''))

# 10 reviews in 1 page
page_end = int(cnt / 10)
if cnt % 10 != 0:
    page_end += 1

print(page_end)


### definite a function to crawling 
import re

def get_review_list(page_no, review_list, movie_code):
    url=f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page_no}"    
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    response=requests.get(url,headers=headers) 
    html = bs(response.text,'lxml')
    
    review = html.select('div.score_result > ul > li > div.score_reple > p > span')
    score = html.select('div.score_result > ul > li > div.star_score > em')

    num = 0
    cnt = 0
    
    like = html.select('div.btn_area > a._sympathyButton> strong')
    unlike = html.select('div.btn_area > a._notSympathyButton > strong')  
    
    while (num < len(review)):
        info_dic = {"댓글번호":'', "작성일자":'', "댓글":'', "평점":0, "관람여부":0, "스포여부":0, "공감수":0, "비공감수":0, "id":''} 

        review_no = str(html.select('div.score_reple > dl > dt > em > a')[cnt])
        info_dic["댓글번호"] = int(re.findall('\d+',str(review_no))[0])
        
        info_dic["id"] = html.select('div.score_reple > dl > dt ')[cnt].text.strip().split('\n\n\n')[0]
        info_dic["작성일자"] = html.select('div.score_reple > dl > dt ')[cnt].text.strip().split('\n\n\n')[1]

        if review[num].text == '관람객':
            info_dic["관람여부"] = 1
            if review[num+1].text == '스포일러가 포함된 감상평입니다. 감상평 보기':
                info_dic["스포여부"] = 1
                info_dic["댓글"] = review[num+2].text.strip()
                num += 3
            else :   
                info_dic["댓글"] = review[num+1].text.strip()
                num += 2
        elif review[num].text == '스포일러가 포함된 감상평입니다. 감상평 보기':
            info_dic["스포여부"] = 1
            info_dic["댓글"] = review[num+1].text.strip()
            num += 2
        else :
            info_dic["댓글"] = review[num].text.strip()
            num += 1

        # score
        info_dic["평점"] = score[cnt].text.strip()
        
        # liked and unliked amount
        info_dic["공감수"] = int(re.findall('\d+',str(like[cnt]))[1])
        info_dic["비공감수"] = int(re.findall('\d+',str(unlike[cnt]))[1])            
        
        # next page
        cnt += 1
        # saving data crawled
        review_list.append(info_dic)


### real crawling with 'while' repeat


