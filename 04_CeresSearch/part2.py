import sys




def possible_word(chars, mask, r, c):
    if( min([m[0]+ r for m in mask]) < 0 or max([m[0]+ r for m in mask]) >= len(chars)  ):
        return "" 
    if( min([m[1]+ c for m in mask]) < 0 or max([m[1]+ c for m in mask]) >= len(chars[r])):
        return "" 
    return "".join([chars[r+m[0]][c+m[1]] for m in mask])
    


# def possible_words(chars, masks, r, c):
#     return [possible_word(chars, mask, r, c) for mask in masks]




# masks = [
#     [(0, 0), (0, -1), (0, -2), (0, -3)], 
#     [(0, 0), (0, 1), (0, 2), (0, 3)],
#     [(0, 0), (1, 0), (2, 0), (3, 0)],
#     [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
#     [(0, 0), (1, 1), (2, 2), (3, 3)],
#     [(0, 0), (1, -1), (2, -2), (3, -3)],
#     [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
#     [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
#     ]

mask = [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
crosses = ["MSAMS", "SSAMM", "MMASS", "SMASM"]
puzzle = [line.strip() for line in sys.stdin]
candidates = [] 


for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        candidates.append(possible_word(puzzle, mask, i, j))


print(sum([candidates.count(cross) for cross in crosses]))





