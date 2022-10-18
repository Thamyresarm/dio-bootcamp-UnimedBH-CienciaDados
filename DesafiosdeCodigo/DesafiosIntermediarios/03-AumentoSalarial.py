salario = float(input()) 

if (salario >= 0 and salario <= 600.00):
  reajuste = salario * 17 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 17 %''')
           
elif (salario > 600.00 and salario <= 900.00):
  reajuste = salario * 13 / 100
  novoSalario = salario + reajuste
    
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 13 %''')

elif (salario > 900.00 and salario <= 1500.00):
  reajuste = salario * 12 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 12 %''')

elif (salario > 1500 and salario <= 2000.00):
  reajuste = salario * 10 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 10 %''' )

else: 
  reajuste = salario * 5 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 5 %''')