from nltk.corpus import wordnet as wn
import pandas as pd

def pprocess(x):

    if x['classt1'] == 'metaphoric':
        meta_example = x['sentencet1']
        meta_term = x['term1']
        literal_term = x['term2']
        literal_example = x['sentencet2']
        meta_is_the_first = True

    else:
        meta_is_the_first = False
        meta_example = x['sentencet2']
        meta_term = x['term2']
        literal_term = x['term1']
        literal_example = x['sentencet1']

    meta_more_emotional = x['meta_more_emotional']
    specificity = x['specificity']
    common_hyper = x['common_hyper']
    if common_hyper == "'see 2D'":
        common_hyper = ''
    if pd.isna(common_hyper):
        return pd.Series({
        'meta_term' : meta_term,
        'meta_example' : meta_example,
        'literal_term' : literal_term,
        'literal_example' : literal_example,
        'meta_is_more_emotiona' : meta_more_emotional,
        'common_hyper' : '',
        'specificity' : specificity
    })
    all_cols = ['common_hyper'] + [i for i in x.keys() if 'Unnamed' in i ]
    if common_hyper.startswith('-'):
        if not meta_is_the_first:
            hyper_string = ''
            for col in all_cols:
                if col == 'common_hyper':
                    cs = x[col][1:]
                else:
                    cs = x[col]
                if pd.isna(cs):
                    continue
                cs = eval(cs)
                new_cs = tuple([cs[0], cs[2], cs[1], cs[4], cs[3]])
                hyper_string += str(new_cs)
                hyper_string += '\t'
        else:
            hyper_string = ''
            for col in all_cols:
                if col == 'common_hyper':
                    hyper_string += str(x[col][1:])
                    hyper_string += '\t'
                else:
                    if pd.isna(x[col]):
                        continue
                    hyper_string += str(x[col])
                    hyper_string += '\t'
    else:
        hyper_string = ''
        for col in all_cols:
            if pd.isna(x[col]):
                continue
            hyper_string += str(x[col])
            hyper_string += '\t'
    return pd.Series({
        'meta_term' : meta_term,
        'meta_example' : meta_example,
        'literal_term' : literal_term,
        'literal_example' : literal_example,
        'meta_is_more_emotiona' : meta_more_emotional,
        'common_hyper' : hyper_string,
        'specificity' : specificity
    })

if __name__ == '__main__':

    df = pd.read_csv('emotional_wordnet_1D.tsv', sep='\t')
    Synset = wn.synset

    df2 = df.apply(pprocess, axis = 1)
    common_hyper = df2['common_hyper']
    df2 = df2.drop(columns=['common_hyper'])
    df2.to_csv('specificity.tsv', sep='\t', index=False)

    with open('common.tsv', 'w') as f:
        for i in common_hyper:
            f.write(i+'\n')

    print('Finish')