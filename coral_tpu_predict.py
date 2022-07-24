import os
import pathlib
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import classify
from PIL import Image

# Specify the TensorFlow model, labels, and image
script_dir = pathlib.Path("./")
model_file = os.path.join(script_dir, 'dermnet_model.tflite')
label_file = os.path.join(script_dir, 'labels.txt')
image_file = os.path.join(script_dir, 'acute-paronychia-7.jpg')

# Initialize the TF interpreter
interpreter = edgetpu.make_interpreter(model_file)
interpreter.allocate_tensors()

# Resize the image
size = common.input_size(interpreter)
image = Image.open(image_file).convert('RGB').resize(size, Image.ANTIALIAS)

# Run an inference
common.set_input(interpreter, image)
interpreter.invoke()
classes = classify.get_classes(interpreter, top_k=1)

# Print the result
labels = dataset.read_label_file(label_file)
for c in classes:
  print('%s: %.5f' % (labels.get(c.id, c.id), c.score))
