# for 문으로 돌릴 때 진행 상황을 볼 수 있도록 하는 라이브러리이다.
from tqdm import tqdm 

# for문의 가져올 리스트에 해당하는 부분을 이것으로 감싸주면 된다.

# 감싸기 전
for i in range(len(df_2010_sample['댓글'])):
    before_2010_review_list.append(spacing(df_2010_sample['댓글'][i]))

# 감싼 후
for i in tqdm(range(len(df_2010_sample['댓글']))):
    before_2010_review_list.append(spacing(df_2010_sample['댓글'][i]))

# 결과문 : 진행 상태가 뜬다.
# 100%|█████████████████████████████████████| 50000/50000 [43:54<00:00, 18.98it/s]
