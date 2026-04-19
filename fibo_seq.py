def fibo(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series
# Fonksiyonu çağır ve sonucu yazdır
print(fibo(10))