import random 
def zgadywanka():
  pada = random.choice([True, False]) # Losuje, czy pada 
  zgaduj = input("Czy pada? (t/n): ").strip().lower() 
  if (zgaduj == "t" and pada) or (zgaduj == "n" and not pada): print("Brawo, zgadłeś!")
  else: print("Niestety, nie zgadłeś.") 
      
  zgadywanka()
