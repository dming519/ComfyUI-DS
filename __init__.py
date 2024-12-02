from .ApiPost import ApiPost
from .AddImageToList import AddImageToList
from .SliceImageList import SliceImageList
from .ImageListToImage import ImageListToImage

NODE_CLASS_MAPPINGS = {
    "DS_ApiPost": ApiPost,
    "DS_AddImageToList": AddImageToList,
    "DS_SliceImageList": SliceImageList,
    "DS_ImageListToImage": ImageListToImage,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DS_ApiPost" : "DS🦥POST请求",
    "DS_AddImageToList": "DS🦥AddImageToList",
    "DS_SliceImageList": "DS🦥SliceImageList",
    "DS_ImageListToImage": "DS🦥ImageListToImage",
}
