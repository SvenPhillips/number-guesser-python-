correct = "n"
minn = 0
maxn = 20
print("Think of a number between 1 and " + str(maxn) + " and I will try to guess it")
while (correct != "="):
  guess = (minn + maxn)//2
  print("is the number you are thinking of " + str(guess))
  print("type > if i guessed low, < if i guessed high, and = if i guessed correctly");
  correct = input()
  if (correct == ">"):
    minn = guess
  elif (correct == "<"):
    maxn = guess
print("good job")
