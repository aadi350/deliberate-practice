import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go 
import sklearn 
from sklearn.linear_model import LogisticRegression
import imblearn
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from pandas_profiling import ProfileReport

os.chdir('data')
COLS = [
'duration', 
'protocol_type', 
'service', 
'flag', 
'src_bytes', 
'dst_bytes', 
'land', 
'wrong_fragment', 
'urgent', 
'hot', 
'num_failed_logins', 
'logged_in', 
'num_compromised', 
'root_shell', 
'su_attempted', 
'num_root', 
'num_file_creations', 
'num_shells', 
'num_access_files', 
'num_outbound_cmds', 
'is_host_login', 
'is_guest_login', 
'count', 
'srv_count', 
'serror_rate', 
'srv_serror_rate', 
'rerror_rate', 
'srv_rerror_rate', 
'same_srv_rate', 
'diff_srv_rate', 
'srv_diff_host_rate', 
'dst_host_count', 
'dst_host_srv_count', 
'dst_host_same_srv_rate', 
'dst_host_diff_srv_rate', 
'dst_host_same_src_port_rate', 
'dst_host_srv_diff_host_rate', 
'dst_host_serror_rate', 
'dst_host_srv_serror_rate', 
'dst_host_rerror_rate', 
'dst_host_srv_rerror_rate', 
]
df = pd.read_csv('kddcup.data.corrected', sep=',', header=None, names=COLS)

df.loc[:, 'dst_host_srv_rerror_rate'] = df.loc[:, 'dst_host_srv_rerror_rate'].apply(lambda x: x[:-1])

#profile = ProfileReport(df)
#profile.to_file('report.html')