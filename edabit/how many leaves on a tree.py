def how_manny_leaves(tree_type,N):
    
    if tree_type == "big tree":
         return 100*N
    elif tree_type == "medium tree":
        return 50*N
    elif tree_type == "small tree":
        return 25*N
    
print(how_manny_leaves("big tree",3))
            