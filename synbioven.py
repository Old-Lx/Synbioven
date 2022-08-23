#Programa para procesamiento de secuencias de ADN
from Bio.Seq import Seq
from Bio import SeqIO

#Nótese que apenas estoy empezando a usar esta librería, cualquier
#recomendación será bien recibida

def com_fasta(archivo):
    print("Ejecutando...")
    secs=list(SeqIO.parse(archivo, "fasta"))
    with open("sec_sin_rep.fasta", "w") as new_fasta:
        for sec_n in secs:
            for ind_2, adn_2 in enumerate(SeqIO.parse(archivo, "fasta")):
                if len(secs)!=ind_2:
                    if sec_n.seq==adn_2[ind_2+1]:
                        SeqIO.write(adn_2, new_fasta, "fasta")


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
        '''with open(f_name+".txt", "w") as cur_seq:
                cur_seq.write(dna_seq)'''

if __name__ == '__main__':
    div_fasta("Lemna_minor.fasta")
    com_fasta("Lemna_minor.fasta")

#antes de publicar, hay que citar a los autores de biopython
#y a los cursos que lo explican en español
#https://biopython.org/ y 
#https://bioinf.comav.upv.es/courses/linux/python/biopython.html