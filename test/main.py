
# 방법 1
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname((__file__)))))
# import test_sub.stu1 as stu1

# 방법 2
import sys
sys.path.append('.\.')
from test_sub import stu1


school1 = stu1.Stu_seoul()
print(school1)