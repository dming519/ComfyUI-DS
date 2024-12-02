class AddImageToList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),  # 单张图片
            },
            "optional": {
                "image_list": ("IMAGE_LIST", {  # 可选参数
                    "default": [],  # 如果未传入，则默认为空集合
                }),
            },
        }

    RETURN_TYPES = ("IMAGE_LIST",)
    FUNCTION = "add_image_to_list"
    CATEGORY = "DS🦥/图像列表"

    def add_image_to_list(self, image, image_list=None):
        # 确保 image_list 是一个列表
        if image_list is None or not isinstance(image_list, list):
            image_list = list(image_list) if image_list else []
        # 将单张图片添加到集合中
        image_list.append(image)
        print("image_list_size:", len(image_list))
        return (image_list,)
