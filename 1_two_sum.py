# # Two Sum

# ## 📌 Description

# Two Sum is a Python program that finds two numbers in a given list whose sum equals a specified target value.

# The program returns the indices of the two numbers that add up to the target.

# ## 🚀 Features

# * Finds two numbers that add up to a target.
# * Returns the indices of the matching elements.
# * Uses Python for a simple and efficient implementation.
# * Demonstrates basic problem-solving and array manipulation.

# ## 🛠️ Technologies Used

# * Python 3

# ## 📂 Project Structure

# ```text
# Two-Sum/
# │
# ├── twosum.py
# └── README.md
# ```

# ## ▶️ How to Run

# 1. Clone the repository:

#    ```bash
#    git clone <your-repository-url>
#    ```

# 2. Navigate to the project directory:

#    ```bash
#    cd Two-Sum
#    ```

# 3. Run the Python file:

#    ```bash
#    python twosum.py
#    ```

# ## 💡 Example

# **Input:**

# ```python
# nums = [2, 7, 11, 15]
# target = 9
# ```

# **Output:**

# ```python
# [0, 1]
# ```

# **Explanation:**

# The numbers at indices `0` and `1` are `2` and `7`.

# Their sum is:

# ```text
# 2 + 7 = 9
# ```

# Therefore, the output is `[0, 1]`.

# ## ⏱️ Complexity Analysis

# For the optimized Hash Map approach:

# * **Time Complexity:** O(n)
# * **Space Complexity:** O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
