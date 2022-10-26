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
지원하는 모드는 아래 Surppoted modes를 참고해주세요.

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
|google|모드 추가 예정|
|microsoft|모드 추가 예정|

### Examples
|Source Senetence|Papago result|
|---|-------|
|나는 오늘 아침에 밥을 맛있게 먹었다.|나는 오늘 아침에 맛있는 식사를 했다.|
|오랜만에 산책하니까 좋다.|오랜만에 산책하니 좋다.|
|빼앗긴 들에도 봄은 오는가|도둑맞은 땅에도 봄이 오나요?|
|하늘을 우러러 한 점 부끄럼이 없기를|하늘을 올려다보는 것에 부끄러움이 없기를 바랍니다.|
|가야 할 때가 언제인가를 분명히 알고 가는 이의 뒷모습은 얼마나 아름다운가|언제 가야 할지 뻔히 아는 사람의 뒷모습은 얼마나 아름다운가.|

