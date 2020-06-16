"""
1516. Xor Sum
https://www.lintcode.com/problem/xor-sum/description
TLE
"""
from collections import deque
class Solution:
    """
    @param arr: the arr
    @param target: the target
    @return: the sum of paths
    """
    def xorSum(self, arr, target):
        # Write your code here.
        if not arr or not arr[0]:
            return 0
        n = len(arr)
        m = len(arr[0])
        hit_to_x_y_with_now_sum = {} #(x, y) : sum
        queue1 = deque([(0, 0, arr[0][0])])
        queue2 = deque([(n - 1, m - 1, arr[n - 1][m - 1])])
        # hit_to_x_y_with_now_sum[(0, 0, arr[0][0])] = 1
        # hit_to_x_y_with_now_sum[(n - 1, m - 1, arr[n - 1][m - 1])] = 1
        QUEUE1_DIRECTION = [(0, 1), (1, 0)]
        QUEUE2_DIRECTION = [(0, -1), (-1, 0)]
        visited = [[None] * m for _ in range(n)]
        visited[0][0] = 0
        visited[n - 1][m - 1] = 1

        hit = 0
        # while queue1 or queue2:
        #     if queue1:
        #         hit += self.process_queue(queue1, arr, QUEUE1_DIRECTION, hit_to_x_y_with_now_sum, target, 1, visited)
        #     if queue2:
        #         hit += self.process_queue(queue2, arr, QUEUE2_DIRECTION, hit_to_x_y_with_now_sum, target, 2, visited)
        while queue1 or queue2:
            if queue1:
                hit += self.process_queue(queue1, arr, QUEUE1_DIRECTION, hit_to_x_y_with_now_sum, target, 0, visited)
            if queue2:
                hit += self.process_queue(queue2, arr, QUEUE2_DIRECTION, hit_to_x_y_with_now_sum, target, 1, visited)

        # print (hit)
        return hit

    def process_queue(self, queue, arr, queue_direction, hit_to_x_y_with_now_sum, target, flag, visited):
        hit = 0
        n = len(arr)
        m = len(arr[0])

        x, y, now_sum = queue.popleft()

        # if visited[x][y] != flag:
        #     # met
        #     continue
        if x + y == (n + m) // 2:
            hit += hit_to_x_y_with_now_sum.get((x, y, target ^ now_sum ^ arr[x][y], not flag), 0)
            hit_to_x_y_with_now_sum[(x, y, now_sum, flag)] = hit_to_x_y_with_now_sum.get((x, y, now_sum, flag), 0) + 1
            return hit

        for delta in queue_direction:
            nx = x + delta[0]
            ny = y + delta[1]
            if not self.is_valid(arr, nx, ny):
                continue
            next_now_sum = now_sum ^ arr[nx][ny]

            queue.append((nx, ny, next_now_sum))
            visited[nx][ny] = flag

        return hit

    def is_valid(self, arr, x, y):
        n = len(arr)
        m = len(arr[0])
        return 0 <= x < n and 0 <= y < m


s = Solution()
arr = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
target = 0
# arr = [[2,1,5],[7,10,0],[12,6,4]]
# target = 11
print(s.xorSum(arr, target))
