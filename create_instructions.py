
f = open("alu_list.txt","r")
i_list = f.readlines()

d = {i_list[i].split()[0].lower() : i for i in range(len(i_list))}
print(d)

inp = "nop"
output_file = open("program1.txt","w")
while(1):
    inp = input("Enter instruction: ")
    instruction = ""
    try : index = d[inp]
    except : print("Exiting program");break
    options = i_list[index].split()[1:]
    for i in options:
        value = ""
        if(i[0].isalpha()):
            value = input("Enter value for "+i+":")
            if(i == "shamt" or i[0] == "r"):
                value = format(int(value), "05b")
            elif(i == "imm"):
                value = format(int(value), "012b")
        else:
            value = i
        instruction = instruction + value
    instruction = hex(int(instruction,2))
    output_file.write(instruction)
    output_file.write("\n")
    print("Instruction = ",instruction)
output_file.close()
            