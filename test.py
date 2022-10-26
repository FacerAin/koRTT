from kortt import Generator


generator = Generator(
    mode="papago", client_id="YOURCLIENTID", secret_id="YOURSECERETID"
)

examples = [
    "나는 오늘 아침에 밥을 맛있게 먹었다.",
    "오랜만에 산책하니까 좋다.",
    "빼앗긴 들에도 봄은 오는가",
    "하늘을 우러러 한 점 부끄럼이 없기를",
    "가야 할 때가 언제인가를 분명히 알고 가는 이의 뒷모습은 얼마나 아름다운가",
]

for example in examples:
    text = generator.generate(example)
    print(text)
