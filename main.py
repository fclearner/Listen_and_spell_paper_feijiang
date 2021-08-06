from src.data import Data

if __name__ == 'main':
    data_path = ''
    D = Data()
    #1.feature extraction
    D.load_dataset(data_path)
    #2.Listen(pyramid BLSTM:feature extraction & reduce dimension of feature vector)
    #3.Attend and spell(attention mechanism:produce characters probability distribution)
    #4.Decode
