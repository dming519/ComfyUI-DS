
class SliceImageList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_list": ("IMAGE_LIST",),  # 图片集合输入
                "start_index": ("INT", {        # 起始索引
                    "default": 0,
                    "min": 0,
                    "max": 1000,  # 可根据需求调整最大值
                    "step": 1,
                    "display": "number"
                }),
                "end_index": ("INT", {          # 结束索引
                    "default": -1,              # -1表示截取到列表末尾
                    "min": -1,
                    "max": 1000,                # 可根据需求调整最大值
                    "step": 1,
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "slice_image_list"
    CATEGORY = "DS🦥/图像列表"

    def slice_image_list(self, image_list, start_index, end_index):
        image_list = list(image_list)
        # 使用Python的列表切片功能截取图像列表
        # 如果end_index为-1，则end_index赋值为列表的长度
        if end_index == -1:
            end_index = len(image_list)
        sliced_list = image_list[start_index:end_index]
        print(f"Current image list size: {len(image_list)}")
        return (sliced_list,)

