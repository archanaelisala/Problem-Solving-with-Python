def Compound_Interest(p,r,t): 
  
    # Calculates compound interest  
    CompoundInterest = p*(pow((1 + r / 100), t)) 
    print("Compound interest is",CompoundInterest) 
  
  
Compound_Interest(2000, 10.25, 5) 
