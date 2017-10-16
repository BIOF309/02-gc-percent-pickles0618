
# coding: utf-8

# In[10]:

'''This script calculates the GC content of a given DNA sequence'''
input_DNA = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
input_DNA = input_DNA.upper()

G_occur = input_DNA.count('G') #count the number of G's
C_occur = input_DNA.count('C') #count the number of C's
DNA_len = len(input_DNA) #length of the input_DNA
GC_content = round((G_occur + C_occur)/DNA_len*100,2) # % of GC content

print('The GC concent of the given DNA sequence is ' + str(GC_content) +'%')

