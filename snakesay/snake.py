SNAKE = r"""  \
   \    __
    \  {oo}    
       (__) \
         λ  \\
            _\\__
           (_____)_
          (________)Ooᵒ
"""

CAT = r"""  \ 
   \
     /\_/\ 
    ( o.o ) 
     > ^ < 
 """

DOG = r"""  \
   \
     /^ ^\ 
    / 0 0 \ 
    V\ Y /V
     / - \ 
     |    \
     || (__V
"""

def bubble(message):
    bubble_length = len(message) + 2
    return f""" 
  {"_" * bubble_length}
 ( {message} )
  {"‾" * bubble_length}"""

def say(message='Hello go to bed'):
    print(bubble(message))  
    print(SNAKE)

def hiss(message="Sleep little cub man"):
    print(bubble(message))  
    print(SNAKE)

def meow(message="Meow, milk please"):
    print(bubble(message))  
    print(CAT)

def bark(message="Hey, trhow the stick"):
    print(bubble(message))  
    print(DOG)
