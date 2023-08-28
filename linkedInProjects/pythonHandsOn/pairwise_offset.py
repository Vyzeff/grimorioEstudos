def pairwise_offset(sequence, fillvalue="*", offset=0):
    sequenceCopy = []
    
    for element in sequence:
        sequenceCopy.append(element)
    
    while offset > 0:
        sequence.insert(0, fillvalue)
        sequenceCopy.insert(len(sequenceCopy), fillvalue)
        
        offset -= 1
        
    # print(sequence)
    # print(sequenceCopy)
    
    pairs = []
    for x in zip(sequence, sequenceCopy):
        pairs.append(x)
    
    # print(pairs)
    
    return pairs


if __name__ == "__main__":
    print(pairwise_offset([1,2,3,4,5], "hehehe", 2))