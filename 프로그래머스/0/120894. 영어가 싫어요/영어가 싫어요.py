def solution(numbers):
    # 해시값에 영어: 숫자 이렇게 들어가 있어야함
    hash_numbers = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
   
    for hu in hash_numbers:
        if numbers.find(hu) > -1:
            numbers = numbers.replace(hu, hash_numbers[hu])
    
    answer = int(numbers)
    
    return answer