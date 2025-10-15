def minimax(depth, node, is_max, scores, h):
    if depth == h:
        return scores[node]
    if is_max:
        return max(minimax(depth+1, node*2, False, scores, h),
                   minimax(depth+1, node*2+1, False, scores, h))
    else:
        return min(minimax(depth+1, node*2, True, scores, h),
                   minimax(depth+1, node*2+1, True, scores, h))

scores = [3, 5, 2, 9]  # leaf node scores
print("Optimal value:", minimax(0, 0, True, scores, 2))
