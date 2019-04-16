import pandas as pd


def decodeTranscript(x):
    '''
    This function decode the transcript putting the right name of the gene
    '''
    gen = x.split('_')[0]
    gen_d = {'chr17':'_BRCA1', 'chr16':'_PALB2','chr13':'_BRCA2','chr11':'_ATM','chr2':'_MSH2', }
    return gen_d[gen]


def csvToDb(df):
    df = pd.read_csv(df, delimiter='\t')
    
    df.rename(columns={'add2':'Tries','add3':'Genes_N'},inplace=True)
    df['Genes'] = df['transcript'].apply(lambda x: decodeTranscript(x)) 
    df['Tries'] = df['Tries'].apply(lambda x: str('{:02d}'.format(x)))
    df['Tries'] = df['sampleID'].str.cat(df['Tries'],sep=" ")              
    d_data = {'gen':[], 'test':[], 'tpm':[],}

    for gen, test, tmp in zip(df['Genes'], df['Tries'], df['TPM']):
        d_data['gen'].append(gen)
        d_data['test'].append(test)
        d_data['tpm'].append(tmp)

    return d_data

#csvToDb('./scater_dataOK_revisado.txt')