# dermnet_Tf_lite_micro

## Dataset

The original [Dermnet](https://www.kaggle.com/datasets/shubhamgoel27/dermnet) dataset consists of 23 classes. Since we work with microprocessors that have hardware constraints, we had to reduce the number of classes to 4. The new dataset contains the following classes:

1- Acne and Rosacea Photos

2- Eczema Photos

3- Nail Fungus and other Nail Disease

4- Tinea Ringworm Candidiasis and other Fungal Infections


Also, the original dataset is imbalanced. So, we applied [data augmentation](https://github.com/ayyucedemirbas/vegetables_detection/blob/main/image_data_augmentation.py) techniques manually. We do not prefer to use a Keras layer to do that. Due to it's not a [supported layer](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/all_ops_resolver.cc) for TensorFlow Lite Micro, we were going to have to build it as a [custom layer](https://www.tensorflow.org/lite/guide/ops_custom). 
