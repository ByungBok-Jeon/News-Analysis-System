import lda
from gensim.summarization.summarizer import summarize


tl_pol=list(); tl_eco=list() ;tl_soc=list() ;tl_lif=list() ;tl_wor=list() ;tl_its=list(); tl_all=list()
tl_pol=lda.TPM(tl_pol,"pol"); tl_eco=lda.TPM(tl_eco,"eco"); tl_soc = lda.TPM(tl_soc,"soc"); tl_lif = lda.TPM(tl_lif,"lif"); tl_wor = lda.TPM(tl_wor,"wor"); tl_its = lda.TPM(tl_its,"its"); tl_all = lda.TPM(tl_all,"all")

def save_result(tl,categori):
    for i in range(5):
        for j in range(5):
            f = open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/result/"+categori+"/"+categori+f"_result{i+1}_{j+1}.txt", "w", encoding="UTF8")
            f.write(tl[i][j])
            f.close()

save_result(tl_pol,"pol")
save_result(tl_eco,"eco")
save_result(tl_soc,"soc")
save_result(tl_lif,"lif")
save_result(tl_wor,"wor")
save_result(tl_its,"its")
save_result(tl_all,"all")
