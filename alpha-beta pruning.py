def alpha_beta(depth, index, is_max, values, alpha, beta, height):
    # Leaf node
    if depth == height:
        return values[index]

    if is_max:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                index * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )
            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                break   # Beta cut-off

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                index * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )
            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                break   # Alpha cut-off

        return best
import math

values = [2,3,5,9,0,1,7,5]
height = int(math.log2(len(values)))

result = alpha_beta(
    0, 0, True, values,
    float('-inf'), float('inf'), height
)

print("Optimal value:", result)
