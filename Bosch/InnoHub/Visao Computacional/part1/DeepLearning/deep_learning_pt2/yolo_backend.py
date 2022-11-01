import sys
sys.path.append("./keras_yolo2/")
from keras_yolov2.backend import BaseFeatureExtractor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, ReLU


SCALE = 1


class Backend(BaseFeatureExtractor):

    def __init__(self, input_size): 
        model = Sequential() 
     
        model.add(Conv2D(16//SCALE, (3, 3), padding="same",input_shape=input_size)) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2))) 
                 
        model.add(Conv2D(16//SCALE, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(128//SCALE, (3, 3), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(16//SCALE, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(128//SCALE, (3, 3), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2))) 
         
        model.add(Conv2D(32//SCALE, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(256//SCALE, (3, 3), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(32//SCALE, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(256//SCALE, (3, 3), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2))) 
 
        model.add(Conv2D(64//SCALE, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(512//SCALE, (3, 3), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(64//SCALE, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(512//SCALE, (3, 3), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(Conv2D(128, (1, 1), padding="same")) 
        model.add(BatchNormalization()) 
        model.add(ReLU()) 
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2))) 
  
        try: 
            model.load_weights("some_pretrained_weights.h5")
        except: 
            print("using fresh backend model") 
        self.feature_extractor = model  

    @staticmethod
    def normalize(image):
        return image / 255.

