# [동적 객체인지 콘테스트](https://www.onoffmix.com/event/231489) 

## Requirements

Python 3.8 or later with all [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) dependencies installed, including `torch>=1.7`. To install run:
```bash
$ pip install -r requirements.txt
```

## Inference

```bash
python inference.py --weights yolov5x_best.pt --source ../dataset/images/val/ --save-conf --save-txt
```

<!-- <img src="https://user-images.githubusercontent.com/26833433/97107365-685a8d80-16c7-11eb-8c2e-83aac701d8b9.jpeg" width="500">   -->


## Training

### Download weight 
```
./weights/download_weights.sh
```

```bash
$ python train.py --data yolo.yaml --weights yolov5x.pt
```
<!-- <img src="https://user-images.githubusercontent.com/26833433/90222759-949d8800-ddc1-11ea-9fa1-1c97eed2b963.png" width="900"> -->


## Citation

[![DOI](https://zenodo.org/badge/264818686.svg)](https://zenodo.org/badge/latestdoi/264818686)

## Contact

**Issues should be raised directly in the repository.** For business inquiries or professional support requests please visit https://www.ultralytics.com or email Glenn Jocher at glenn.jocher@ultralytics.com. 
