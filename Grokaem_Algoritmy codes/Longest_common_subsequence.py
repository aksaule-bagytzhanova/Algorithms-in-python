#pseudocode

if word_a[i] == word_b[j]:
    cell[i][j] = cell[i-1][j-1]+1
else:
    cell[i][j] = m a x(cell[i-1][j], cell[i][j-1])
    