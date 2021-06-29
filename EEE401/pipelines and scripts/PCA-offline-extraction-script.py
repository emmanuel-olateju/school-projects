import pylsl
from pylsl import StreamInfo,StreamInlet, StreamOutlet, resolve_stream
import csv
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



#info=StreamInfo(name='PCA-OutStream', type='EEG', channel_count=8, channel_format='int32', source_id='PCA')

def main():
    
    #SEARCH FOR EEG STREAM
    print("looking for an EEG stream...")
    streams=resolve_stream('name', 'PCA-testStream')
    eeg_info=streams[0]
    eeg_info=streams[0]
    PCA_inlet=StreamInlet(eeg_info)
    print(eeg_info.name(),eeg_info.type(),"\n")

    #SEARCH FOR MARKER STREAM
    marker_stream=resolve_stream('name', 'PCA-testStream-Markers')
    marker_info=marker_stream[0]
    MARKER_inlet=StreamInlet(marker_stream[0])
    print(marker_info.name(),marker_info.type())
    
    marker, marker_timestamp=MARKER_inlet.pull_sample()
    print("marker:",marker_timestamp,marker,"\n")
    i=0
    # format of test_data=> [['A1A', 'A2A', 'A3A', 'A4A', 'A4B', 'A3B', 'A2B', 'A1B','timestamp','marker','i']]
    test_data=[]
    if marker==['calib-begin']:
        print('stream acquired,acqusition ongoing........',"\n")
        while marker!=['calib-end']:
            sample, timestamp=PCA_inlet.pull_sample()
            marker, marker_timestamp=MARKER_inlet.pull_sample()
            test_data.append([sample[0], sample[1], sample[2], sample[3], sample[4], sample[5], sample[6], sample[7], marker_timestamp, marker[0],i])
            i=i+1
        
    test_df=pd.DataFrame(test_data,columns=['A1A', 'A2A', 'A3A', 'A4A', 'A4B', 'A3B', 'A2B', 'A1B','timestamp','marker','i'])
    test_data=test_df.loc[:,['A1A', 'A2A', 'A3A', 'A4A', 'A4B', 'A3B', 'A2B', 'A1B']].values
    test_data=StandardScaler().fit_transform(test_data)
    print('test_data acqusition complete',"\n")

    pca2=PCA(n_components=2)
    pca2_test_data=pca2.fit_transform(test_data)
    pca2_test_data=pd.DataFrame(data=pca2_test_data,columns=['A','B'])
    pca2_test_data['timestamp']=test_df['timestamp']
    pca2_test_data['marker']=test_df['marker']
    pca2_test_data['i']=test_df['i']
    pca2_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/2C/Test/Bimbola_Test.csv', index=False)
    

    pca3=PCA(n_components=3)
    pca3_test_data=pca3.fit_transform(test_data)
    pca3_test_data=pd.DataFrame(data=pca3_test_data,columns=['A','B','C'])
    pca3_test_data['timestamp']=test_df['timestamp']
    pca3_test_data['marker']=test_df['marker']
    pca3_test_data['i']=test_df['i']
    pca3_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/3C/Test/Bimbola_Test.csv', index=False)

    pca4=PCA(n_components=4)
    pca4_test_data=pca4.fit_transform(test_data)
    pca4_test_data=pd.DataFrame(data=pca4_test_data,columns=['A','B','C','D'])
    pca4_test_data['timestamp']=test_df['timestamp']
    pca4_test_data['marker']=test_df['marker']
    pca4_test_data['i']=test_df['i']
    pca4_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/4C/Test/Bimbola_Test.csv', index=False)

    pca5=PCA(n_components=5)
    pca5_test_data=pca5.fit_transform(test_data)
    pca5_test_data=pd.DataFrame(data=pca5_test_data,columns=['A','B','C','D','E'])
    pca5_test_data['timestamp']=test_df['timestamp']
    pca5_test_data['marker']=test_df['marker']
    pca5_test_data['i']=test_df['i']
    pca5_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/5C/Test/Bimbola_Test.csv', index=False)

    pca6=PCA(n_components=6)
    pca6_test_data=pca6.fit_transform(test_data)
    pca6_test_data=pd.DataFrame(data=pca6_test_data,columns=['A','B','C','D','E','F'])
    pca6_test_data['timestamp']=test_df['timestamp']
    pca6_test_data['marker']=test_df['marker']
    pca6_test_data['i']=test_df['i']
    pca6_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/6C/Test/Bimbola_Test.csv', index=False)

    pca7=PCA(n_components=7)
    pca7_test_data=pca7.fit_transform(test_data)
    pca7_test_data=pd.DataFrame(data=pca7_test_data,columns=['A','B','C','D','E','F','G'])
    pca7_test_data['timestamp']=test_df['timestamp']
    pca7_test_data['marker']=test_df['marker']
    pca7_test_data['i']=test_df['i']
    pca7_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/7C/Test/Bimbola_Test.csv', index=False)
    
    pca8=PCA(n_components=8)
    pca8_test_data=pca8.fit_transform(test_data)
    pca8_test_data=pd.DataFrame(data=pca8_test_data,columns=['A','B','C','D','E','F','G','H'])
    pca8_test_data['timestamp']=test_df['timestamp']
    pca8_test_data['marker']=test_df['marker']
    pca8_test_data['i']=test_df['i']
    pca8_test_data.to_csv(r'C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features/PCA/8C/Test/Bimbola_Test.csv', index=False)

    print("data saving complee ........") 


    
    
if __name__=='__main__':
    main()
