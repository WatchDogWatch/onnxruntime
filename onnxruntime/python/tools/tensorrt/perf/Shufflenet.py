import os
import sys
import numpy as np
import onnxruntime
import subprocess
import onnx
from onnx import numpy_helper
from BaseModel import *

class Shufflenet(BaseModel):
    def __init__(self, model_name='Shufflenet-v2', providers=None): 
        BaseModel.__init__(self, model_name, providers)
        self.inputs_ = []
        self.ref_outputs_ = []
        # self.validate_decimal_ = 3 

        if not os.path.exists("model/test_shufflenetv2/model.onnx"):
            subprocess.run("wget https://github.com/onnx/models/raw/master/vision/classification/shufflenet/model/shufflenet-v2-10.tar.gz", shell=True, check=True)
            subprocess.run("tar zxf shufflenet-v2-10.tar.gz", shell=True, check=True)

        self.onnx_zoo_test_data_dir_ = os.path.join(os.getcwd(), "model/test_shufflenetv2") 
        self.create_session("model/test_shufflenetv2/model.onnx")


    def preprocess(self):
        return

    def inference(self, input_list=None):
        session = self.session_
        if input_list:
            outputs = []
            for test_data in input_list:
                img_data = test_data
                output = session.run(None, {
                    session.get_inputs()[0].name: img_data
                })
                outputs.append(output[0])
            self.outputs_ = outputs

    def postprocess(self):
        return
