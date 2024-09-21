import spacy

# GiNZAモデルのロード
nlp = spacy.load('ja_ginza')

# テキストを入力
text = '''
AIVtuberボイスで使える合成音声4選と比較紹介！【API使用可能】
https://youtu.be/52DHnERJIy8

AIVtuberボイスとして導入できる合成音声4選です！
→VOICEVOX、COEIROINK、Style-Bert-VITS2、ElevenLabs

こちら各ツールの概要・特徴を網羅的にこの動画1本で知ることができます🌟
'''

# テキストを解析
doc = nlp(text)

# 固有表現を抽出
proper_nouns = set()
for ent in doc.ents:
    if ent.label_ in ['Product', 'Work_of_art', 'ORG', 'PERSON']:
        proper_nouns.add(ent.text)

# 結果を表示
print("固有名詞：", proper_nouns)
