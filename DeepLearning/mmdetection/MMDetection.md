Pytorch 기반의 주요 object detection/segmentation 패키지

- torchvision
  - code 기반
  - 지원 알고리즘이 많지 않음
- detectron2
  - config 기반
  - Facebook Research에서 주도
- MMdetection
  - config 기반
  - 중국 칭화 대학 중심의 OpenMMLab 주도



## MMDetection

- 칭화 대학의 주도로 만들어진 Computer Vision Open Source Project인 OpenMMLab에서 출발
- 2018년 MS-COCO Challenge에서 우승 후 모듈을 확장하여 다수의 알고리즘 수용
- 최신의 다양한 Object Detection, Segmentation 알고리즘을 Package로 구현 제공
- 뛰어난 구현 성능, 효율적인 모듈 설계, Config 기반으로 데이터부터 모델 학습/ 평가 까지 이어지는 간편한 파이프라인 적용
- Pytorch 기반으로 구현



## MMDetection 모델 아키텍처

- Backbone
  - Feature Extractor (이미지 -> Feature Map)
- Neck
  - Backbone과 Heads를 연결하면서 heads가 feature map의 특성을 보다 잘 해석하고 처리할 수 있도록 정제 작업
- DeseHead (AnchorHead/AnchorFreeHead)
  - Feature Map에서 Object의 위치와 Classification을 처리하는 부분
- RoIExtractor
  - Feature Map에서 ROI 정보를 뽑아내는 부분
- RoIHead (BBoxHead/MaskHead)
  - ROI정보를 기반으로 Object 위치와 Classification을 수행하는 부분



## Config

config가 거대하다.

- Dataset Config
- Data Pipeline Config
- Model Config (FRCNN, SSD, YOLO, RetinaNet.... etc)
- Data Pipeline Config (optimizer, epochs... etc)
- Train/Valid/Test Config



## Training Pipeline (Hook - Callback)

- Hook(Calllback)을 통해 학습에 필요한 여러 설정들을 Customization 가능
- 대부분 Configuration에서 이를 설정함





## install

```
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html
```













