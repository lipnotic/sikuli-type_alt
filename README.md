# sikuli-type_alt


# sikuli-type_alt

This simple sikuli module (python based) was wrote to allow "typing" on Sikuli.
There are some situations we need to type a text eg. (type-and-search fields)
So instead of using type() (which returns a java.lang.IllegalArgumentException ( java.lang.IllegalArgumentException: Key: Not supported character), you shold use type_alt() function.


**USAGE**

1. Place type_alt.sikuli on the same others sikuli´s projects directory.
2. On the top of your sikuli script type:
import type_alt
reload(type_alt)
from type_alt import *
3.YOU ARE DONE!

Now everytime you need to type accented/special characters, you can use type_alt() instead of type()

**EXAMPLE**

    import type_alt
    reload(type_alt)
    from type_alt import *
    
    
    txt="Lúcia, Sônia, João, Patrícia, Fábio and André are names containing accented chars!"
    type_alt(txt)
