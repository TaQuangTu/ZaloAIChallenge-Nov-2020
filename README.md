# ZaloAIChallenge-Nov-2020
Traffic light detection contest

### Contest description, data, evaluation and regulations: 
https://challenge.zalo.ai/portal/traffic-sign-detection

### Using model: YOLOv4
https://github.com/AlexeyAB/

#### Using YOLOv4 requires following files (all of those files were uploaded in this repo)
1. `yolov4-custom.cfg` located at `darknet/cfg/` directory
2. `obj.data` and `obj.names` located at `build/darknet/x64/data`
3. `train.txt` and `valid.txt` located at `data`
4. `prepare.py` located at root of your project. Use this file to prepare data for training
5. Follow instructions in `ZaloAiChallenge.ipynb` colab notebook for continue training. This is not a completed instruction but help you cutdown preparing time for training. I recommend reading instructions from official YOLOv4 github and back here to take advantage of above files.

Goodluckkkk!
