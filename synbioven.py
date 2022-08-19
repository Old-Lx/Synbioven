#Programa para procesamiento de secuencias de ADN
from Bio.Seq import Seq
from Bio import SeqIO

#Nótese que apenas estoy empezando a usar esta librería, cualquier
#recomendación será bien recibida

#Función usada para dividir todas las secuencias de un archivo
#fasta en varios archivos fasta
def div_fasta():
    #estoy iterando sobre el archivo fasta para dividir cada secuencia
    #la librería que importé tiene todas las herramientas necesarias para
    #manipular archivos fasta
    with open(input("Ruta del archivo fasta: ")) as handle:
        for dna_seq in SeqIO.parse(handle, "fasta"):
            f_name="secuencia_"+str(dna_seq.id)
            with open(f_name+".fasta", "w") as cur_seq:
                cur_seq.write(dna_seq)




#antes de publicar, hay que citar a los autores de biopython
#y a los cursos que lo explican en español
#https://biopython.org/ y 
#https://bioinf.comav.upv.es/courses/linux/python/biopython.html