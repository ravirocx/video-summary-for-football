from model_architecture import Model
from load_images import load
import random
import numpy as np
from model_architecture import Model
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
epochs=25
learning_rate=0.001
bs=32
data=[]
labels=[]
architecture=Model(224,224,3,2)
model=architecture.model4()
model.summary()
ld=load(224,224,3,[['subs'],['socbo']])

data,labels=ld.imgload()
print(data)
c=list(zip(data,labels))
random.shuffle(c)
data[:],labels[:]=zip(*c)
data=np.array(data,dtype="float")/255.0
labels=np.array(labels)
trainX,testX,trainY,testY=train_test_split(data,labels,test_size=0.1,random_state=42)
trainY=to_categorical(trainY,num_classes=2)
testY=to_categorical(testY,num_classes=2)
aug=ImageDataGenerator(width_shift_range=0.1,height_shift_range=0.1,shear_range=0.2,zoom_range=0.2,fill_mode="nearest")
opt=Adam(lr=learning_rate,decay=learning_rate/epochs)
model.compile(loss="binary_crossentropy",optimizer=opt,metrics=["accuracy"])
h=model.fit_generator(aug.flow(trainX,trainY,batch_size=bs),validation_data=(testX,testY),steps_per_epoch=len(trainX)//bs,epochs=epochs,verbose=1)
model.save("soccer.model")
