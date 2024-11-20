def sum_odd_numbers(): 
  odd_sum = sum(number for number in range(1, 101) if number % 2 != 0) 
  return odd_sum 
  
print(f"Suma wszystkich nieparzystych liczb od 1 do 100 wynosi: {sum_odd_numbers()}")
