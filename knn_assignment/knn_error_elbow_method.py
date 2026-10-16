from sklearn.datasets import load_iris
import pandas as pd
import ml_module as ml

ir = load_iris()
data = pd.DataFrame(data = ir.data , columns = ir.feature_names)
mapper = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# testing 20% of dataset (30 records)
# training 80% of dataset (120 records)
trains = int(len(data)*0.8)
training_data = data.iloc[0:trains]
train_tar = ir.target[0:trains]

tests = len(data) - trains
testing_data = data.iloc[trains:(trains+tests)]
test_tar = ir.target[trains:(trains+tests)]


# print(len(training_data),len(testing_data)) WORKING
wrongs = []

for k in range(1,11,1):
    wrong = 0
    
    for i in range(len(testing_data)):  # Iterate over row indices
        point = list(testing_data.iloc[i])  # Get feature values for row i
        
        df,votes = ml.knn(training_data,point,train_tar,mapper,k)
        
        ans = list(votes)[0]
        
        if(ans != mapper[test_tar[i]]):
            wrong += 1
            
    wrongs.append(wrong)


print(wrongs)

