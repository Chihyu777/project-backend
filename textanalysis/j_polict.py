#jieba 逐字稿斷詞+詞性標註
#encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as psg

#jieba.load_userdict("my.dict.txt")

#蔡適應立委政見
news = '持續推進 交通優化：持續爭取快捷公車新路線；督促城際轉運站工程進度；爭取國道一號拓寬。文化傳承 藝文觀光：古蹟修復，重現大基隆歷史場景；改善藝文環境發展觀光。河川整治 親水空間：爭取政府補助治水、改善水質，打造市民親水環境。活化閒置 國有土地：政府三年移撥30公頃土地；持續活化空間及電桿下地。軍港西遷 繁榮軍港：監督軍港遷移如期如質完工；推動郵輪母港計畫，促進觀光再生。長照貼心 走入社區：廣佈各級長照據點，擴增服務項目，落實銀髮族照護。醫療資源 整合服務：部立醫院引進台北榮總醫療資源；擴大三總服務，提升品質與醫病關係。友善婦幼 敢生好養：提高公共化托嬰托兒比例，落實婦幼福利，減輕育兒負擔。守護主權 堅持民主：全力推動相關政策及修法，維護台灣主體性與民主價值。潛艦園區 活絡產業：支持國防自主與裝備籌獲，爭取基隆成為產業基地、增加就業機會。'
tags = jieba.analyse.extract_tags(news, topK=30, withWeight=True)
seg = psg.cut(news)


for ele in seg:
        print(ele)
for sentence in news:
    seg_list = jieba.lcut(sentence, cut_all=True)
seg_list = jieba.lcut(news)
print(seg_list)
for tag in tags:
    print('word:', tag[0], 'tf-idf:', tag[1])


