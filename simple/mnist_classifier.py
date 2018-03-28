"""
@author: S425510
Classify MNIST dataset.
"""
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

class Classifier:
    def __init__(self, X, y):
         self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=11)
         
    def classify(self, model):
        model.fit(self.X_train, self.y_train) 
        y_pred = model.predict(self.X_test)        
        print('Accuracy: {}'.format(accuracy_score(self.y_test, y_pred))) 
        return y_pred
        # cross validation, other performance metrics to be added.
   
   
   
        

