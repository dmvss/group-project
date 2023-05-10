import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def remove_headers(data):
    data = data.drop('Flow ID',axis=1)
    data = data.drop('Src IP',axis=1)
    data = data.drop('Dst IP',axis=1)
    data = data.drop('Timestamp',axis=1)
    data = data.drop('Src Port',axis=1)
    data = data.drop('Dst Port',axis=1)
    data = data.drop('Protocol',axis=1)
    data =  data[data['Flow Duration'] != 0]
    return data
def main():
    keras.backend.clear_session()
    data = pd.read_csv('merged_files2.csv')
    data=remove_headers(data)
    new_data=np.array(data)
    new_data=new_data[:,1:]
    model = Sequential()
    np.random.shuffle(new_data)
    data_points=new_data[0:,0:75]
    labels=new_data[:,75]
    data_points=data_points.reshape((data_points.shape[0], data_points.shape[1], 1))
    model.add(tf.keras.layers.Masking(input_shape=(75, 1)))
    #model.add(tf.keras.layers.LSTM(350,input_shape=(75, 1)))
    model.add(tf.keras.layers.LSTM(350))
    model.add(Dense(units=2, use_bias=True, activation="softmax"))
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(loss='binary_crossentropy', optimizer=opt,metrics=['accuracy'])
    model.summary()
    epochs = 100
    data_points = np.asarray(data_points).astype('float32')
    labels=np.asarray(labels).astype('float32')
    labels = tf.one_hot(labels, depth=2)
    h = model.fit(data_points, labels,verbose=1, epochs=epochs, batch_size=100,validation_split=0.2)
    Loss = h.history['loss']
    Val_Loss = h.history['val_loss']
    plt.plot(Loss)
    plt.plot(Val_Loss)
    plt.show()
    data_test=pd.read_csv('test.csv')
    data_test=remove_headers(data_test)
    data_test = data_test.drop('Label', axis=1)
    ndata_test=np.array(data_test)
    ndata_test=ndata_test[:,1:]
    ndata_test=np.asarray(ndata_test).astype('float32')
    print("test: ",model.predict(ndata_test))
    
if __name__ == '__main__':
    main()
