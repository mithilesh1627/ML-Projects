import numpy as np
import pickle
import sklearn
loader = pickle.load(open('/PIMA Diabetes/training_model.sav', 'rb'))
input_data = (8,183,64,0,0,23.3,0.672,32)
# converting the the data in numpy array
input_data_np = np.asarray(input_data)
# reshaping the array as we are predicting for one instance
input_data_np_reshape = input_data_np.reshape(1,-1)
predict = loader.predict(input_data_np_reshape)
if (predict[0] == 0):
    print("The person is not diabetic")
else:
    print("The person is diabetic")