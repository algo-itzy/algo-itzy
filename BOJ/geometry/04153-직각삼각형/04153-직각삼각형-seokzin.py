while True:
  nums = list(map(int, input().split()))
  
  if sum(nums) == 0:
    break
  
  num_max = max(nums)
  nums.remove(num_max)

  print('right' if nums[0]**2 + nums[1]**2 == num_max**2 else 'wrong')

# 정렬된 리스트란 가정하에 pop()을 썼다 -> 틀림
# sort 한 뒤 pop()을 했다 -> 틀림. 예외가 있는듯
# 결국 첫 방법인 remove로 했다. 심히 맘에 안든다

"""
git commit -m "code: Solve boj 04153 직각삼각형 (seokzin)"
"""