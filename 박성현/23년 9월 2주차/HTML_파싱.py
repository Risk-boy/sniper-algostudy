import re

def parse_html(html):
    # 문단(div 태그)을 찾는다.
    divs = re.findall(r'<div title="([^"]+)">((?:<p>.*?</p>)+)</div>', html)
    for title, p_tags in divs:
        print(f"title : {title}")
        
        # 각 문단에서 문장(p 태그)을 찾는다.
        sentences = re.findall(r'<p>(.*?)</p>', p_tags)
        
        for sentence in sentences:
            # 문장 내의 다른 태그를 제거한다.
            sentence = re.sub(r'<.*?>', '', sentence)
            
            # 문장의 시작과 끝의 공백을 제거한다.
            sentence = sentence.strip()
            
            # 문장에서 연속된 공백을 하나로 만든다.
            sentence = re.sub(r' +', ' ', sentence)
            
            print(sentence)


parse_html(input())