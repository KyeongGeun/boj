def solution(genres, plays):
    answer = []
    
    dic_cnt = {}
    dic_li = {}
    for i in range(len(genres)):
        dic_cnt.setdefault(genres[i], 0)
        dic_li.setdefault(genres[i], [])
        dic_cnt[genres[i]] += plays[i]
        dic_li[genres[i]].append((plays[i], i))
    
    for key in dic_li:
        dic_li[key].sort(key=lambda x: (-x[0], x[1]))
    
    for key, _ in sorted(dic_cnt.items(), key=lambda x: -x[1]):
        answer.append(dic_li[key][0][1])
        if len(dic_li[key]) > 1:
            answer.append(dic_li[key][1][1])
        
    
    return answer