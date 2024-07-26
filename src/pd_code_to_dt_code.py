# 假设给出的 pd_code 是合法的
# 试图计算与之对应同一个扭结的 dt_code

from in_out_code import in_out_code

def pd_code_to_dt_code(pd_code: list) -> tuple:
    io_code = in_out_code(pd_code)
    dic    = {}
    for i in range(len(pd_code)): # 考虑每个交叉点的编号处，谁在下方谁在上方
        down_node = pd_code[i][0]
        up_node   = pd_code[i][1] if io_code[i][1] == "IN" else pd_code[i][3]
        print(down_node, up_node)
        assert ((down_node - up_node)%2) != 0 # 保证奇偶性不同
        if down_node % 2== 0:
            dic[up_node]   = +down_node # 偶数从下面穿过，标记为正
        else:
            dic[down_node] = -up_node   # 偶数从上面跨过，标记为负
    dt_code = []
    for i in range(len(pd_code)):
        val = i * 2 + 1
        dt_code.append(dic[val])
    return tuple(dt_code)

if __name__ == "__main__":
    print(pd_code_to_dt_code([[4,1,5,2],[15,1,16,22],[10,4,11,3],[2,12,3,11],[9,16,10,17],[7,18,8,19],[17,8,18,9],[19,12,20,13],[5,15,6,14],[13,20,14,21],[21,6,22,7]]))