class ImageListToImage:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_list": ("IMAGE_LIST",),  # 单张图片
            },
        }

    RETURN_TYPES = ("IMAGE",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "image_list_to_image"
    CATEGORY = "DS🦥/图像列表"

    def image_list_to_image(self, image_list):
        image_list = list(image_list)
        print("image_list_size:", len(image_list))
        return (image_list,)

