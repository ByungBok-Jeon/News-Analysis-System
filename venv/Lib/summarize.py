from gensim.summarization.summarizer import summarize

tmp_text = ''
with open(f"C:/Users/BB/PycharmProjects/LDA_EX02/txt/news1.txt", encoding="utf-8") as f:
    tmp_text=f.read()

print(tmp_text)

print(summarize(tmp_text, ratio=0.3))

