# 開啟檔案
with open('hw2_data.txt', 'r') as file:
    # 初始化計數器和集合
    count = {}
    distinct_set = set()

    # 逐行讀取檔案
    for line in file:
        # 移除換行符號
        char = line.strip()

        # 若是第一次出現的英文字，則將其加入集合
        if char not in distinct_set:
            distinct_set.add(char)

        # 更新計數器
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # 輸出統計結果
    print("總共有", len(distinct_set), "個不重複的英文字")
    for char in count:
        print(char, "出現了", count[char], "次")
