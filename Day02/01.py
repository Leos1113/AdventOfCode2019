inputProgram = [int(x) for x in open("input.txt").readline().split(",")]
inputProgram[1] = 12
inputProgram[2] = 2

computer = {
    "program": inputProgram,
    "pc": 0
}

def intCode(computer):
    opcode = computer["program"][computer["pc"]]
    output = None
    
    if opcode == 99:
        print(computer["program"][0])
        return
    
    ptrInput1 = computer["program"][computer["pc"] + 1]
    
    ptrInput2 = computer["program"][computer["pc"] + 2]
    
    ptrOutput = computer["program"][computer["pc"] + 3]
    
    input1 = computer["program"][ptrInput1]
   
    input2 = computer["program"][ptrInput2]
    
    if opcode == 1:
        output = input1 + input2
    elif opcode == 2:
        output = input1 * input2
    
    computer["program"][ptrOutput] = output
    computer["pc"] += 4
    intCode(computer)


intCode(computer)
