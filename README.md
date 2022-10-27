## koRTT
**Round Trip Translation(RTT)** tool for **Korean data** augmentation

**한국어 데이터 증강을 위한 파이썬 라이브러리**입니다.  
Round Trip Translation을 활용하여 **주어진 문장을 유사한 의미의 문장으로 변환**합니다.

### Install 
```
pip install kortt
```

### Usage
사용에 앞서 각 모드별로 **API Key 발급**이 필요합니다.   
(google의 경우 API 키 입력이 필요 없습니다.)   
지원하는 모드는 아래 Surppoted modes를 참고해주세요.  
⚠️  **발급받은 API 키는 공개된 파일에 노출되지 않도록 주의해주세요**

```
from kortt import Generator

generator = Generator(
    mode="papago", client_id="YOURCLIENTID", secret_id="YOURSECRETID"
)

result = generator.generate("나는 오늘 아침에 밥을 맛있게 먹었다.")
print(result)

# "나는 오늘 아침에 맛있는 식사를 했다."
```

### Surppoted modes
|Mode|Link|
|---|---|
|papago|https://developers.naver.com/docs/papago/README.md|
|google|API Key 필요 X|
|microsoft|모드 추가 예정|

### Examples
|Source Senetence|Papago result|Google result|
|---|-------|-------|
|나는 오늘 아침에 밥을 맛있게 먹었다.|나는 오늘 아침에 맛있는 식사를 했다.|나는 오늘 아침에 맛있는 쌀을 먹었다.|
|오랜만에 산책하니까 좋다.|오랜만에 산책하니 좋다.|내가 걷는 지 오래되었습니다.|
|빼앗긴 들에도 봄은 오는가|도둑맞은 땅에도 봄이 오나요?|봄이 도난당한 들판에오고 있습니다|
|하늘을 우러러 한 점 부끄럼이 없기를|하늘을 올려다보는 것에 부끄러움이 없기를 바랍니다.|하늘에 부끄러운 지점이 없기를 바랍니다.|
|가야 할 때가 언제인가를 분명히 알고 가는 이의 뒷모습은 얼마나 아름다운가|언제 가야 할지 뻔히 아는 사람의 뒷모습은 얼마나 아름다운가.|언제 갈지 명확하게 아는 사람의 뒷면이 얼마나 아름답습니까?|
|Pytorch는 딥러닝을 위한 강력한 도구이다|파이토치는 딥러닝을 위한 강력한 도구이다.|Pytorch는 딥 러닝을위한 강력한 도구입니다|
|한국어 자연어 처리 난이도 ㄹㅇ 실화냐 ㅋㅋ|한국어 자연어 처리 난이도는 정말 현실이야 ㅋㅋ|한국 자연 언어 처리 난이도는 실화입니다 haha|
|오늘 미팅은 10시에 시작합니다|오늘 회의는 10시에 시작한다.|오늘의 회의는 10시에 시작됩니다|
## Reference
- https://github.com/ssut/py-googletrans