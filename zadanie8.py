def liczenie_odpowiedzi():
    licznik_nie = 0 
    
    while True:
        odpowiedz = input("Czy pada? (tak/nie): ").strip().lower()
        
       if odpowiedz == "nie":
           licznik_nie += 1 
       elif odpowiedz == "tak": 
          print(f"Powiedziałeś 'nie' {licznik_nie} razy.")
          break
      else:
         print("Nie rozumiem odpowiedzi, spróbuj ponownie.") 
  
liczenie_odpowiedzi()
