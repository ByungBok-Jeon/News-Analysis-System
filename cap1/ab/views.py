from django.shortcuts import render
from django.http import HttpResponse
from gensim.summarization.summarizer import summarize
import main

def opentxt(categori,tp_list):
    for i in range(5):
        for j in range(5):
            tmp_text = ''
            with open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/result/" + categori + "/" + categori + f"_result{i + 1}_{j + 1}.txt",encoding="utf-8") as f:
                tmp_text = f.read()
                tp_list.append(tmp_text)
#{'all' : '전체',  'pol' : '정치','eco' : '경제','soc' : '사회','lif' : '생활/문화','wor' : '세계','its' : 'IT/과학'}
all = list(); pol = list(); eco = list(); soc = list(); lif = list(); wor = list(); its = list();
all_tl = list(); pol_tl = list(); eco_tl = list(); soc_tl = list(); lif_tl = list(); wor_tl = list(); its_tl = list();
opentxt("all",all); opentxt("pol",pol); opentxt("eco",eco); opentxt("soc",soc); opentxt("lif",lif); opentxt("wor",wor); opentxt("its",its);
for i in range(25):
    a = summarize((all[i]),word_count=50)
    all_tl.append(a)
    a = summarize((pol[i]), word_count=50)
    pol_tl.append(a)
    a = summarize((eco[i]), word_count=50)
    eco_tl.append(a)
    a = summarize((soc[i]), word_count=50)
    soc_tl.append(a)
    a = summarize((lif[i]), word_count=50)
    lif_tl.append(a)
    a = summarize((wor[i]), word_count=50)
    wor_tl.append(a)
    a = summarize((its[i]), word_count=50)
    its_tl.append(a)


all_pos = 0
all_nut = 0
all_neg = 0

for i in range(5):
    all_pos += main.cat_result_all[i].count(1)
    all_nut += main.cat_result_all[i].count(2)
    all_neg += main.cat_result_all[i].count(0)

all_pos = all_pos*4
all_nut = all_nut*4
all_neg = all_neg*4

pol_pos = 0
pol_nut = 0
pol_neg = 0

for i in range(5):
    pol_pos += main.cat_result_all[i+5].count(1)
    pol_nut += main.cat_result_all[i+5].count(2)
    pol_neg += main.cat_result_all[i+5].count(0)

pol_pos = pol_pos * 4
pol_nut = pol_nut * 4
pol_neg = pol_neg * 4

soc_pos = 0
soc_nut = 0
soc_neg = 0

for i in range(5):
    soc_pos += main.cat_result_all[i + 10].count(1)
    soc_nut += main.cat_result_all[i + 10].count(2)
    soc_neg += main.cat_result_all[i + 10].count(0)

soc_pos = soc_pos * 4
soc_nut = soc_nut * 4
soc_neg = soc_neg * 4

eco_pos = 0
eco_nut = 0
eco_neg = 0

for i in range(5):
    eco_pos += main.cat_result_all[i + 15].count(1)
    eco_nut += main.cat_result_all[i + 15].count(2)
    eco_neg += main.cat_result_all[i + 15].count(0)

eco_pos = eco_pos * 4
eco_nut = eco_nut * 4
eco_neg = eco_neg * 4

lif_pos = 0
lif_nut = 0
lif_neg = 0

for i in range(5):
    lif_pos += main.cat_result_all[i + 20].count(1)
    lif_nut += main.cat_result_all[i + 20].count(2)
    lif_neg += main.cat_result_all[i + 20].count(0)

lif_pos = lif_pos * 4
lif_nut = lif_nut * 4
lif_neg = lif_neg * 4

wor_pos = 0
wor_nut = 0
wor_neg = 0

for i in range(5):
    wor_pos += main.cat_result_all[i + 25].count(1)
    wor_nut += main.cat_result_all[i + 25].count(2)
    wor_neg += main.cat_result_all[i + 25].count(0)

wor_pos = wor_pos * 4
wor_nut = wor_nut * 4
wor_neg = wor_neg * 4

its_pos = 0
its_nut = 0
its_neg = 0

for i in range(5):
    its_pos += main.cat_result_all[i + 30].count(1)
    its_nut += main.cat_result_all[i + 30].count(2)
    its_neg += main.cat_result_all[i + 30].count(0)

its_pos = its_pos * 4
its_nut = its_nut * 4
its_neg = its_neg * 4

all_list = main.cat_result_all

def openTopicName(categori):
    name_list = list()
    for i in range(5):
        tmp_text = ''
        with open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/result/" + categori + "/" + categori + f"_result{i + 1}_name.txt",encoding="utf-8") as f:
            tmp_text = f.read()
            name_list.append(tmp_text)
    return name_list

# Create your views here.

def 전체(request):
    allName = openTopicName("all")
    ex1 = allName[0]

    ex2 = allName[1]

    ex3 = allName[2]

    ex4 = allName[3]

    ex5 = allName[4]


    return render(request, 'news/전체.html', {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': all_tl[0],'sum1_2': all_tl[1], 'sum1_3': all_tl[2], 'sum1_4': all_tl[3], 'sum1_5': all_tl[4],
                   'sum2_1': all_tl[5],'sum2_2': all_tl[6], 'sum2_3': all_tl[7], 'sum2_4': all_tl[8], 'sum2_5': all_tl[9],
                   'sum3_1': all_tl[10],'sum3_2': all_tl[11], 'sum3_3': all_tl[12], 'sum3_4': all_tl[13], 'sum3_5': all_tl[14],
                   'sum4_1': all_tl[15],'sum4_2': all_tl[16], 'sum4_3': all_tl[17], 'sum4_4': all_tl[18], 'sum4_5': all_tl[19],
                   'sum5_1': all_tl[20],'sum5_2': all_tl[21], 'sum5_3': all_tl[22], 'sum5_4': all_tl[23], 'sum5_5': all_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[0][0],'sent1_2' : all_list[0][1],'sent1_3' : all_list[0][2],
                    'sent1_4': all_list[0][3],'sent1_5' : all_list[0][4],'sent2_1' : all_list[1][0],'sent2_2' : all_list[1][1],
                    'sent2_3': all_list[1][2],'sent2_4' : all_list[1][3],'sent2_5' : all_list[1][4],'sent3_1' : all_list[2][0],
                    'sent3_2': all_list[2][1],'sent3_3' : all_list[2][2],'sent3_4' : all_list[2][3],'sent3_5' : all_list[2][4],
                    'sent4_1': all_list[3][0],'sent4_2' : all_list[3][1],'sent4_3' : all_list[3][2],'sent4_4' : all_list[3][3],
                    'sent4_5': all_list[3][4],'sent5_1' : all_list[4][0],'sent5_2' : all_list[4][1],'sent5_3' : all_list[4][2],
                    'sent5_4': all_list[4][3],'sent5_5' : all_list[4][4],
                    'txt1_1': all[0], 'txt1_2': all[1] , 'txt1_3': all[2] , 'txt1_4': all[3] , 'txt1_5': all[4] ,
                   'txt2_1': all[5], 'txt2_2': all[6] , 'txt2_3': all[7] , 'txt2_4': all[8] , 'txt2_5': all[9] ,
                   'txt3_1': all[10], 'txt3_2': all[11] , 'txt3_3': all[12] , 'txt3_4': all[13] , 'txt3_5': all[14] ,
                   'txt4_1': all[15], 'txt4_2': all[16] , 'txt4_3': all[17] , 'txt4_4': all[18] , 'txt4_5': all[19] ,
                   'txt5_1': all[20], 'txt5_2': all[21] , 'txt5_3': all[22] , 'txt5_4': all[23] , 'txt5_5': all[24]
                    })

def 정치(request):
    polName = openTopicName("pol")
    ex1 = polName[0]

    ex2 = polName[1]

    ex3 = polName[2]

    ex4 = polName[3]

    ex5 = polName[4]


    return render(request, 'news/정치.html',
                  {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': pol_tl[0],'sum1_2': pol_tl[1], 'sum1_3': pol_tl[2], 'sum1_4': pol_tl[3], 'sum1_5': pol_tl[4],
                   'sum2_1': pol_tl[5],'sum2_2': pol_tl[6], 'sum2_3': pol_tl[7], 'sum2_4': pol_tl[8], 'sum2_5': pol_tl[9],
                   'sum3_1': pol_tl[10],'sum3_2': pol_tl[11], 'sum3_3': pol_tl[12], 'sum3_4': pol_tl[13], 'sum3_5': pol_tl[14],
                   'sum4_1': pol_tl[15],'sum4_2': pol_tl[16], 'sum4_3': pol_tl[17], 'sum4_4': pol_tl[18], 'sum4_5': pol_tl[19],
                   'sum5_1': pol_tl[20],'sum5_2': pol_tl[21], 'sum5_3': pol_tl[22], 'sum5_4': pol_tl[23], 'sum5_5': pol_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[5][0],'sent1_2' : all_list[5][1],'sent1_3' : all_list[5][2],
                    'sent1_4': all_list[5][3],'sent1_5' : all_list[5][4],'sent2_1' : all_list[6][0],'sent2_2' : all_list[6][1],
                    'sent2_3': all_list[6][2],'sent2_4' : all_list[6][3],'sent2_5' : all_list[6][4],'sent3_1' : all_list[7][0],
                    'sent3_2': all_list[7][1],'sent3_3' : all_list[7][2],'sent3_4' : all_list[7][3],'sent3_5' : all_list[7][4],
                    'sent4_1': all_list[8][0],'sent4_2' : all_list[8][1],'sent4_3' : all_list[8][2],'sent4_4' : all_list[8][3],
                    'sent4_5': all_list[8][4],'sent5_1' : all_list[9][0],'sent5_2' : all_list[9][1],'sent5_3' : all_list[9][2],
                    'sent5_4': all_list[9][3],'sent5_5' : all_list[9][4],
                   'txt1_1': pol[0], 'txt1_2': pol[1], 'txt1_3': pol[2], 'txt1_4': pol[3], 'txt1_5': pol[4],
                   'txt2_1': pol[5], 'txt2_2': pol[6], 'txt2_3': pol[7], 'txt2_4': pol[8], 'txt2_5': pol[9],
                   'txt3_1': pol[10], 'txt3_2': pol[11], 'txt3_3': pol[12], 'txt3_4': pol[13], 'txt3_5': pol[14],
                   'txt4_1': pol[15], 'txt4_2': pol[16], 'txt4_3': pol[17], 'txt4_4': pol[18], 'txt4_5': pol[19],
                   'txt5_1': pol[20], 'txt5_2': pol[21], 'txt5_3': pol[22], 'txt5_4': pol[23], 'txt5_5': pol[24]
                   })
def 사회(request):
    socName = openTopicName("soc")
    ex1 = socName[0]

    ex2 = socName[1]

    ex3 = socName[2]

    ex4 = socName[3]

    ex5 = socName[4]


    return render(request, 'news/사회.html',
                  {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': soc_tl[0],'sum1_2': soc_tl[1], 'sum1_3': soc_tl[2], 'sum1_4': soc_tl[3], 'sum1_5': soc_tl[4],
                   'sum2_1': soc_tl[5],'sum2_2': soc_tl[6], 'sum2_3': soc_tl[7], 'sum2_4': soc_tl[8], 'sum2_5': soc_tl[9],
                   'sum3_1': soc_tl[10],'sum3_2': soc_tl[11], 'sum3_3': soc_tl[12], 'sum3_4': soc_tl[13], 'sum3_5': soc_tl[14],
                   'sum4_1': soc_tl[15],'sum4_2': soc_tl[16], 'sum4_3': soc_tl[17], 'sum4_4': soc_tl[18], 'sum4_5': soc_tl[19],
                   'sum5_1': soc_tl[20],'sum5_2': soc_tl[21], 'sum5_3': soc_tl[22], 'sum5_4': soc_tl[23], 'sum5_5': soc_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[10][0],'sent1_2' : all_list[10][1],'sent1_3' : all_list[10][2],
                    'sent1_4': all_list[10][3],'sent1_5' : all_list[10][4],'sent2_1' : all_list[11][0],'sent2_2' : all_list[11][1],
                    'sent2_3': all_list[11][2],'sent2_4' : all_list[11][3],'sent2_5' : all_list[11][4],'sent3_1' : all_list[12][0],
                    'sent3_2': all_list[12][1],'sent3_3' : all_list[12][2],'sent3_4' : all_list[12][3],'sent3_5' : all_list[12][4],
                    'sent4_1': all_list[13][0],'sent4_2' : all_list[13][1],'sent4_3' : all_list[13][2],'sent4_4' : all_list[13][3],
                    'sent4_5': all_list[13][4],'sent5_1' : all_list[14][0],'sent5_2' : all_list[14][1],'sent5_3' : all_list[14][2],
                    'sent5_4': all_list[14][3],'sent5_5' : all_list[14][4],
                   'txt1_1': soc[0], 'txt1_2': soc[1], 'txt1_3': soc[2], 'txt1_4': soc[3], 'txt1_5': soc[4],
                   'txt2_1': soc[5], 'txt2_2': soc[6], 'txt2_3': soc[7], 'txt2_4': soc[8], 'txt2_5': soc[9],
                   'txt3_1': soc[10], 'txt3_2': soc[11], 'txt3_3': soc[12], 'txt3_4': soc[13], 'txt3_5': soc[14],
                   'txt4_1': soc[15], 'txt4_2': soc[16], 'txt4_3': soc[17], 'txt4_4': soc[18], 'txt4_5': soc[19],
                   'txt5_1': soc[20], 'txt5_2': soc[21], 'txt5_3': soc[22], 'txt5_4': soc[23], 'txt5_5': soc[24]
                   })
def 경제(request):
    ecoName = openTopicName("eco")
    ex1 = ecoName[0]

    ex2 = ecoName[1]

    ex3 = ecoName[2]

    ex4 = ecoName[3]

    ex5 = ecoName[4]



    return render(request, 'news/경제.html',
                  {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': eco_tl[0],'sum1_2': eco_tl[1], 'sum1_3': eco_tl[2], 'sum1_4': eco_tl[3], 'sum1_5': eco_tl[4],
                   'sum2_1': eco_tl[5],'sum2_2': eco_tl[6], 'sum2_3': eco_tl[7], 'sum2_4': eco_tl[8], 'sum2_5': eco_tl[9],
                   'sum3_1': eco_tl[10],'sum3_2': eco_tl[11], 'sum3_3': eco_tl[12], 'sum3_4': eco_tl[13], 'sum3_5': eco_tl[14],
                   'sum4_1': eco_tl[15],'sum4_2': eco_tl[16], 'sum4_3': eco_tl[17], 'sum4_4': eco_tl[18], 'sum4_5': eco_tl[19],
                   'sum5_1': eco_tl[20],'sum5_2': eco_tl[21], 'sum5_3': eco_tl[22], 'sum5_4': eco_tl[23], 'sum5_5': eco_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[15][0],'sent1_2' : all_list[15][1],'sent1_3' : all_list[15][2],
                    'sent1_4': all_list[15][3],'sent1_5' : all_list[15][4],'sent2_1' : all_list[16][0],'sent2_2' : all_list[16][1],
                    'sent2_3': all_list[16][2],'sent2_4' : all_list[16][3],'sent2_5' : all_list[16][4],'sent3_1' : all_list[17][0],
                    'sent3_2': all_list[17][1],'sent3_3' : all_list[17][2],'sent3_4' : all_list[17][3],'sent3_5' : all_list[17][4],
                    'sent4_1': all_list[18][0],'sent4_2' : all_list[18][1],'sent4_3' : all_list[18][2],'sent4_4' : all_list[18][3],
                    'sent4_5': all_list[18][4],'sent5_1' : all_list[19][0],'sent5_2' : all_list[19][1],'sent5_3' : all_list[19][2],
                    'sent5_4': all_list[19][3],'sent5_5' : all_list[19][4],
                   'txt1_1': eco[0], 'txt1_2': eco[1], 'txt1_3': eco[2], 'txt1_4': eco[3], 'txt1_5': eco[4],
                   'txt2_1': eco[5], 'txt2_2': eco[6], 'txt2_3': eco[7], 'txt2_4': eco[8], 'txt2_5': eco[9],
                   'txt3_1': eco[10], 'txt3_2': eco[11], 'txt3_3': eco[12], 'txt3_4': eco[13], 'txt3_5': eco[14],
                   'txt4_1': eco[15], 'txt4_2': eco[16], 'txt4_3': eco[17], 'txt4_4': eco[18], 'txt4_5': eco[19],
                   'txt5_1': eco[20], 'txt5_2': eco[21], 'txt5_3': eco[22], 'txt5_4': eco[23], 'txt5_5': eco[24]
                   })
def 생활문화(request):
    lifName = openTopicName("lif")
    ex1 = lifName[0]

    ex2 = lifName[1]

    ex3 = lifName[2]

    ex4 = lifName[3]

    ex5 = lifName[4]



    return render(request, 'news/생활문화.html',
                  {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': lif_tl[0],'sum1_2': lif_tl[1], 'sum1_3': lif_tl[2], 'sum1_4': lif_tl[3], 'sum1_5': lif_tl[4],
                   'sum2_1': lif_tl[5],'sum2_2': lif_tl[6], 'sum2_3': lif_tl[7], 'sum2_4': lif_tl[8], 'sum2_5': lif_tl[9],
                   'sum3_1': lif_tl[10],'sum3_2': lif_tl[11], 'sum3_3': lif_tl[12], 'sum3_4': lif_tl[13], 'sum3_5': lif_tl[14],
                   'sum4_1': lif_tl[15],'sum4_2': lif_tl[16], 'sum4_3': lif_tl[17], 'sum4_4': lif_tl[18], 'sum4_5': lif_tl[19],
                   'sum5_1': lif_tl[20],'sum5_2': lif_tl[21], 'sum5_3': lif_tl[22], 'sum5_4': lif_tl[23], 'sum5_5': lif_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[20][0],'sent1_2' : all_list[20][1],'sent1_3' : all_list[20][2],
                    'sent1_4': all_list[20][3],'sent1_5' : all_list[20][4],'sent2_1' : all_list[21][0],'sent2_2' : all_list[21][1],
                    'sent2_3': all_list[21][2],'sent2_4' : all_list[21][3],'sent2_5' : all_list[21][4],'sent3_1' : all_list[22][0],
                    'sent3_2': all_list[22][1],'sent3_3' : all_list[22][2],'sent3_4' : all_list[22][3],'sent3_5' : all_list[22][4],
                    'sent4_1': all_list[23][0],'sent4_2' : all_list[23][1],'sent4_3' : all_list[23][2],'sent4_4' : all_list[23][3],
                    'sent4_5': all_list[23][4],'sent5_1' : all_list[24][0],'sent5_2' : all_list[24][1],'sent5_3' : all_list[24][2],
                    'sent5_4': all_list[24][3],'sent5_5' : all_list[24][4],
                   'txt1_1': lif[0], 'txt1_2': lif[1], 'txt1_3': lif[2], 'txt1_4': lif[3], 'txt1_5': lif[4],
                   'txt2_1': lif[5], 'txt2_2': lif[6], 'txt2_3': lif[7], 'txt2_4': lif[8], 'txt2_5': lif[9],
                   'txt3_1': lif[10], 'txt3_2': lif[11], 'txt3_3': lif[12], 'txt3_4': lif[13], 'txt3_5': lif[14],
                   'txt4_1': lif[15], 'txt4_2': lif[16], 'txt4_3': lif[17], 'txt4_4': lif[18], 'txt4_5': lif[19],
                   'txt5_1': lif[20], 'txt5_2': lif[21], 'txt5_3': lif[22], 'txt5_4': lif[23], 'txt5_5': lif[24]
                   })
def 세계(request):
    worName = openTopicName("wor")
    ex1 = worName[0]

    ex2 = worName[1]

    ex3 = worName[2]

    ex4 = worName[3]

    ex5 = worName[4]



    return render(request, 'news/세계.html',
                  {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': wor_tl[0],'sum1_2': wor_tl[1], 'sum1_3': wor_tl[2], 'sum1_4': wor_tl[3], 'sum1_5': wor_tl[4],
                   'sum2_1': wor_tl[5],'sum2_2': wor_tl[6], 'sum2_3': wor_tl[7], 'sum2_4': wor_tl[8], 'sum2_5': wor_tl[9],
                   'sum3_1': wor_tl[10],'sum3_2': wor_tl[11], 'sum3_3': wor_tl[12], 'sum3_4': wor_tl[13], 'sum3_5': wor_tl[14],
                   'sum4_1': wor_tl[15],'sum4_2': wor_tl[16], 'sum4_3': wor_tl[17], 'sum4_4': wor_tl[18], 'sum4_5': wor_tl[19],
                   'sum5_1': wor_tl[20],'sum5_2': wor_tl[21], 'sum5_3': wor_tl[22], 'sum5_4': wor_tl[23], 'sum5_5': wor_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[25][0],'sent1_2' : all_list[25][1],'sent1_3' : all_list[25][2],
                    'sent1_4': all_list[25][3],'sent1_5' : all_list[25][4],'sent2_1' : all_list[26][0],'sent2_2' : all_list[26][1],
                    'sent2_3': all_list[26][2],'sent2_4' : all_list[26][3],'sent2_5' : all_list[26][4],'sent3_1' : all_list[27][0],
                    'sent3_2': all_list[27][1],'sent3_3' : all_list[27][2],'sent3_4' : all_list[27][3],'sent3_5' : all_list[27][4],
                    'sent4_1': all_list[28][0],'sent4_2' : all_list[28][1],'sent4_3' : all_list[28][2],'sent4_4' : all_list[28][3],
                    'sent4_5': all_list[28][4],'sent5_1' : all_list[29][0],'sent5_2' : all_list[29][1],'sent5_3' : all_list[29][2],
                    'sent5_4': all_list[29][3],'sent5_5' : all_list[29][4],
                   'txt1_1': wor[0], 'txt1_2': wor[1], 'txt1_3': wor[2], 'txt1_4': wor[3], 'txt1_5': wor[4],
                   'txt2_1': wor[5], 'txt2_2': wor[6], 'txt2_3': wor[7], 'txt2_4': wor[8], 'txt2_5': wor[9],
                   'txt3_1': wor[10], 'txt3_2': wor[11], 'txt3_3': wor[12], 'txt3_4': wor[13], 'txt3_5': wor[14],
                   'txt4_1': wor[15], 'txt4_2': wor[16], 'txt4_3': wor[17], 'txt4_4': wor[18], 'txt4_5': wor[19],
                   'txt5_1': wor[20], 'txt5_2': wor[21], 'txt5_3': wor[22], 'txt5_4': wor[23], 'txt5_5': wor[24]
                   })
def IT과학(request):
    itsName = openTopicName("its")
    ex1 = itsName[0]

    ex2 = itsName[1]

    ex3 = itsName[2]

    ex4 = itsName[3]

    ex5 = itsName[4]



    return render(request, 'news/IT과학.html',
                  {'example1': ex1, 'example2': ex2, 'example3': ex3, 'example4': ex4, 'example5': ex5,
                   'sum1_1': its_tl[0],'sum1_2': its_tl[1], 'sum1_3': its_tl[2], 'sum1_4': its_tl[3], 'sum1_5': its_tl[4],
                   'sum2_1': its_tl[5],'sum2_2': its_tl[6], 'sum2_3': its_tl[7], 'sum2_4': its_tl[8], 'sum2_5': its_tl[9],
                   'sum3_1': its_tl[10],'sum3_2': its_tl[11], 'sum3_3': its_tl[12], 'sum3_4': its_tl[13], 'sum3_5': its_tl[14],
                   'sum4_1': its_tl[15],'sum4_2': its_tl[16], 'sum4_3': its_tl[17], 'sum4_4': its_tl[18], 'sum4_5': its_tl[19],
                   'sum5_1': its_tl[20],'sum5_2': its_tl[21], 'sum5_3': its_tl[22], 'sum5_4': its_tl[23], 'sum5_5': its_tl[24],
                   'pos1': all_pos,'nut1': all_nut,'neg1': all_neg,'pos2': pol_pos, 'nut2': pol_nut, 'neg2': pol_neg,
                   'pos3': soc_pos, 'nut3': soc_nut, 'neg3': soc_neg,'pos4': eco_pos, 'nut4': eco_nut, 'neg4': eco_neg,
                   'pos5': lif_pos, 'nut5': lif_nut, 'neg5': lif_neg,'pos6': wor_pos, 'nut6': wor_nut, 'neg6': wor_neg,
                   'pos7': its_pos, 'nut7': its_nut, 'neg7': its_neg,'sent1_1' : all_list[30][0],'sent1_2' : all_list[30][1],'sent1_3' : all_list[30][2],
                    'sent1_4': all_list[30][3],'sent1_5' : all_list[30][4],'sent2_1' : all_list[31][0],'sent2_2' : all_list[31][1],
                    'sent2_3': all_list[31][2],'sent2_4' : all_list[31][3],'sent2_5' : all_list[31][4],'sent3_1' : all_list[32][0],
                    'sent3_2': all_list[32][1],'sent3_3' : all_list[32][2],'sent3_4' : all_list[32][3],'sent3_5' : all_list[32][4],
                    'sent4_1': all_list[33][0],'sent4_2' : all_list[33][1],'sent4_3' : all_list[33][2],'sent4_4' : all_list[33][3],
                    'sent4_5': all_list[33][4],'sent5_1' : all_list[34][0],'sent5_2' : all_list[34][1],'sent5_3' : all_list[34][2],
                    'sent5_4': all_list[34][3],'sent5_5' : all_list[34][4],
                   'txt1_1': its[0], 'txt1_2': its[1], 'txt1_3': its[2], 'txt1_4': its[3], 'txt1_5': its[4],
                   'txt2_1': its[5], 'txt2_2': its[6], 'txt2_3': its[7], 'txt2_4': its[8], 'txt2_5': its[9],
                   'txt3_1': its[10], 'txt3_2': its[11], 'txt3_3': its[12], 'txt3_4': its[13], 'txt3_5': its[14],
                   'txt4_1': its[15], 'txt4_2': its[16], 'txt4_3': its[17], 'txt4_4': its[18], 'txt4_5': its[19],
                   'txt5_1': its[20], 'txt5_2': its[21], 'txt5_3': its[22], 'txt5_4': its[23], 'txt5_5': its[24]
                   })