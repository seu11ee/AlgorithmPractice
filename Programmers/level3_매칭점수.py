from collections import defaultdict
import re

BASIC = 0
EXTERNAL = 1
LINK = 2
MATCH = 3
def solution(word, pages):
    answer = 0
    score_dict = defaultdict(int)
    urls = ["" for _ in range(len(pages))]
    external_links = [[] for _ in range(len(pages))]
    link_to_me = [set() for _ in range(len(pages))]
    for idx,page in enumerate(pages):
        #페이지 분석후 딕셔너리에 저장
        url = get_url(page)
        urls[idx] = url
        score_dict[(idx, BASIC)] = get_word_count(page, word.lower())
        links = get_external_links(page)
        external_links[idx] = links
        score_dict[(idx, EXTERNAL)] = len(links)
    #나를 가리키는 링크 찾
    for idx,links in enumerate(external_links):
        for link in links:
            if link in urls:
                link_to_me[urls.index(link)].add(idx)
    #링크/매칭 점수 계산
    for i in range(len(pages)):
        link_score = 0
        for j in link_to_me[i]:
            link_score += score_dict[(j,BASIC)]/score_dict[(j,EXTERNAL)]
        score_dict[(i,LINK)] = link_score
        score_dict[(i,MATCH)] = score_dict[(i,BASIC)]+score_dict[(i,LINK)]
    maxValue = -1
    for i in range(len(pages)):
        if score_dict[(i,MATCH)] > maxValue:
            maxValue = score_dict[(i,MATCH)]
            answer = i
    return answer

def get_external_links(page):
    urls = re.findall('<a href="https://([\S]+)"', page)
    print("urls",urls)
    return urls

def get_url(page):
    url = re.search('<meta property="og:url" content="https://(\S+)"/>',page).group(1)
    print("url: ",url)
    return url
def get_word_count(body_text,word):
    body_text = body_text.lower()
    words = re.findall("[a-z]+",body_text)
    cnt = words.count(word)

    return cnt

print(solution('blind',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))