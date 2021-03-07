# 2020-2_(AAI2007-01)Introduction-to-Algorithm 알고리즘개론
# 2018311199 박준혁

## weighted_scheduling : 작업리스트(j)과 작업 당 이익리스트(p)를 입력 받아 작업스케쥴링하여 최대 이익(max)을 반환하는 함수
# j : 시작시간과 종료시간을 담은 각 작업 (star_time, end_time) 튜플을 담은 리스트
# p : j에 대응되는 각 이익을 담은 리스트
# cache : 현재 작업까지의 작업 스케쥴링 중 최대 이익을 담은 리스트


def weighted_scheduling(j, p):
    # 1 # j와 p를 zip으로 짝지어 j의 end_time을 기준으로 함께 정렬하여 튜플로 반환한다.
    # pair는 zip(j, p)의 element이므로 sorted 함수의 key 값 pair[0][1]는 j(=pair[0])의 end_time을 뜻 한다.
    j, p = zip(*sorted(zip(j, p), key=lambda pair: pair[0][1]))

    # p를 list로 변환하여 cache를 초기화 한다.
    cache = list(p)

    # 2 # i=1인 작업부터 차례대로 max(cache[i], cache[k]+p[i])를 계산하여 cache를 업데이트 한다.
    for i in range(1, len(j)):

        # k는 i보다 작은 수에서 작업이 겹치지 않아야 한다.
        # 즉, k번째 작업 j[k]의 end_time(=j[k][1])이 i번째 작업 j[i]의 start_time(=j[i][0])보다 작거나 같아야 한다.
        for k in range(i):
            if j[k][1] <= j[i][0]:

                # 현재 i번째의 최대 이익이, 겹치지 않는 이전 작업과 현재 작업의 합보다 크다면
                # 그 합을 현재 i번째의 최대 이익으로 업데이트 한다.
                if cache[i] < cache[k] + p[i]:
                    cache[i] = cache[k] + p[i]

        # 작업 스케쥴링으로 업데이트된 cache를 보여준다.
        print(cache)

    # 3 # 전체 작업 스케쥴링 중 최대이익 max를 찾아 반환한다.
    # 처음 max는 0으로 초기화 한다.
    max = 0

    # cache를 돌면서 현재 max보다 큰 값을 max로 업데이트 한다.
    for i in range(len(cache)):
        if max < cache[i]:
            max = cache[i]
    # max를 반환한다.
    return max


if __name__ == "__main__":
    # 10.알고리즘개론.pdf 의 예시
    # 작업과 이익 초기화
    jobs = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
    profits = [5, 6, 5, 4, 11, 2]
    # 최대이익 출력
    print(weighted_scheduling(jobs, profits))