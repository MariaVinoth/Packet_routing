mask = []
destination = []
next_hop = []
flags = []
interface = []
inp_ip = []
classmask = ['255.255.255.255','255.255.255.0','255.255.0.0','255.0.0.0','0.0.0.0']
global check_ip
check_ip = []
global check_ip2
check_ip2 = ""
global output
output = []
global mask_order
mask_order = []
direct = "-"

#read file with the table
with open("R_input.txt") as f1:
    for line in f1:
        linearray1 = line.split("|")
        mask.append(linearray1[0])
        destination.append(linearray1[1])
        next_hop.append(linearray1[2])
        flags.append(linearray1[3])
        interface.append(linearray1[4])

#read file with the IP
with open("R_input2.txt") as f2:
    for line in f2:
        line = filter(lambda x: not x.isspace(), line)
        inp_ip.append(line)

#define the output
def perform_output(inp_ip2,index):
    if (next_hop[index] == direct):
        output.append("Packet with destination address "+inp_ip2+" is connected directly and will be out on interface " +interface[index] )
    else:
        output.append("Packet with destination address "+inp_ip2+" will be forwarded to "+next_hop[index]+" out on interface " +interface[index] )

#perform and operation on mask and IP and check whether the result has entry in the input table
def perform_and_match(inp_ip1):
    ip_matched = False
    temp_inp_ip = inp_ip1.split(".")
    for mskordr in range(mask_order_len):
        if ip_matched:
            break
        
        temp_mask_split = mask_order[mskordr].split(".")
        first = 0
        for ipmsk in range(len(temp_mask_split)):
            if(temp_mask_split[ipmsk] == "0" or temp_inp_ip[ipmsk] == "0"):
                if (first == 0):
                    check_ip2 = "0"
                    first = 1
                else:
                    check_ip2 = check_ip2 + ".0"
            else:
                if (first == 0):
                    check_ip2 = temp_inp_ip[ipmsk]
                    first = 1
                else:
                    check_ip2 = check_ip2 + "." + temp_inp_ip[ipmsk]
        for destn_match in range(destn_len):
            if (check_ip2 == destination[destn_match]):
                perform_output(inp_ip1,destn_match)
                ip_matched = True
                break
                
#order the mask in highest sequence
def order_mask():
    for i in range(classmask_len):
        for j in range(mask_len):
            if (classmask[i] == mask[j]):
                mask_order.append(mask[j])

    


classmask_len = len(classmask)
mask_len = len(mask)
input_ip_len = len(inp_ip)
order_mask()
mask_order_len = len(mask_order)
destn_len = len(destination)
for x in range(input_ip_len):
    perform_and_match(inp_ip[x])

    
            
#output
op_len = len(output)
op_res = open("Pack_routing_Output.txt","w")
op_res.write("The Output is\n")
op_res.write("\n")
for x in range(op_len):
    op_res.write(output[x])
    op_res.write("\n")



op_res.close()    
        
    



        


        
