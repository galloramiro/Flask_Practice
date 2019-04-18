
import pandas as pd
from dataloader import db
from dataloader.models import GenData


def decodeTranscript(x):
    '''
    This function decode the transcript putting the right name of the gene
    '''
    gen = x.split('_')[0]
    gen_d = {'chr17':'BRCA1', 'chr16':'PALB2','chr13':'BRCA2','chr11':'ATM','chr2':'MSH2', }
    return gen_d[gen]


def dataToDb(df):
    df = pd.read_csv(df, delimiter='\t')
    
    df.rename(columns={'add2':'Tries','add3':'Genes_N'},inplace=True)
    df['Genes'] = df['transcript'].apply(lambda x: decodeTranscript(x)) 
    df['Tries'] = df['Tries'].apply(lambda x: str('{:02d}'.format(x)))
    df['Tries'] = df['sampleID'].str.cat(df['Tries'],sep=" ")              

    for gen, test, tpm in zip(df['Genes'], df['Tries'], df['TPM']):
        row = GenData(gen=gen, test=test, tpm=tpm)
        db.session.add(row)
    
    db.session.commit()
    return 'Done'

