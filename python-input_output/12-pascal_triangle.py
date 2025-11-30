#!/usr/bin/python3
"""
pascal triade
"""


def pascal_triangle(n):
    """
    function
    """
    if (n <= 0):
        return []

    triangle = [[1]]  # İlk sıra

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # Hər zaman 1 ilə başlayır
        # Ortadakı elementləri hesabla
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Hər zaman 1 ilə bitir
        triangle.append(row)

    return triangle
