from pylsl import StreamInfo,StreamInlet, StreamOutlet, resolve_stream

def main():
    
    #SEARCH FOR EEG STREAM
    print("looking for an EEG stream...")
    streams=resolve_stream('name', 'PCA-testStream')
    eeg_info=streams[0]
    eeg_info=streams[0]
    PCA_inlet=StreamInlet(eeg_info)
    print(eeg_info.name(),eeg_info.type(),"\n")
    i=0
    if i==0:
        print('stream acquired,acqusition ongoing........',"\n")
    while True:
        sample, timestamp=PCA_inlet.pull_sample()
        print([ sample[0], sample[1] ])
        i=i+1


if __name__=='__main__':
    main()
