import json

import requests


class ApiPost:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            # 必填
            "required": {
                "api_url": ("STRING", {"default": "", "multiline": False}),
                "headers": ("STRING", {"default": "", "multiline": True}),
                "body": ("STRING", {"default": "", "multiline": True}),
                "get_response_key": ("STRING", {"default": "", "multiline": False}),
                "seed": ("INT", {
                    "default": 0,
                    "min": -1125899906842624,
                    "max": 1125899906842624
                }),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
                "unique_id": "UNIQUE_ID",
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response_text",)
    FUNCTION = "exec_main"
    CATEGORY = "DS🦥/接口调用"

    def exec_main(self,seed, prompt, extra_pnginfo, unique_id,api_url, headers, body, get_response_key):
        payload = json.loads(body)
        headers = json.loads(headers)
        print(payload)
        response = requests.post(api_url, json=payload, headers=headers, timeout=20)
        if response.status_code == 200:
            answer = response.json()[get_response_key]
            return (answer,)
        else:
            raise Exception("Failed to generate content. Status code: {}".format(response.status_code))
