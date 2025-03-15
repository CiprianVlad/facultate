#%%
matrix = [[3, 4, 70, 4], 
        [8, 8, 1, 8],
        [2, 11, 5, 10]]

def max_2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    poz1_j = 0
    poz2_j = 0
    
    for i in range(n): 
        max2 = 0 
        max1 = 0
        aux = 0 
        for j in range(m): 
            if max1 < matrix[i][j]: 
                max1 = matrix[i][j]
                poz1_j = j
            elif max2 < matrix[i][j]: 
                max2 = matrix[i][j]
                poz2_j = j 
            # Swap(min1, min2)
            if max1 < max2: 
                aux = max1  
                max1 = max2 
                max2 = aux
                
                aux = poz1_j 
                poz2_j = poz1_j
                poz1_j = aux
        

        for j in range(m): 
            if j != poz1_j:
                if j != poz2_j: 
                    print(matrix[i][j], end =' ')
        print()

def max_v2(matrix):
    for row in matrix:
        if len(row) < 2:
            print("Row has fewer than two elements. Skipping...")
            continue

        # Find the two largest elements
        largest_two = sorted(row, reverse=True)[:2]

        # Print all elements except the largest two
        filtered_row = [value for value in row if value not in largest_two or largest_two.remove(value)]
        print(' '.join(filtered_row))
        
max_v2(matrix)

#%%

def frecventa(frec_cuv):
    return frec_cuv[1] 

cuvinte = "Ana are mere si pere dar Ana are mai multe mere decat pere si nu are decat mere rosii"
cuvinte = cuvinte.lower().split()

frec_cuv = []
for cuvant in cuvinte: 
    found = False 
    for i in range(len(frec_cuv)):
        if frec_cuv[i][0] == cuvant:
            frec_cuv[i] = (cuvant, frec_cuv[i][1] + 1)
            found = True 
            break
    if not found: 
        frec_cuv.append((cuvant, 1))
        
frec_cuv = sorted (frec_cuv, key = frecventa, reverse=True) 

frec_curenta = None
    
for cuvant, frec in frec_cuv: 
    if frec != frec_curenta: 
        if frec_curenta is not None: 
            print()
        print(f"Frecventa {frec} :",end=" ")
        frec_curenta = frec 
    print(cuvant, end =", ")
print()

#%% 

fin = open(r'C:\Users\Ciprian\OneDrive - unibuc.ro\Desktop\facultate\Anul I sem I\PA\Exercitii Colocviu\cinema.in.txt', 'r')

lines = fin.readlines()
d = {}

for line in lines:
    line = line.strip()  
    l = line.split(' % ')  
    print(line)
    cinema = l[0]
    film = l[1]
    ore = set(l[2].split())  
    if cinema not in d:
        d[cinema] = {film: ore}
    else:
        d[cinema][film] = ore

#%% 

fin = open(r"C:\Users\Ciprian\OneDrive - unibuc.ro\Desktop\facultate\Anul I sem I\PA\Exercitii Colocviu\angajati.in.txt", 'r')

lines = fin.readlines()
d = {}

for line in lines:
    line = line.strip()  
    l = line.split(' % ')  
    print(line)
    d[l[0]]={ 
        'functie' : l[1],
        'salariu' : l[2],
        'program_de_lucru':l[3:]
        }

def modifica_salariu(database, nume_angajat, nou_salariu):

    if nume_angajat in database:
        # Update the salary
        database[nume_angajat]['salariu'] = nou_salariu
    else:
        print(f"Angajatul {nume_angajat} nu există în baza de date.")
    
    # Return the updated list of employees and their salaries
    return [(name, details['salariu']) for name, details in database.items()]

print(modifica_salariu(d, 'Ionescu Maria', 10000))
#%%
matrix = []  # Initialize an empty matrix
with open(r"C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\facultate\Anul I sem I\PA\Exercitii Colocviu\array.in.txt", 'r') as file:
    for line in file:
        # Split the line into individual elements
        row = [int(element) for element in line.strip().split()]
        
        matrix.append(row)
# Print the matrix to verify the contents
for row in matrix:
    print(row)

