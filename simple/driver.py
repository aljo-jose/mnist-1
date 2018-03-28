"""
@author: S425510
Load MNIST dataset, call cluster and classifer.
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from importlib import reload
from sklearn.linear_model import LogisticRegression
import mnist_cluster
import mnist_classifier

# Load MNIST dataset from sklearn.
def load_mnist_data():
    mnist_dataset = load_digits()
    X = pd.DataFrame(mnist_dataset.data)
    y = mnist_dataset.target
    return X, y

# Reload imported modules so that changes in code files reflects without kernel restart.
def reload_modules():
    reload(mnist_cluster)
    reload(mnist_classifier)        

if __name__ == 'main':
    X, y = load_mnist_data()
    
    # Cluster using kmeans.
    obj_cluster = mnist_cluster.Cluster(data = X)
    X_clustered = obj_cluster.kmeans(n_clusters = len(np.unique(y)))
    
    # Classify non-clustered dataset.
    obj_classifier = mnist_classifier.Classifier(X, y)
    predictions = obj_classifier.classify(LogisticRegression(random_state=11)) # Accuracy: 0.9666
    
    # Classify clustered dataset.
    obj_classifier = mnist_classifier.Classifier(X_clustered, y)
    predictions = obj_classifier.classify(LogisticRegression(random_state=11)) #Accuracy: 0.9694
    print(np.unique(predictions))
    
    # Classify clustered dataset with a multiclass paramater.
    obj_classifier = mnist_classifier.Classifier(X_clustered, y)
    predictions = obj_classifier.classify(LogisticRegression(multi_class='multinomial', solver='newton-cg', random_state=11))
    print(np.unique(predictions)) # Accuracy 0.9722

    
    
    
    
    
    
