def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """

    def maxnum(pyramid):

    return type(pyramid)

if __name__ == '__main__':
    print count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    ))
    # assert count_gold((
    #     (1,),
    #     (2, 3),
    #     (3, 3, 1),
    #     (3, 1, 5, 4),
    #     (3, 1, 3, 1, 3),
    #     (2, 2, 2, 2, 2, 2),
    #     (5, 6, 4, 5, 6, 4, 3)
    # )) == 23, "First example"
    # assert count_gold((
    #     (1,),
    #     (2, 1),
    #     (1, 2, 1),
    #     (1, 2, 1, 1),
    #     (1, 2, 1, 1, 1),
    #     (1, 2, 1, 1, 1, 1),
    #     (1, 2, 1, 1, 1, 1, 9)
    # )) == 15, "Second example"
    # assert count_gold((
    #     (9,),
    #     (2, 2),
    #     (3, 3, 3),
    #     (4, 4, 4, 4)
    # )) == 18, "Third example"
