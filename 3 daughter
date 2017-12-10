import math

def get_triplets(N):
    triplets = []  # array for saving all possible triplets
    buffer = dict()# dictionary to save sums of arrays in triplets as key and their index as values 
    duplicates = tuple()# tuple of indexes of arrays in triplets with same sum
    for i in range(1, math.ceil(N**(1/3))):
        for j in range(i,math.ceil(math.sqrt(N))+1):
            k = int(N/(i * j))
            if i * j * k == N and j <= k: # to avoid repetition like 334 and 343 
                s = i + j + k 
                triplets.append([i, j, k])
                if s not in buffer:
                    buffer[s] = len(triplets) - 1 # saving the sum in dictionary . in case it is not already there  
                else:
                    duplicates = len(triplets) - 1, buffer[s],  # if sum already exists then saving the duplicate indexes  tuple
    return triplets, duplicates

def get_age_triplet(N):
    t, d = get_triplets(N)
    for i in d:  #for indexes in dupcate tuplle
        if t[i][1] < t[i][2]:#In our case of triplets
			# the first element is always going to be less than or equal to the second element
	return t[i]	# and the second element is always going to be less than or equal to the third element
			# ensuing either two greater elements at position 1 and 2
			# or just one greater element at position 2
            

print(get_age_triplet(36))
