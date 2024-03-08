def bubble_sort(arr):
    # 获取数组长度
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # 每轮遍历都将最大的元素冒泡到末尾
        for j in range(0, n - i - 1):

            # 如果当前元素比下一个元素大，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr




if __name__ == '__main__':
    a = bubble_sort([3, 1, 2, 4, 5])
    print(a)
