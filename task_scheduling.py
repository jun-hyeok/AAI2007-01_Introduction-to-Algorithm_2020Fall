# 2020-2_(AAI2007-01)Introduction-to-Algorithm 알고리즘개론
# 2018311199 박준혁

# 이진힙 클래스
class BinaryHeap:
    def __init__(self, array=[]):
        self.items = array

    def size(self):
        return len(self.items)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def downheap(self, i):
        while 2 * i + 1 <= self.size() - 1:
            k = 2 * i + 1
            if k < self.size() - 1 and self.items[k] > self.items[k + 1]:
                k += 1
            if self.items[i] < self.items[k]:
                break
            self.swap(i, k)
            i = k

    def heapify(self):  # 시간복잡도: O(N)
        hsize = len(self.items)
        for i in range(hsize // 2 - 1, -1, -1):
            self.downheap(i)

    def extract_earliest(self):  # 시간복잡도: O(logN)
        if self.size() == 0:
            print("Heap is empty.")
            return None
        earliest = self.items[0]
        self.swap(0, -1)
        del self.items[-1]
        self.downheap(0)
        return earliest


def classroom_assign(classes):  # 시간복잡도 : O(NlogN)
    # 처음 선택한 가장 이른 강의를 timetable[0](classroom #1)으로 초기화
    timetable = [[classes.extract_earliest()]]

    # 배정하지 않은 강의가 없을 때까지 실행
    while classes.size() != 0:
        # 배정하지 않은 강의 중 가장 이른 강의 선택
        # 시간복잡도: O(logN) - Sum: logN + log(N-1) + ...
        startTime, endTime = classes.extract_earliest()

        # 배정하지 않은 강의 중 가장 이른 강의시작시간 startTime과
        # 배정된 강의 중 가장 이른 강의종료시간 timetable[0][-1][-1]을 비교
        # 강의 시간이 겹치는 경우
        if startTime < timetable[0][-1][-1]:
            # 강의실 추가 및 배정
            timetable.append([(startTime, endTime)])
        # 그렇지 않은 경우
        else:
            # 동일한 강의실에 배정
            timetable[0].append((startTime, endTime))

        # 강의실마다 마지막 강의의 강의종료시간이 가장 이른 순서로 timetable 정렬
        # 시간복잡도: O(NlogN) - 최악의 경우 모든 강의시간이 겹칠 때
        timetable.sort(key=lambda x: x[-1][-1])
    # 배정 시간표를 반환
    return timetable


if __name__ == "__main__":
    # 7.알고리즘개론.pdf 의 예시
    # 강의시간 초기화
    classes = [
        (900, 1030),
        (900, 1230),
        (900, 1030),
        (1100, 1230),
        (1100, 1400),
        (1300, 1430),
        (1400, 1630),
        (1500, 1630),
        (1500, 1630),
    ]

    # 입력받은 classes list를 BinaryHeap을 이용한 우선 순위 큐를 이용해 강의시작시간(start)을 기준으로 우선순위를 만든다.
    classes = BinaryHeap(classes)
    classes.heapify()  # 시간복잡도: O(N)

    # 강의실에 강의를 배정한다
    timetable = classroom_assign(classes)  # 시간복잡도: O(NlogN)
    classrooms = len(timetable)  # 강의실 수 계산

    # 강의실과 강의시간이 적힌 시간표 정보를 출력한다.
    for i, t in enumerate(timetable):
        print(f"classrooom #{i+1}", t)
    print("강의실 개수:", classrooms)