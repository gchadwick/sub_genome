from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from random import randint
import string
genome_file = raw_input('File with complete genomes: ')
fragment_size = input('Length of sub sequence: ')
sub_genomes = []
genome_records = SeqIO.parse(open(genome_file,'rU'), 'fasta')
for genome in genome_records:
	print genome.name
	start = randint(0,len(genome.seq) - fragment_size)
	end = start + fragment_size
	sub_genome = genome.seq[start:end]
	sub_record = SeqRecord(sub_genome,str(genome.name),'','')
	sub_genomes.append(sub_record)
path = genome_file[0:string.rfind(genome_file,'/')+1]
out_file = path + 'sub_' + str(fragment_size) + '_' + genome_file[string.rfind(genome_file,'/')+1:len(genome_file)]
output_handle = open(out_file,'w')
SeqIO.write(sub_genomes,output_handle,'fasta')
output_handle.close()