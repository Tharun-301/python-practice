#1. Normal function (all positional or keyword allowed)
def fun(a, b, c, d):          # a, b, c, d → can be positional or keyword
    print(a, b, c, d)

fun(1, 2, 3, 4)               # Positional call → Valid
fun(a=1, b=2, c=3, d=4)       # Keyword call → Valid

#2. Keyword-only parameters using *
def fun(a, b, *, c, d):
    # a, b → can be positional or keyword
    # c, d → must be keyword-only (because they appear after '*')
    print(a, b, c, d)

fun(1, 2, c=3, d=4)           # Valid → c and d given as keywords
fun(1, b=2, c=3, d=4)        # Valid → b is also  pos or keyword arg, c and d given as keywords

# fun(1, 2, 3, 4)             # ❌ INVALID → c and d cannot be positional

#Keyword-only parameters using * — with default values
def fun(a=10, b=20, *, c=30, d=40):
    # a, b → positional or keyword
    # c, d → keyword-only (appear after '*')
    print(a, b, c, d)

fun()                          # a=10, b=20, c=30, d=40
fun(1, 2, c=3, d=4)            # All correct
fun(a=100, d=400)              # a=100, b=20, c=30, d=400

# fun(1, 2, 3, 4)              # ❌ INVALID → c and d cannot be positional


#3. All keyword-only parameters
def fun(*, a, b, c, d):
    # '*' at the beginning → no positional arguments allowed
    # a, b, c, d → must be keyword-only
    print(a, b, c, d)

fun(a=1, b=2, c=3, d=4)       # Valid → all are keyword arguments 

# fun(1, 2, 3, 4)             # ❌ INVALID → positional arguments not allowed
