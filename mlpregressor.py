import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,normalize

class MlpRegressor():

    def __init__(self):

        self.data = 0
        self.inp = 0                                     #inputs are 0
        self.target = 0

    def dataOku(self, dosya):

        self.data = pd.read_csv(dosya)                 #get file

        return self.data
    def inpTar(self,inp1,inp2,tar1,tar2):

        buffer = [0 for i in range(2)]
        self.input = self.data.iloc[:,inp1-1:inp2]

        if  tar2==0:
            self.target = self.data.iloc[:,-1:]

        else:

            self.target = self.data.iloc[:,tar1-1:tar2]

        buffer[0] = self.input
        buffer[1] = self.target
        return buffer


    def columns(self):
        summ = 0
        for i in self.data.columns:
            summ += 1                                      #columns number

        return summ

    def encoder(self,inp,tar):
        self.le = LabelEncoder()
        arr = [0 for i in range(2)]
        for i in inp.columns:
            if inp[i].dtype == object:                              #typecast string to numerical
                inp[i] = self.le.fit_transform(inp[i])
        for i in tar.columns:
            if tar[i].dtype == object:
                tar[i] = self.le.fit_transform(tar[i])

        arr[0] = inp
        arr[1] = tar

        return arr

    def egitim(self,data,target,iterasyon,testsize,randomstate,hidden_layer,activationf):

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(data, target,
                                                                              test_size=testsize, random_state=randomstate)             #training

        arr  =  [0 for i in range(2)]
        if hidden_layer == 0:                                                                       #if hidden layer is NULL default
            nn = MLPRegressor(max_iter=iterasyon,activation = activationf)

        else:

            nn = MLPRegressor(max_iter=iterasyon,hidden_layer_sizes=hidden_layer,activation = activationf)                      #hidden layer is not NULL

        #print(nn)

        nn.fit(self.x_train, self.y_train)

        self.predictions_test = nn.predict(self.x_test)
        self.predictions_train = nn.predict(self.x_train)

        self.score_test = nn.score(self.x_test, self.y_test)                                           #scorer
        self.score_train = nn.score(self.x_train, self.y_train)


        arr[0] = self.score_train
        arr[1] = self.score_test

        return arr

    def mae(self):

        arr = [0 for i in range(2)]
        self.mae_test = mean_absolute_error(self.y_test, self.predictions_test)

        self.mae_train = mean_absolute_error(self.y_train, self.predictions_train)                        #testing

        arr[0] = self.mae_train
        arr[1] = self.mae_test

        return arr