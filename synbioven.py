#Programa para procesamiento de secuencias de ADN
from Bio.Seq import Seq
from Bio import SeqIO

#Nótese que apenas estoy empezando a usar esta librería, cualquier
#recomendación será bien recibida

#Esta función crea un nuevo fasta sin secuencias repetidas
def limp_rep(archivo):
    print("Ejecutando...")
    secs=list(SeqIO.parse(archivo, "fasta"))
    with open("sec_rep.fasta", "w") as new_fasta:    
        n=1
        rep_id=[]
        for adn_2 in SeqIO.parse(archivo, "fasta"):
            for sec_n in secs[n:]:
                if sec_n.seq==adn_2.seq:
                    rep_id[n]=sec_n.id
                print('Analizando secuencia '+n+' de '+str(len(secs)))
            n=n+1
            if len(secs)==n:
                break
        for adn_2 in SeqIO.parse(archivo, "fasta"):
            for id in rep_id:
                if adn_2.id==id:
                    SeqIO.write(adn_2, new_fasta, "fasta")

#Esta función guarda un nuevo fasta con los mismos elementos que el original
#pero excluyendo las secuencias repetidas que guardamos con recon_rep donde arc_comp es
#el archivo completo y arc_sec_rep es el archivo con las secuencias que están repetidas
'''def elim_rep(arc_comp, arc_sec_rep):
    print("Ejecutando...")
    secs=list(SeqIO.parse(arc_comp, "fasta"))
    with open(arc_sec_rep) as reps:    
        for ind in len(secs)-1:
            with open("sec_sin_rep.fasta", "w") as n_fasta:
                if secs[ind].seq!=reps[ind]:
                    SeqIO.write(secs[ind], n_fasta, "fasta")

            



#Función usada para dividir todas las secuencias de un archivo
#fasta en varios archivos fasta
def div_fasta(archivo):
    #estoy iterando sobre el archivo fasta para dividir cada secuencia
    #la librería que importé tiene todas las herramientas necesarias para
    #manipular archivos fasta
    print("Ejecutando...")
    with open(archivo) as handle:
        for indice, adn_sec in enumerate(SeqIO.parse(handle, "fasta")):
            print(str(len(adn_sec.seq)))
            break
        with open(f_name+".txt", "w") as cur_seq:
                cur_seq.write(dna_seq)'''

if __name__ == '__main__':
    limp_rep("Lemna_minor.fasta")
    '''recon_rep("Lemna_minor.fasta")
    elim_rep(str(), str())'''

#antes de publicar, hay que citar a los autores de biopython
#y a los cursos que lo explican en español
#https://biopython.org/ y 
#https://bioinf.comav.upv.es/courses/linux/python/biopython.html