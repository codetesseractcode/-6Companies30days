class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = []
        node, left, right, cur = preorder[0], None, None, 'L'
        n = len(preorder)
        if n == 1:
            return node == '#'
        elif node == '#':
            return False

        for i in range(1, n):
            if preorder[i] == '#':
                if cur == 'L':
                    cur = 'R'
                    left = '#'
                else:
                    if stack:
                        node = stack.pop()
                        left = "#"
                        cur = 'R'
                    else:
                        return i == n - 1
            else:
                stack.append(node)
                node, left, right = preorder[i], None, None

        return stack == [] and left == '#' and right == '#'