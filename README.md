<div align="center">

## 백준(BOJ) <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>

[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=kkg0510)](https://solved.ac/profile/kkg0510)
[![mazandi profile](http://mazandi.herokuapp.com/api?handle=kkg0510&theme=cold)](https://solved.ac/profile/kkg0510)

</div>

---

<details markdown="1">
<summary><strong>백준 단계별로 풀어보기<br>2022/01/27 ~ 2022/06/01</strong></summary>

<br>

<div align="center">

<table>

<th colspan="3">Contents</th>
<tr>
<td width="33%"  align="center"><a href="#브루트-포스">브루트 포스</a></td>
<td width="33%" align="center"><a href="#정렬">정렬</a></td>
<td width="33%" align="center"><a href="#백트래킹">백트래킹</a></td>
</tr>
<tr>
<td align="center"><a href="#동적-계획법-1">동적 계획법 1</a></td>
<td align="center"><a href="#그리디-알고리즘">그리디 알고리즘</a></td>
<td align="center"><a href="#정수론-및-조합론">정수론 및 조합론</a></td>
</tr>
<tr>
<td align="center"><a href="#스택">스택</a></td>
<td align="center"><a href="#큐-덱">큐, 덱</a></td>
<td align="center"><a href="#분할-정복">분할 정복</a></td>
</tr>
<tr>
<td align="center"><a href="#이분-탐색">이분 탐색</a></td>
<td align="center"><a href="#우선순위-큐">우선순위 큐</a></td>
<td align="center"><a href="#동적-계획법-2">동적 계획법 2</a></td>
</tr>
<tr>
<td align="center"><a href="#dfs와-bfs">DFS와 BFS</a></td>
<td align="center"><a href="#최단-경로">최단 경로</a></td>
<td align="center"><a href="#투-포인터">투 포인터</a></td>
</tr>
<tr>
<td align="center"><a href="#동적-계획법과-최단거리-역추적">동적 계획법과 최단거리 역추적</a></td>
<td align="center"><a href="#트리">트리</a></td>
<td align="center"><a href="#유니온-파인드">유니온 파인드</a></td>
</tr>
<tr>
<td align="center"><a href="#최소-신장-트리">최소 신장 트리</a></td>
<td align="center"><a href="#트리에서의-동적-계획법">트리에서의 동적 계획법</a></td>
<td align="center"><a href="#기하">기하</a></td>
</tr>
<tr>
<td align="center"><a href="#동적-계획법-3">동적 계획법 3</a></td>
<td align="center"><a href="#문자열-알고리즘-1">문자열 알고리즘 1</a></td>
<td align="center"><a href="#위상-정렬">위상 정렬</a></td>
</tr>
<tr>
<td align="center"><a href="#최소-공통-조상">최소 공통 조상</a></td>
<td align="center"><a href="#강한-연결-요소">강한 연결 요소</a></td>
<td align="center"><a href="#세그먼트-트리">세그먼트 트리</a></td>
</tr>

</table>

<!-- Contents -->

---

### 브루트 포스

|                                         난이도                                         |     번호     |        이름        | 날짜  | 체크 |
| :------------------------------------------------------------------------------------: | :----------: | :----------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/4.svg" width="20px" height="25px"></img> | [2798][2798] |       블랙잭       | 01/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/4.svg" width="20px" height="25px"></img> | [2231][2231] |       분해합       | 01/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [7568][7568] |        덩치        | 01/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [1018][1018] | 체스판 다시 칠하기 | 01/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [1436][1436] |    영화감독 숌     | 01/29 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 정렬

|                                         난이도                                         |      번호      |      이름       | 날짜  | 체크 |
| :------------------------------------------------------------------------------------: | :------------: | :-------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/5.svg" width="20px" height="25px"></img> |  [2750][2750]  |   수 정렬하기   | 01/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> |  [2751][2751]  |  수 정렬하기 2  | 01/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [10989][10989] |  수 정렬하기 3  | 01/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img> |  [2108][2108]  |     통계학      | 01/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> |  [1427][1427]  |  소트인사이드   | 01/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [11650][11650] |  좌표 정렬하기  | 01/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [11651][11651] | 좌표 정렬하기 2 | 01/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> |  [1181][1181]  |    단어 정렬    | 01/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img> | [10814][10814] |   나이순 정렬   | 01/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img> | [18870][18870] |    좌표 압축    | 01/30 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 백트래킹

|                                         난이도                                          |      번호      |      이름       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [15649][15649] |    N과 M (1)    | 01/31 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [15650][15650] |    N과 M (2)    | 01/31 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [15651][15651] |    N과 M (3)    | 01/31 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [15652][15652] |    N과 M (4)    | 01/31 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [9663][9663]  |     N-Queen     | 02/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [2580][2580]  |     스도쿠      | 02/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [14888][14888] | 연산자 끼워넣기 | 02/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  | [14889][14889] |  스타트와 링크  | 02/02 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 동적 계획법 1

|                                         난이도                                          |      번호      |            이름            | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :------------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [1003][1003]  |       피보나치 함수        | 02/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  |  [9184][9184]  |      신나는 함수 실행      | 02/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [1904][1904]  |           01타일           | 02/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [9461][9461]  |        파도반 수열         | 02/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [1149][1149]  |          RGB거리           | 02/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [1932][1932]  |        정수 삼각형         | 02/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [2579][2579]  |        계단 오르기         | 02/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [1463][1463]  |         1로 만들기         | 02/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [10844][10844] |        쉬운 계단 수        | 02/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [2156][2156]  |        포도주 시식         | 02/06 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  | [11053][11053] | 가장 긴 증가하는 부분 수열 | 02/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [11054][11054] | 가장 긴 바이토닉 부분 수열 | 02/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2565][2565]  |           전깃줄           | 02/08 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [9251][9251]  |            LCS             | 02/09 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  |  [1912][1912]  |           연속합           | 02/10 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [12865][12865] |        평범한 배낭         | 02/11 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 그리디 알고리즘

|                                         난이도                                          |      번호      |     이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-----------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [11047][11047] |    동전 0     | 02/11 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [1931][1931]  |  회의실 배정  | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [11399][11399] |      ATM      | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  |  [1541][1541]  | 잃어버린 괄호 | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [13305][13305] |    주유소     | 02/12 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 정수론 및 조합론

|                                         난이도                                          |      번호      |          이름           | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :---------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/3.svg" width="20px" height="25px"></img>  |  [5086][5086]  |       배수와 약수       | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img>  |  [1037][1037]  |          약수           | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img>  |  [2609][2609]  | 최대공약수와 최소공배수 | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img>  |  [1934][1934]  |       최소공배수        | 02/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2981][2981]  |          검문           | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [3036][3036]  |           링            | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/5.svg" width="20px" height="25px"></img>  | [11050][11050] |       이항 계수 1       | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [11051][11051] |       이항 계수 2       | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img>  |  [1010][1010]  |        다리 놓기        | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [9375][9375]  |      패션왕 신해빈      | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img>  |  [1676][1676]  |    팩토리얼 0의 개수    | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  |  [2004][2004]  |      조합 0의 개수      | 02/13 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 스택

|                                         난이도                                          |      번호      |     이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-----------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [10828][10828] |     스택      | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [10773][10773] |     제로      | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  |  [9012][9012]  |     괄호      | 02/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  |  [4949][4949]  | 균형잡힌 세상 | 02/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [1874][1874]  |   스택 수열   | 02/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [17298][17298] |    오큰수     | 02/15 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 큐, 덱

|                                         난이도                                          |      번호      |      이름       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [18258][18258] |      큐 2       | 02/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  |  [2164][2164]  |      카드2      | 02/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [11866][11866] | 요세푸스 문제 0 | 02/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [1966][1966]  |    프린터 큐    | 02/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [10866][10866] |       덱        | 02/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  |  [1021][1021]  |   회전하는 큐   | 02/17 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [5430][5430]  |       AC        | 02/18 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 분할 정복

|                                         난이도                                          |      번호      |              이름               | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-----------------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [2630][2630]  |          색종이 만들기          | 02/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [1992][1992]  |            쿼드트리             | 02/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  |  [1780][1780]  |           종이의 개수           | 02/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [1629][1629]  |              곱셈               | 02/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [11401][11401] |           이항 계수 3           | 02/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/5.svg" width="20px" height="25px"></img>  |  [2740][2740]  |            행렬 곱셈            | 02/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [10830][10830] |            행렬 제곱            | 02/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [11444][11444] |          피보나치 수 6          | 02/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [6549][6549]  | 히스토그램에서 가장 큰 직사각형 | 02/20 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 이분 탐색

|                                         난이도                                          |      번호      |             이름             | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :--------------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  |  [1920][1920]  |           수 찾기            | 02/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/7.svg" width="20px" height="25px"></img>  | [10816][10816] |         숫자 카드 2          | 02/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [1654][1654]  |         랜선 자르기          | 02/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [2805][2805]  |         나무 자르기          | 02/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2110][2110]  |         공유기 설치          | 02/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [1300][1300]  |           K번째 수           | 02/22 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [12015][12015] | 가장 긴 증가하는 부분 수열 2 | 02/23 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 우선순위 큐

|                                         난이도                                          |      번호      |      이름       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  | [11279][11279] |     최대 힙     | 02/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  |  [1927][1927]  |     최소 힙     | 02/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [11286][11286] |    절댓값 힙    | 02/24 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [1655][1655]  | 가운데를 말해요 | 02/24 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 동적 계획법 2

|                                         난이도                                          |      번호      |      이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [11066][11066] |  파일 합치기   | 02/24 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [11049][11049] | 행렬 곱셈 순서 | 02/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1520][1520]  |   내리막 길    | 02/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [10942][10942] |   팰린드롬?    | 02/26 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2629][2629]  |    양팔저울    | 02/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2293][2293]  |     동전 1     | 02/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [7579][7579]  |       앱       | 03/01 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### DFS와 BFS

|                                         난이도                                          |     번호     |        이름        | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :----------: | :----------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  | [1260][1260] |     DFS와 BFS      | 03/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [2606][2606] |      바이러스      | 03/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [2667][2667] |   단지번호붙이기   | 03/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  | [1012][1012] |    유기농 배추     | 03/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [2178][2178] |     미로 탐색      | 03/06 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [7576][7576] |       토마토       | 03/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [7569][7569] |       토마토       | 03/08 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [1697][1697] |      숨바꼭질      | 03/09 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [2206][2206] | 벽 부수고 이동하기 | 03/10 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [7562][7562] |   나이트의 이동    | 03/11 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [1707][1707] |    이분 그래프     | 03/12 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 최단 경로

|                                         난이도                                          |      번호      |       이름       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :--------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1753][1753]  |     최단경로     | 03/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1504][1504]  | 특정한 최단 경로 | 03/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [9370][9370]  |  미확인 도착지   | 03/15 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [11657][11657] |     타임머신     | 03/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [11404][11404] |     플로이드     | 03/17 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [10217][10217] |    KCM Travel    | 03/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1956][1956]  |       운동       | 03/19 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 투 포인터

|                                         난이도                                          |     번호     |     이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :----------: | :-----------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [3273][3273] |  두 수의 합   | 03/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [2470][2470] |    두 용액    | 03/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [1806][1806] |    부분합     | 03/22 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [1644][1644] | 소수의 연속합 | 03/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [1450][1450] |   냅색문제    | 03/24 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 동적 계획법과 최단거리 역추적

|                                         난이도                                          |      번호      |             이름             | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :--------------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> | [12852][12852] |         1로 만들기 2         | 03/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [14002][14002] | 가장 긴 증가하는 부분 수열 4 | 03/26 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> | [14003][14003] | 가장 긴 증가하는 부분 수열 5 | 03/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [9252][9252]  |            LCS 2             | 03/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [2618][2618]  |            경찰차            | 03/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [13913][13913] |          숨바꼭질 4          | 03/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [9019][9019]  |             DSLR             | 03/31 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [11779][11779] |      최소비용 구하기 2       | 04/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [11780][11780] |          플로이드 2          | 04/02 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 트리

|                                         난이도                                          |      번호      |       이름       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :--------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/9.svg" width="20px" height="25px"></img>  | [11725][11725] | 트리의 부모 찾기 | 04/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [1167][1167]  |   트리의 지름    | 04/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1967][1967]  |   트리의 지름    | 04/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/10.svg" width="20px" height="25px"></img> |  [1991][1991]  |    트리 순회     | 04/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [2263][2263]  |   트리의 순회    | 04/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [5639][5639]  |  이진 검색 트리  | 04/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [4803][4803]  |       트리       | 04/06 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 유니온 파인드

|                                         난이도                                          |      번호      |     이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-----------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1717][1717]  |  집합의 표현  | 04/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1976][1976]  |   여행 가자   | 04/08 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [4195][4195]  | 친구 네트워크 | 04/09 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [20040][20040] |  사이클 게임  | 04/10 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 최소 신장 트리

|                                         난이도                                          |      번호      |       이름       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :--------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  |  [9372][9372]  |  상근이의 여행   | 04/11 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1197][1197]  | 최소 스패닝 트리 | 04/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [4386][4386]  |  별자리 만들기   | 04/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [1774][1774]  | 우주신과의 교감  | 04/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> |  [2887][2887]  |    행성 터널     | 04/15 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [17472][17472] |  다리 만들기 2   | 04/16 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 트리에서의 동적 계획법

|                                         난이도                                          |      번호      |        이름        | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :----------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [15681][15681] |    트리와 쿼리     | 04/17 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> |  [2213][2213]  |  트리의 독립집합   | 04/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2533][2533]  | 사회망 서비스(SNS) | 04/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [1949][1949]  |     우수 마을      | 04/20 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 기하

|                                         난이도                                          |      번호      |     이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-----------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2166][2166]  | 다각형의 면적 | 04/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [11758][11758] |      CCW      | 04/22 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [17386][17386] |  선분 교차 1  | 04/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [17387][17387] |  선분 교차 2  | 04/24 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> | [20149][20149] |  선분 교차 3  | 04/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [2162][2162]  |   선분 그룹   | 04/26 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [7869][7869]  |     두 원     | 04/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [1069][1069]  |    집으로     | 04/28 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 동적 계획법 3

|                                         난이도                                          |      번호      |      이름      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/6.svg" width="20px" height="25px"></img>  | [11723][11723] |      집합      | 04/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> |  [1311][1311]  | 할 일 정하기 1 | 04/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> |  [2098][2098]  |  외판원 순회   | 04/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [1086][1086]  |     박성원     | 05/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [17404][17404] |   RGB거리 2    | 05/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [2482][2482]  |     색상환     | 05/02 |  ✔   |

<div align=right>
 
[TOP](#백준boj-)
 
</div>

---

### 문자열 알고리즘 1

|                                         난이도                                          |      번호      |    이름     | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :---------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [1786][1786]  |    찾기     | 05/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [4354][4354]  | 문자열 제곱 | 05/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [1305][1305]  |    광고     | 05/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> | [10266][10266] | 시계 사진들 | 05/06 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [14725][14725] |   개미굴    | 05/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/8.svg" width="20px" height="25px"></img>  | [14425][14425] | 문자열 집합 | 05/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [5670][5670]  | 휴대폰 자판 | 05/08 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 위상 정렬

|                                         난이도                                          |     번호     |   이름    | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :----------: | :-------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [2252][2252] | 줄 세우기 | 05/09 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [3665][3665] | 최종 순위 | 05/10 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [1766][1766] |  문제집   | 05/11 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 최소 공통 조상

|                                         난이도                                          |      번호      |         이름          | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [3584][3584]  | 가장 가까운 공통 조상 | 05/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [17435][17435] |    합성함수와 쿼리    | 05/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> | [11438][11438] |         LCA 2         | 05/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [3176][3176]  |     도로 네트워크     | 05/15 |  ✔   |
| <img src="https://static.solved.ac/tier_small/18.svg" width="20px" height="25px"></img> | [13511][13511] |     트리와 쿼리 2     | 05/16 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 강한 연결 요소

|                                         난이도                                          |      번호      |             이름             | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :--------------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [2150][2150]  | Strongly Connected Component | 05/17 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [4196][4196]  |            도미노            | 05/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [3977][3977]  |          축구 전술           | 05/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/19.svg" width="20px" height="25px"></img> |  [4013][4013]  |             ATM              | 05/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> | [11280][11280] |          2-SAT - 3           | 05/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/18.svg" width="20px" height="25px"></img> | [11281][11281] |          2-SAT - 4           | 05/22 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [3648][3648]  |            아이돌            | 05/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/18.svg" width="20px" height="25px"></img> | [16367][16367] |         TV Show Game         | 05/24 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>

---

### 세그먼트 트리

|                                         난이도                                          |      번호      |            이름            | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :------------------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> |  [2042][2042]  |       구간 합 구하기       | 05/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [11505][11505] |       구간 곱 구하기       | 05/26 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> |  [2357][2357]  |      최솟값과 최댓값       | 05/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [1517][1517]  |         버블 소트          | 05/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/18.svg" width="20px" height="25px"></img> |  [9345][9345]  | 디지털 비디오 디스크(DVDs) | 05/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> | [16975][16975] |       수열과 쿼리 21       | 05/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> | [12899][12899] |        데이터 구조         | 05/31 |  ✔   |
| <img src="https://static.solved.ac/tier_small/17.svg" width="20px" height="25px"></img> |  [1168][1168]  |      요세푸스 문제 2       | 06/01 |  ✔   |

<div align=right>

[TOP](#백준boj-)

</div>
<!-- ### -->

[2798]: https://www.acmicpc.net/problem/2798
[2231]: https://www.acmicpc.net/problem/2231
[7568]: https://www.acmicpc.net/problem/7568
[1018]: https://www.acmicpc.net/problem/1018
[1436]: https://www.acmicpc.net/problem/1436
[2750]: https://www.acmicpc.net/problem/2750
[2751]: https://www.acmicpc.net/problem/2751
[10989]: https://www.acmicpc.net/problem/10989
[2108]: https://www.acmicpc.net/problem/2108
[1427]: https://www.acmicpc.net/problem/1427
[11650]: https://www.acmicpc.net/problem/11650
[11651]: https://www.acmicpc.net/problem/11651
[1181]: https://www.acmicpc.net/problem/1181
[10814]: https://www.acmicpc.net/problem/10814
[18870]: https://www.acmicpc.net/problem/18870
[15649]: https://www.acmicpc.net/problem/15649
[15650]: https://www.acmicpc.net/problem/15650
[15651]: https://www.acmicpc.net/problem/15651
[15652]: https://www.acmicpc.net/problem/15652
[9663]: https://www.acmicpc.net/problem/9663
[2580]: https://www.acmicpc.net/problem/2580
[14888]: https://www.acmicpc.net/problem/14888
[14889]: https://www.acmicpc.net/problem/14889
[1003]: https://www.acmicpc.net/problem/1003
[9184]: https://www.acmicpc.net/problem/9184
[1904]: https://www.acmicpc.net/problem/1904
[9461]: https://www.acmicpc.net/problem/9461
[1149]: https://www.acmicpc.net/problem/1149
[1932]: https://www.acmicpc.net/problem/1932
[2579]: https://www.acmicpc.net/problem/2579
[1463]: https://www.acmicpc.net/problem/1463
[10844]: https://www.acmicpc.net/problem/10844
[2156]: https://www.acmicpc.net/problem/2156
[11053]: https://www.acmicpc.net/problem/11053
[11054]: https://www.acmicpc.net/problem/11054
[2565]: https://www.acmicpc.net/problem/2565
[9251]: https://www.acmicpc.net/problem/9251
[1912]: https://www.acmicpc.net/problem/1912
[12865]: https://www.acmicpc.net/problem/12865
[11047]: https://www.acmicpc.net/problem/11047
[1931]: https://www.acmicpc.net/problem/1931
[11399]: https://www.acmicpc.net/problem/11399
[1541]: https://www.acmicpc.net/problem/1541
[13305]: https://www.acmicpc.net/problem/13305
[5086]: https://www.acmicpc.net/problem/5086
[1037]: https://www.acmicpc.net/problem/1037
[2609]: https://www.acmicpc.net/problem/2609
[1934]: https://www.acmicpc.net/problem/1934
[2981]: https://www.acmicpc.net/problem/2981
[3036]: https://www.acmicpc.net/problem/3036
[11050]: https://www.acmicpc.net/problem/11050
[11051]: https://www.acmicpc.net/problem/11051
[1010]: https://www.acmicpc.net/problem/1010
[9375]: https://www.acmicpc.net/problem/9375
[1676]: https://www.acmicpc.net/problem/1676
[2004]: https://www.acmicpc.net/problem/2004
[10828]: https://www.acmicpc.net/problem/10828
[10773]: https://www.acmicpc.net/problem/10773
[9012]: https://www.acmicpc.net/problem/9012
[4949]: https://www.acmicpc.net/problem/4949
[1874]: https://www.acmicpc.net/problem/1874
[17298]: https://www.acmicpc.net/problem/17298
[18258]: https://www.acmicpc.net/problem/18258
[2164]: https://www.acmicpc.net/problem/2164
[11866]: https://www.acmicpc.net/problem/11866
[1966]: https://www.acmicpc.net/problem/1966
[10866]: https://www.acmicpc.net/problem/10866
[1021]: https://www.acmicpc.net/problem/1021
[5430]: https://www.acmicpc.net/problem/5430
[2630]: https://www.acmicpc.net/problem/2630
[1992]: https://www.acmicpc.net/problem/1992
[1780]: https://www.acmicpc.net/problem/1780
[1629]: https://www.acmicpc.net/problem/1629
[11401]: https://www.acmicpc.net/problem/11401
[2740]: https://www.acmicpc.net/problem/2740
[10830]: https://www.acmicpc.net/problem/10830
[11444]: https://www.acmicpc.net/problem/11444
[6549]: https://www.acmicpc.net/problem/6549
[1920]: https://www.acmicpc.net/problem/1920
[10816]: https://www.acmicpc.net/problem/10816
[1654]: https://www.acmicpc.net/problem/1654
[2805]: https://www.acmicpc.net/problem/2805
[2110]: https://www.acmicpc.net/problem/2110
[1300]: https://www.acmicpc.net/problem/1300
[12015]: https://www.acmicpc.net/problem/12015
[11279]: https://www.acmicpc.net/problem/11279
[1927]: https://www.acmicpc.net/problem/1927
[11286]: https://www.acmicpc.net/problem/11286
[1655]: https://www.acmicpc.net/problem/1655
[11066]: https://www.acmicpc.net/problem/11066
[11049]: https://www.acmicpc.net/problem/11049
[1520]: https://www.acmicpc.net/problem/1520
[10942]: https://www.acmicpc.net/problem/10942
[2629]: https://www.acmicpc.net/problem/2629
[2293]: https://www.acmicpc.net/problem/2293
[7579]: https://www.acmicpc.net/problem/7579
[1260]: https://www.acmicpc.net/problem/1260
[2606]: https://www.acmicpc.net/problem/2606
[2667]: https://www.acmicpc.net/problem/2667
[1012]: https://www.acmicpc.net/problem/1012
[2178]: https://www.acmicpc.net/problem/2178
[7576]: https://www.acmicpc.net/problem/7576
[7569]: https://www.acmicpc.net/problem/7569
[1697]: https://www.acmicpc.net/problem/1697
[2206]: https://www.acmicpc.net/problem/2206
[7562]: https://www.acmicpc.net/problem/7562
[1707]: https://www.acmicpc.net/problem/1707
[1753]: https://www.acmicpc.net/problem/1753
[1504]: https://www.acmicpc.net/problem/1504
[9370]: https://www.acmicpc.net/problem/9370
[11657]: https://www.acmicpc.net/problem/11657
[11404]: https://www.acmicpc.net/problem/11404
[10217]: https://www.acmicpc.net/problem/10217
[1956]: https://www.acmicpc.net/problem/1956
[3273]: https://www.acmicpc.net/problem/3273
[2470]: https://www.acmicpc.net/problem/2470
[1806]: https://www.acmicpc.net/problem/1806
[1644]: https://www.acmicpc.net/problem/1644
[1450]: https://www.acmicpc.net/problem/1450
[12852]: https://www.acmicpc.net/problem/12852
[14002]: https://www.acmicpc.net/problem/14002
[14003]: https://www.acmicpc.net/problem/14003
[9252]: https://www.acmicpc.net/problem/9252
[2618]: https://www.acmicpc.net/problem/2618
[13913]: https://www.acmicpc.net/problem/13913
[9019]: https://www.acmicpc.net/problem/9019
[11779]: https://www.acmicpc.net/problem/11779
[11780]: https://www.acmicpc.net/problem/11780
[11725]: https://www.acmicpc.net/problem/11725
[1167]: https://www.acmicpc.net/problem/1167
[1967]: https://www.acmicpc.net/problem/1967
[1991]: https://www.acmicpc.net/problem/1991
[2263]: https://www.acmicpc.net/problem/2263
[5639]: https://www.acmicpc.net/problem/5639
[4803]: https://www.acmicpc.net/problem/4803
[1717]: https://www.acmicpc.net/problem/1717
[1976]: https://www.acmicpc.net/problem/1976
[4195]: https://www.acmicpc.net/problem/4195
[20040]: https://www.acmicpc.net/problem/20040
[9372]: https://www.acmicpc.net/problem/9372
[1197]: https://www.acmicpc.net/problem/1197
[4386]: https://www.acmicpc.net/problem/4386
[1774]: https://www.acmicpc.net/problem/1774
[2887]: https://www.acmicpc.net/problem/2887
[17472]: https://www.acmicpc.net/problem/17472
[15681]: https://www.acmicpc.net/problem/15681
[2213]: https://www.acmicpc.net/problem/2213
[2533]: https://www.acmicpc.net/problem/2533
[1949]: https://www.acmicpc.net/problem/1949
[2166]: https://www.acmicpc.net/problem/2166
[11758]: https://www.acmicpc.net/problem/11758
[17386]: https://www.acmicpc.net/problem/17386
[17387]: https://www.acmicpc.net/problem/17387
[20149]: https://www.acmicpc.net/problem/20149
[2162]: https://www.acmicpc.net/problem/2162
[7869]: https://www.acmicpc.net/problem/7869
[1069]: https://www.acmicpc.net/problem/1069
[11723]: https://www.acmicpc.net/problem/11723
[1311]: https://www.acmicpc.net/problem/1311
[2098]: https://www.acmicpc.net/problem/2098
[1086]: https://www.acmicpc.net/problem/1086
[17404]: https://www.acmicpc.net/problem/17404
[2482]: https://www.acmicpc.net/problem/2482
[1786]: https://www.acmicpc.net/problem/1786
[4354]: https://www.acmicpc.net/problem/4354
[1305]: https://www.acmicpc.net/problem/1305
[10266]: https://www.acmicpc.net/problem/10266
[14725]: https://www.acmicpc.net/problem/14725
[14425]: https://www.acmicpc.net/problem/14425
[5670]: https://www.acmicpc.net/problem/5670
[2252]: https://www.acmicpc.net/problem/2252
[3665]: https://www.acmicpc.net/problem/3665
[1766]: https://www.acmicpc.net/problem/1766
[3584]: https://www.acmicpc.net/problem/3584
[17435]: https://www.acmicpc.net/problem/17435
[11438]: https://www.acmicpc.net/problem/11438
[3176]: https://www.acmicpc.net/problem/3176
[13511]: https://www.acmicpc.net/problem/13511
[2150]: https://www.acmicpc.net/problem/2150
[4196]: https://www.acmicpc.net/problem/4196
[3977]: https://www.acmicpc.net/problem/3977
[4013]: https://www.acmicpc.net/problem/4013
[11280]: https://www.acmicpc.net/problem/11280
[11281]: https://www.acmicpc.net/problem/11281
[3648]: https://www.acmicpc.net/problem/3648
[16367]: https://www.acmicpc.net/problem/16367
[2042]: https://www.acmicpc.net/problem/2042
[11505]: https://www.acmicpc.net/problem/11505
[2357]: https://www.acmicpc.net/problem/2357
[1517]: https://www.acmicpc.net/problem/1517
[9345]: https://www.acmicpc.net/problem/9345
[16975]: https://www.acmicpc.net/problem/16975
[12899]: https://www.acmicpc.net/problem/12899
[1168]: https://www.acmicpc.net/problem/1168

</div>

</details>

<details markdown="1">
<summary><strong>꾸준히 한 문제씩<br>2022/06/02 ~ 2022/06/30</strong></summary>

<br>

<div align="center">

|                                         난이도                                          |      번호      |        이름        |       분류       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :----------------: | :--------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [14503][14503] |    로봇 청소기     |       구현       | 06/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2550][2550]  |        전구        |        DP        | 06/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1107][1107]  |       리모컨       |    브루트포스    | 06/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [2133][2133]  |    타일 채우기     |        DP        | 06/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [7868][7868]  |     해밍 수열      |    브루트포스    | 06/06 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1041][1041]  |       주사위       |      그리디      | 06/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [16954][16954] | 움직이는 미로 탈출 |       BFS        | 06/08 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [12869][12869] |     뮤탈리스크     |        DP        | 06/09 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [3055][3055]  |        탈출        |       BFS        | 06/10 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [16929][16929] |      Two Dots      |       DFS        | 06/11 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2230][2230]  |     수 고르기      |    투 포인터     | 06/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [3661][3661]  |     생일 선물      |      그리디      | 06/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [14852][14852] |   타일 채우기 3    |        DP        | 06/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1354][1354]  |    무한 수열 2     |        DP        | 06/15 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1759][1759]  |    암호 만들기     |    브루트포스    | 06/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [10993][10993] |    별 찍기 - 18    |       재귀       | 06/17 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1261][1261]  |      알고스팟      |    다익스트라    | 06/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [23843][23843] |       콘센트       |      그리디      | 06/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2812][2812]  |    크게 만들기     |      그리디      | 06/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [5014][5014]  |     스타트링크     |       BFS        | 06/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [1365][1365]  |    꼬인 전깃줄     |    이분 탐색     | 06/22 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [23296][23296] |  엘리베이터 조작   |    위상 정렬     | 06/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [14262][14262] |    그림 그리기     |       구현       | 06/24 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [13023][13023] |       ABCDE        |       DFS        | 06/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [21924][21924] |     도시 건설      | 최소 스패닝 트리 | 06/26 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1240][1240]  |  노드사이의 거리   |       BFS        | 06/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [10422][10422] |        괄호        |      조합론      | 06/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [24463][24463] |        미로        |       DFS        | 06/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [22867][22867] |        종점        |      스위핑      | 06/30 |  ✔   |

[14503]: https://www.acmicpc.net/problem/14503
[2550]: https://www.acmicpc.net/problem/2550
[1107]: https://www.acmicpc.net/problem/1107
[2133]: https://www.acmicpc.net/problem/2133
[7868]: https://www.acmicpc.net/problem/7868
[1041]: https://www.acmicpc.net/problem/1041
[16954]: https://www.acmicpc.net/problem/16954
[12869]: https://www.acmicpc.net/problem/12869
[3055]: https://www.acmicpc.net/problem/3055
[16929]: https://www.acmicpc.net/problem/16929
[2230]: https://www.acmicpc.net/problem/2230
[3661]: https://www.acmicpc.net/problem/3661
[14852]: https://www.acmicpc.net/problem/14852
[1354]: https://www.acmicpc.net/problem/1354
[1759]: https://www.acmicpc.net/problem/1759
[10993]: https://www.acmicpc.net/problem/10993
[1261]: https://www.acmicpc.net/problem/1261
[23843]: https://www.acmicpc.net/problem/23843
[2812]: https://www.acmicpc.net/problem/2812
[5014]: https://www.acmicpc.net/problem/5014
[1365]: https://www.acmicpc.net/problem/1365
[23296]: https://www.acmicpc.net/problem/23296
[14262]: https://www.acmicpc.net/problem/14262
[13023]: https://www.acmicpc.net/problem/13023
[21924]: https://www.acmicpc.net/problem/21924
[1240]: https://www.acmicpc.net/problem/1240
[10422]: https://www.acmicpc.net/problem/10422
[24463]: https://www.acmicpc.net/problem/24463
[22867]: https://www.acmicpc.net/problem/22867

</div>

</details>

<details markdown="1">
<summary><strong>꾸준히 한 문제씩<br>2022/07/01 ~ 2022/07/31</strong></summary>

<br>

<div align="center">

|                                         난이도                                          |      번호      |            이름            |      분류      | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :------------------------: | :------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2170][2170]  |          선 긋기           |     스위핑     | 07/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [9997][9997]  |            폰트            |   비트마스크   | 07/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [15831][15831] |       준표의 조약돌        |   투 포인터    | 07/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1501][1501]  |         영어 읽기          |      해시      | 07/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [24391][24391] |       귀찮은 해강이        | 유니온 파인드  | 07/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [15553][15553] |            난로            |     그리디     | 07/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2251][2251]  |            물통            |      BFS       | 07/06 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [13398][13398] |          연속합 2          |       DP       | 07/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2528][2528]  |           사다리           |      구현      | 07/08 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [1516][1516]  |         게임 개발          |   위상 정렬    | 07/09 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [6087][6087]  |        레이저 통신         |   다익스트라   | 07/10 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [14466][14466] |  소가 길을 건너간 이유 6   |      BFS       | 07/11 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> | [12896][12896] |       스크루지 민호        |      트리      | 07/12 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [13460][13460] |        구슬 탈출 2         |      구현      | 07/13 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [12100][12100] |        2048 (Easy)         |      구현      | 07/14 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [3190][3190]  |             뱀             |      구현      | 07/15 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2065][2065]  |           나룻배           |      구현      | 07/16 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [14499][14499] |       주사위 굴리기        |      구현      | 07/17 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [13334][13334] |            철로            |     스위핑     | 07/18 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [2836][2836]  |         수상 택시          |     스위핑     | 07/19 |  ✔   |
| <img src="https://static.solved.ac/tier_small/15.svg" width="20px" height="25px"></img> | [14428][14428] |       수열과 쿼리 16       | 세그먼트 트리  | 07/20 |  ✔   |
| <img src="https://static.solved.ac/tier_small/16.svg" width="20px" height="25px"></img> |  [1761][1761]  |       정점들의 거리        | 최소 공통 조상 | 07/21 |  ✔   |
| <img src="https://static.solved.ac/tier_small/13.svg" width="20px" height="25px"></img> |  [1865][1865]  |            웜홀            |   벨만 포드    | 07/22 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [7511][7511]  | 소셜 네트워킹 어플리케이션 | 유니온 파인드  | 07/23 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1245][1245]  |         농장 관리          |      DFS       | 07/24 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1106][1106]  |            호텔            |       DP       | 07/25 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [18116][18116] |         로봇 조립          | 유니온 파인드  | 07/26 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> |  [3109][3109]  |            빵집            |      DFS       | 07/27 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1043][1043]  |           거짓말           | 유니온 파인드  | 07/28 |  ✔   |
| <img src="https://static.solved.ac/tier_small/14.svg" width="20px" height="25px"></img> | [10711][10711] |           모래성           |      BFS       | 07/29 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [1744][1744]  |          수 묶기           |     그리디     | 07/30 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [14567][14567] |  선수과목 (Prerequisite)   |   위상 정렬    | 07/31 |  ✔   |

[2170]: https://www.acmicpc.net/problem/2170
[9997]: https://www.acmicpc.net/problem/9997
[15831]: https://www.acmicpc.net/problem/15831
[1501]: https://www.acmicpc.net/problem/1501
[24391]: https://www.acmicpc.net/problem/24391
[15553]: https://www.acmicpc.net/problem/15553
[2251]: https://www.acmicpc.net/problem/2251
[13398]: https://www.acmicpc.net/problem/13398
[2528]: https://www.acmicpc.net/problem/2528
[1516]: https://www.acmicpc.net/problem/1516
[6087]: https://www.acmicpc.net/problem/6087
[14466]: https://www.acmicpc.net/problem/14466
[12896]: https://www.acmicpc.net/problem/12896
[13460]: https://www.acmicpc.net/problem/13460
[12100]: https://www.acmicpc.net/problem/12100
[3190]: https://www.acmicpc.net/problem/3190
[2065]: https://www.acmicpc.net/problem/2065
[14499]: https://www.acmicpc.net/problem/14499
[13334]: https://www.acmicpc.net/problem/13334
[2836]: https://www.acmicpc.net/problem/2836
[14428]: https://www.acmicpc.net/problem/14428
[1761]: https://www.acmicpc.net/problem/1761
[1865]: https://www.acmicpc.net/problem/1865
[7511]: https://www.acmicpc.net/problem/7511
[1245]: https://www.acmicpc.net/problem/1245
[1106]: https://www.acmicpc.net/problem/1106
[18116]: https://www.acmicpc.net/problem/18116
[3109]: https://www.acmicpc.net/problem/3109
[1043]: https://www.acmicpc.net/problem/1043
[10711]: https://www.acmicpc.net/problem/10711
[1744]: https://www.acmicpc.net/problem/1744
[14567]: https://www.acmicpc.net/problem/14567

</div>

</details>

<details open markdown="1">
<summary><strong>꾸준히 한 문제씩<br>2022/08/01 ~</strong></summary>

<br>

<div align="center">

|                                         난이도                                          |      번호      |           이름            |      분류       | 날짜  | 체크 |
| :-------------------------------------------------------------------------------------: | :------------: | :-----------------------: | :-------------: | :---: | :--: |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> |  [3078][3078]  |         좋은 친구         | 슬라이딩 윈도우 | 08/01 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [15723][15723] |         n단 논법          |  플로이드 워셜  | 08/02 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [18231][18231] |        파괴된 도시        |     그리디      | 08/03 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [14267][14267] |        회사 문화 1        |       DP        | 08/04 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [2096][2096]  |         내려가기          | 슬라이딩 윈도우 | 08/05 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [15703][15703] |        주사위 쌓기        |     그리디      | 08/06 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> | [17265][17265] | 나의 인생에는 수학과 함께 |       BFS       | 08/07 |  ✔   |
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" height="25px"></img> |  [1013][1013]  |          Contact          |     정규식      | 08/08 |  ✔   |
| <img src="https://static.solved.ac/tier_small/12.svg" width="20px" height="25px"></img> | [11056][11056] |      두 부분 문자열       |       DP        | 08/09 |  ✔   |

<!-- new -->

[3078]: https://www.acmicpc.net/problem/3078
[15723]: https://www.acmicpc.net/problem/15723
[18231]: https://www.acmicpc.net/problem/18231
[14267]: https://www.acmicpc.net/problem/14267
[2096]: https://www.acmicpc.net/problem/2096
[15703]: https://www.acmicpc.net/problem/15703
[17265]: https://www.acmicpc.net/problem/17265
[1013]: https://www.acmicpc.net/problem/1013
[11056]: https://www.acmicpc.net/problem/11056

<!-- new-link -->

</div>

</details>
