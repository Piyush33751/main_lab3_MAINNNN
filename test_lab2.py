import Lab2.excersie2 as temp


    
def test_bubble_sort_ascending():
    print("Running test for median...")
    My_list = [1, 2, 3, 4, 5]
    x = 5
    medi = temp.median_temp(My_list, x)
    assert(medi==3)
