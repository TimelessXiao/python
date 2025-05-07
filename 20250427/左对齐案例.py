title = "3 abcd"
title1 = "3.1 abcdef"
title2 = "3.2 abcdefg"
title3 = "3.3 abcdefghijk"
title4 = "3.4 abcdaaaa"
number = "7"
number1 = "13"

print(title.ljust(30, "."), number.rjust(3, '.'), sep='')
print(title1.ljust(30, "."), number.rjust(3, '.'), sep='')
print(title2.ljust(30, "."), number.rjust(3, '.'), sep='')
print(title3.ljust(30, "."), number.rjust(3, '.'), sep='')
print(title4.ljust(30, "."), number1.rjust(3, '.'), sep='')
