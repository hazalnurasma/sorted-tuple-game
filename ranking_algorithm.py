import numpy as np

#Notes
#~np.isnan(arr) --> finds non null values in the array

class Water_Sort_Puzzle:
    def __init__(self,pos):
        self.pos = pos

    def __repr__(self):
        rep = str(self.pos)
        return rep
    
    @staticmethod
    def CalculateFullnes(bottles):
        # Initialize an empty list to store ranks
        lenghts = []
        # Iterate over each bottle
        for bottle in bottles:
            # Count non-NaN values in the current bottle
            lenght = np.count_nonzero(~np.isnan(bottle))
            
            # Append the rank to the list
            lenghts.append(lenght)

        # Convert the list of ranks to a NumPy array before returning
        return np.array(lenghts)
    
    @staticmethod
    def CalculateRank(bottles):
        # Use calculate_length_for_bottles as a regular function
        lenghts = Water_Sort_Puzzle.CalculateFullnes(bottles)
     
        ranks = []

        for i in range(12): #range şişe sayısı
            if lenghts[i] == 0:
                rank = 0
                ranks.append(rank)
            elif lenghts[i] == 1:
                rank = 1
                ranks.append(rank) 
            else:
                rank = 1
                for j in range(1,lenghts[i]):
                    if bottles[i,lenghts[i]-1-j] == bottles[i,lenghts[i]-1]:
                        rank = rank + 1
                        print(rank)
                ranks.append(rank)

        return np.array(ranks)
    
   



       
     
        
bottles = np.array([[1,np.nan,np.nan,np.nan],
                [2,1,1,1],
                [2,2,np.nan,np.nan],
                [np.nan,np.nan,np.nan,np.nan],
                [3, 4, 5, 6],
                [np.nan, np.nan, np.nan, np.nan],
                [1, 2, np.nan, np.nan],
                [2, 2, 1, 1],
                [np.nan, np.nan, np.nan, np.nan],
                [1, 1, 1, 1],
                [2, 2, 2, 2],
                [3, 3, 3, 3]])

lengths = Water_Sort_Puzzle.CalculateFullnes(bottles)
ranks = Water_Sort_Puzzle.CalculateRank(bottles)

print(bottles)
print(lengths)
print(ranks)
