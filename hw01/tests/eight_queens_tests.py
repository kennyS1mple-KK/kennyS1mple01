import sys
import os

# 【关键】把 hw01 目录加入 Python 搜索路径，彻底解决导入问题
current_file = os.path.abspath(__file__)
tests_dir = os.path.dirname(current_file)
hw01_dir = os.path.dirname(tests_dir)
sys.path.insert(0, hw01_dir)

# 导入核心函数
from src.eight_queens import solve_n_queens

def run_tests():
    print("===== 八皇后问题测试开始 =====")
    
    # 测试 4 皇后
    try:
        sol4 = solve_n_queens(4)
        assert len(sol4) == 2, f"4 皇后解法数错误：实际 {len(sol4)}，预期 2"
        print("✅ 4 皇后测试通过：共 2 种解法")
    except AssertionError as e:
        print(f"❌ 4 皇后测试失败：{e}")
    
    # 测试 8 皇后
    try:
        sol8 = solve_n_queens(8)
        assert len(sol8) == 92, f"8 皇后解法数错误：实际 {len(sol8)}，预期 92"
        print("✅ 8 皇后测试通过：共 92 种解法")
    except AssertionError as e:
        print(f"❌ 8 皇后测试失败：{e}")
    
    print("\n===== 测试结束 =====")

if __name__ == "__main__":
    run_tests()