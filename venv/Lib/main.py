import sent_act

all_news = []
pol_news = []
eco_news = []
soc_news = []
wor_news = []
lif_news = []
its_news = []

for i in range(5):
    all_news.append(sent_act.read_file("all", f"{i+1}", 5))
    pol_news.append(sent_act.read_file("pol", f"{i+1}", 5))
    eco_news.append(sent_act.read_file("eco", f"{i+1}", 5))
    soc_news.append(sent_act.read_file("soc", f"{i+1}", 5))
    wor_news.append(sent_act.read_file("wor", f"{i+1}", 5))
    lif_news.append(sent_act.read_file("lif", f"{i+1}", 5))
    its_news.append(sent_act.read_file("its", f"{i+1}", 5))

cat_result = list()
cat_result_all = list()

# cat_result_all[[all]*5,[pol]*5,[eco]*5,[soc]*5,[wor]*5,[lif]*5,[its]*5]
for i in range(5):
    cat_result = sent_act.cat_predict(all_news[i])
    cat_result_all.append(cat_result)
for i in range(5):
    cat_result = sent_act.cat_predict(pol_news[i])
    cat_result_all.append(cat_result)
for i in range(5):
    cat_result = sent_act.cat_predict(soc_news[i])
    cat_result_all.append(cat_result)
for i in range(5):
    cat_result = sent_act.cat_predict(eco_news[i])
    cat_result_all.append(cat_result)
for i in range(5):
    cat_result = sent_act.cat_predict(lif_news[i])
    cat_result_all.append(cat_result)
for i in range(5):
    cat_result = sent_act.cat_predict(wor_news[i])
    cat_result_all.append(cat_result)
for i in range(5):
    cat_result = sent_act.cat_predict(its_news[i])
    cat_result_all.append(cat_result)

