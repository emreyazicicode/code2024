def vergiHesapla( income, type, age, nof ):

	if income > 1000000:
		if type == 'limited':
			if age < 5: 
				return 0.15
			else:
				return 0.20
		elif type == 'holding':
			if nof > 10:
				return 0.08
		

print( vergiHesapla( 100000, 'limited', 5, 0 ) )

