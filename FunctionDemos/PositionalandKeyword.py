def fun(a, b, /, c, d, *, e, f):
    # a, b → positional-only (cannot use keyword)
    # c, d → positional or keyword
    # e, f → keyword-only (must use keywords)
    print(a, b, c, d, e, f)


fun(15, 20, 30, 40, e=2, f=3)
fun(15, 20, 30, d=40, e=2, f=3) 
fun(15, 20, c=30, d=40, e=2, f=3) # c and d passed as keyword → allowed
# fun(a=15, b=20, c=30, d=40, e=2, f=3) # TypeError:  a and b are positional-only → cannot use keyword
# fun(15, 20, 30, 40, 2, 3) # TypeError: e and f are keyword-only → cannot pass positionally

# fun(15, b=20, c=30, d=40, e=2, f=3) # TypeError: b is positional-only → cannot be keyword

def fun(a, b, /, *, c, d, e, f):
    # a, b → positional-only
    # c, d, e, f → keyword-only
    print(a, b, c, d, e, f)

fun(10, 20, c=3, d=4, e=5, f=6)# a=10, b=20 (positional-only)--- # c,d,e,f must be keyword-only

fun(1, 2, c=30, d=40, e=50, f=60)# All keyword-only parameters correctly used

# fun(a=10, b=20, c=3, d=4, e=5, f=6)# ❌ ERROR: a and b are positional-only, cannot be keyword

# fun(10, 20, 3, 4, 5, 6)# ❌ ERROR: c, d, e, f are keyword-only

# fun(10, b=20, c=3, d=4, e=5, f=6)# ❌ ERROR: b is positional-only, cannot be keyword


def fun2(a, /, b, *, c):
    # a → positional-only
    # b → positional OR keyword
    # c → keyword-only
    print(a, b, c)

fun2(5, b=10, c=15)
# a = 5 (positional-only)
# b = 10 (keyword allowed)
# c = 15 (keyword-only)

# fun2(a=5, b=10, c=15)# ERROR: a is positional-only → cannot use keyword

# fun2(5, 10, 15)# ERROR: c is keyword-only → cannot pass positionally