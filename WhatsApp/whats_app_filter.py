import numpy as np
import pandas as pd
import re

# Approach:
# Data filtering and cleaning
# 1. Extract statistical data  
# 2. Stats: 1. Time between messages, 2. Dispersion of messages in month, day, hour   
# 3. Senders
# 4. Media (audio/pics)posted
# 5. message length(by time, person )
# 6. key words: laughing, (time,person,  )
# 7. 
# Finally: use NLP for text meaning for English convs =>Semantic Analysis => http://textacy.readthedocs.io/en/latest/
class Data(self):
    def __init__(self):

    def cleanup(self):
    #import data
    whatsapp=pd.read_table('_chat_ali.txt', header=None)
    #delimit by ':'
    for i in range(len(whatsapp)):
        whatsapp.ix[i,0]=re.sub(r'(:)(?!$)', r'\1,', whatsapp.ix[i,0])
    whatsapp[0] = whatsapp[0].str.replace(r'\:','')
    whatsapp['Date']=whatsapp[0].str.split(',')
    for j in range(len(whatsapp)):
        if len(whatsapp.ix[j,'Date'])==7:
            whatsapp.ix[j,'Date'][5]=(whatsapp.ix[j,'Date'][5]+','+whatsapp.ix[j,'Date'][6])
            del whatsapp.ix[j,'Date'][6]
        if len(whatsapp.ix[j,'Date'])==8:
            whatsapp.ix[j,'Date'][5]=(whatsapp.ix[j,'Date'][5]+','+whatsapp.ix[j,'Date'][6]+','+whatsapp.ix[j,'Date'][7])
            del whatsapp.ix[j,'Date'][6]
        if len(whatsapp.ix[j,'Date'])==9:
            whatsapp.ix[j,'Date'][5]=(whatsapp.ix[j,'Date'][5]+','+whatsapp.ix[j,'Date'][6]+','+whatsapp.ix[j,'Date'][7]+','+whatsapp.ix[j,'Date'][8])
            del whatsapp.ix[j,'Date'][6]
            del whatsapp.ix[j,'Date'][7]
    data_array=[whatsapp.ix[i,'Date']for i in range(len(whatsapp)) if len(whatsapp.ix[i,'Date'])<7]
    data_array_full=[whatsapp.ix[i,'Date']for i in range(len(whatsapp))if len(whatsapp.ix[i,'Date'])>6]

    data=pd.DataFrame( data_array, columns=["Date","Hour", "Minute", "Seconds", 'Sender', 'Message'])

        return data