"""
@author: S425510
Cluster MNIST dataset.
"""

import pandas as pd
from sklearn.cluster import KMeans

class Cluster:
    def __init__(self, data):
        self.data = data        
    
    def kmeans(self, n_clusters):       
        kmeans_model = KMeans(n_clusters = n_clusters, random_state=11)
        kmeans_model.fit(self.data) # fit kmeans
        cluster_labels = pd.DataFrame(kmeans_model.labels_)
        cluster_labels.columns = ['clusterNo']
        return pd.concat([self.data, cluster_labels], axis=1) 
        