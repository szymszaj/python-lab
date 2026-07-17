def srednia(liczby):
  if len(liczby) ==0:
    return 0
  return sum(liczby) / len(liczby)   

oceny = [4, 5, 3, 5, 4]
print(f"Srednia ocen: {srednia(oceny)}")