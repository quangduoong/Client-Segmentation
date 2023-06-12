import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, normalize, OrdinalEncoder
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
np.random.seed(42)

# Read dataset
class GMM_model:
    __model = None
    __encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    __scaler = StandardScaler() 
    __pca =  PCA(2) 
    
    def __init__(self):
        df = pd.read_csv("../Data/bank.csv")
        df = df.drop('contact', axis=1)
        df = df.dropna()

        X_principal = self.__init_preprocessing(df)
        
        # Fitting model 
        self.__model = GaussianMixture(n_components=4).fit(X_principal)
        
    def predict(self, df):
        # Encoding df
        encoded_df = self.__encoder.transform(df)
        encoded_df = pd.DataFrame(encoded_df)
        encoded_df.columns = df.columns.tolist()      
        
        print("Encoded df: ", encoded_df)
        # Scaling
        scaled_df = self.__scaler.transform(encoded_df) 
        
        # Normalizing 
        normalized_df = normalize(scaled_df) 
        normalized_df = pd.DataFrame(normalized_df) 
        
        # Reducing the dimensions of the data 
        X_principal = self.__pca.transform(normalized_df) 
        X_principal = pd.DataFrame(X_principal) 
        
        return self.__model.predict(X_principal) 
    
    def __init_preprocessing(self, df):
        # Encoding df
        self.__encoder.fit(df)
        encoded_df = self.__encoder.transform(df)
        encoded_df = pd.DataFrame(encoded_df)
        encoded_df.columns = df.columns.tolist()

        # Scaling
        self.__scaler.fit(encoded_df)
        scaled_df = self.__scaler.transform(encoded_df) 
        
        # Normalizing 
        normalized_df = normalize(scaled_df) 
        normalized_df = pd.DataFrame(normalized_df) 
        
        # Reducing the dimensions of the data 
        self.__pca.fit(normalized_df)
        X_principal = self.__pca.transform(normalized_df) 
        X_principal = pd.DataFrame(X_principal) 
        
        return X_principal
