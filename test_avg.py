import averagin as average
def test_avg():
    avg=(3+6+9+10+11)/5
    x=[3,6,9,10,11]
    y=average._avg_temp(x)
    assert(y==avg)
def test_max_min():
    x=[3,6,9,10,11]
    y=[max(x),min(x)]
    z=average.calc_min_max_temp(x)
    assert(z==y)
def test_median():
    x=[3,6,9,10,11]
    median =9
    z=average.calculation_median(x)
    assert(median==z) 
