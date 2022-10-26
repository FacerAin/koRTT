import urllib.request
import json


class Generator:
    def __init__(self, mode="papago", client_id=None, secret_id=None):
        self.mode = mode
        self.client_id = client_id
        self.secret_id = secret_id

        self.compatible_modes = ["papago"]

        if self.mode not in self.compatible_modes:
            raise Exception("Choose the correct mode (Ex. papago)")

    def generate(self, text):
        if not text:
            raise Exception("You must input in the text")

        if self.mode == "papago":
            tgt_text = self.get_papago_request(text, src="ko", tgt="en")
            generate_text = self.get_papago_request(tgt_text, src="en", tgt="ko")
            return generate_text

    def get_papago_request(self, text, src="ko", tgt="en"):
        url = "https://openapi.naver.com/v1/papago/n2mt"
        prefix = f"source={src}&target={tgt}&text="
        encode_text = urllib.parse.quote(text)
        request = urllib.request.Request(url)
        request.add_header(
            "Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"
        )
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.secret_id)
        data = (prefix + encode_text).encode("utf-8")

        try:
            response = urllib.request.urlopen(request, data)
            if response.getcode() == 200:
                response_body = json.load(response)
                response_text = response_body["message"]["result"]["translatedText"]
                return response_text

        except Exception as e:
            raise (e)
