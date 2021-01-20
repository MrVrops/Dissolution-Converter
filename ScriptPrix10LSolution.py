def input_float(lib): #Fonction pour forcer l'input d'un float
   while True :
      saisie = input (lib)
      try:
         return (float(saisie))
      except ValueError:
          pass

continuer = True #Variable de reboot de programme

while continuer == True : #Boucle de reboot le programme


	prix = input_float("Prix du bidon de 5 litres de produit en euros:") #Saisie du prix du bidon de 5 litres

	pourcentage = input_float("Pourcentage de produit a diluer dans 100 L d'eau: ") #Saisie du pourcentage


	pec = 500 / pourcentage #Produit en croix

	final = prix / pec # Prix du bidon / Résultat du produit en croix = Prix au litre

	final2 = final *10 # Multiplier par 10 pour avoir 10 litres

	print("Le prix pour 10 litres de la solution finale est de", final2 ,"euros.") #Afficher le prix pour 10 litres de solution finale



	continuer = input("Voulez vous recommencer? (o/n) ") in ("o", "O") #Demander si on veut recommencer
