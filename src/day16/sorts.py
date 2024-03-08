def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        # 数组中第一个下标
        min_index = i
        for j in range(i + 1, len(items)):
            # 数组中第二个下标，下面满足依次递增，满足comp含义，j就置换为min_index+1
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    print(select_sort([3, 41, 12, 4, 20]))
