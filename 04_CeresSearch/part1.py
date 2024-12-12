import sys




def possible_word(chars, mask, r, c):
    if( min([m[0]+ r for m in mask]) < 0 or max([m[0]+ r for m in mask]) >= len(chars)  ):
        return "" 
    if( min([m[1]+ c for m in mask]) < 0 or max([m[1]+ c for m in mask]) >= len(chars[r])):
        return "" 
    return "".join([chars[r+m[0]][c+m[1]] for m in mask])
    


def possible_words(chars, masks, r, c):
    return [possible_word(chars, mask, r, c) for mask in masks]




masks = [
    [(0, 0), (0, -1), (0, -2), (0, -3)], 
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (1, -1), (2, -2), (3, -3)],
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
    ]





puzzle = [line.strip() for line in sys.stdin]
candidates = [] 
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        candidates.extend(possible_words(puzzle, masks, i, j))

print(candidates.count("XMAS"))






