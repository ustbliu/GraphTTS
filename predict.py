# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:42:36 2019

@author: SY
"""
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from graphtts.parsing import parse_train_args, modify_train_args
from graphtts.train import make_predictions
from graphtts.data import StandardScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,accuracy_score
import os
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math



if __name__ == '__main__':
    args = parse_train_args()
    df = pd.read_csv(args.data_path, index_col=0)
    pred, smiles = make_predictions(args, df.index.tolist())
    hard_preds = [1 if p[0] > 0.5 else 0 for p in pred]
    df_pred_l = pd.DataFrame()
    pred1 = []
    for i in range(len(pred)):
        pred1.append(pred[i][0])
    y_pred = np.argmax(pred,axis=1)
    true1 = []
    df = pd.DataFrame()
    for i in range(len(smiles)):
            df.loc[smiles[i],'pred'] = pred1[i]
