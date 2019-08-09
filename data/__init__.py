# from .voc import VOCDetection, AnnotationTransform, detection_collate, VOC_CLASSES
from .voc0712 import VOCDetection, AnnotationTransform, detection_collate, VOC_CLASSES
from .data_augment import *
from .config import *
from .cvwc import CVWCDetection, CVWCAnnotationTransform, CVWC_CLASSES
from .coco import COCODetection