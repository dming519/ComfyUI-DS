import requests
class Dify:

   

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "query": ("STRING", {"default": "one girl", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate_content"


    def generate_content(self, query, user="abc-123",bearer_token="app-TjSUW3IqRus3byugIMEUoBCD"):
        url = "http://172.16.3.188/v1/workflows/run"
        payload = {
            "inputs": {"prompt": query},
            "response_mode": "blocking",
            "user": user
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(bearer_token)
            
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            answer = response.json()["data"]["outputs"]["text"]
            return (answer,)
        else:
            raise Exception("Failed to generate content. Status code: {}".format(response.status_code))



NODE_CLASS_MAPPINGS = {
    "ComfyUIDify": Dify,
    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DifyPromptGen": "ComfyUIDify",
}
