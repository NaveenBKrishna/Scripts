
# coding: utf-8

# In[44]:


import os
import re
import fileinput


# In[45]:


count_line = 0
line_list = []
with open("PGM_new.itp") as topol_file:
    for line in topol_file:
        if line.strip() == '[ atoms ]':  # Or whatever test is needed
            break
    for line in topol_file:  # This keeps reading the file
        if line.strip() == '[ bonds ]':
            break
        count_line += 1    
        line_list.append(line) #line[:-1]
atoms_final_count = line_list[-2].split()[0]


# In[63]:


initial_text_content = ""
topology_file_atoms_content = ""
topology_file_bonds_content = ""
topology_file_pairs_content = ""
topology_file_angles_content = ""
topology_file_dihedrals_content =""
with open("UNL.itp","r+") as itp_file:
    for line2 in itp_file:
        if line2.strip() == '[ atoms ]':
            initial_text_content += line2
            break
        initial_text_content += line2
    for line2 in itp_file:
        if line2.strip() == '[ bonds ]':
            break
        try:
            if(line2.split()[0] != ";"):
                line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                line2 = line2.lstrip()
                initial_text_content += "    "+line2
                topology_file_atoms_content +="    "+line2
            else:
                initial_text_content += line2
                topology_file_atoms_content += line2
        except IndexError:
            pass   
        

#append edited data fo bonds section
with open("UNL.itp","r+") as itp_file:
    for line2 in itp_file:
        if line2.strip() == '[ bonds ]':
            initial_text_content += "\n"+line2
            break
    for line2 in itp_file:
        if line2.strip() == '[ pairs ]':
            break
        try:
            if(line2.split()[0] != ";"):
                #pat = re.compile("^\S(.*\S)?$")
                line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[1]+" ",str(int(line2.split()[1])+int(atoms_final_count)),1)
                line2 = line2.lstrip()
                initial_text_content += "    "+line2
                topology_file_bonds_content += "    "+line2
            else:
                initial_text_content += line2
                topology_file_bonds_content += line2
        except IndexError:
            pass 
        
#append edited data for pairs section
with open("UNL.itp","r+") as itp_file:
    for line2 in itp_file:
        if line2.strip() == '[ pairs ]':
            initial_text_content += "\n"+line2
            break
    for line2 in itp_file:
        if line2.strip() == '[ angles ]':
            break
        try:
            if(line2.split()[0] != ";"):
                #pat = re.compile("^\S(.*\S)?$")
                line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[1]+" ",str(int(line2.split()[1])+int(atoms_final_count)),1)
                line2 = line2.lstrip()
                initial_text_content += "    "+line2
                topology_file_pairs_content += "    "+line2
            else:
                initial_text_content += line2
                topology_file_pairs_content += line2
        except IndexError:
            pass 
        

#append edited data for angles section
with open("UNL.itp","r+") as itp_file:
    for line2 in itp_file:
        if line2.strip() == '[ angles ]':
            initial_text_content += "\n"+line2
            break
    for line2 in itp_file:
        if line2.strip() == '[ dihedrals ]':
            break
        try:
            if(line2.split()[0] != ";"):
                #pat = re.compile("^\S(.*\S)?$")
                line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[1]+" "," "+str(int(line2.split()[1])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[2]+" "," "+str(int(line2.split()[2])+int(atoms_final_count)),1)
                line2 = line2.lstrip()
                initial_text_content += "    "+line2
                topology_file_angles_content+= "    "+line2
            else:
                initial_text_content += line2
                topology_file_angles_content += line2
        except IndexError:
            pass 
        
#apend edited data for dihedrals section
with open("UNL.itp","r+") as itp_file:
    empty_line = "      \n  \r  \t   "
    for line2 in itp_file:
        if line2.strip() == '[ dihedrals ]':
            initial_text_content += "\n"+line2
            break
        
    for line2 in itp_file:
        if line2.strip() == '[ dihedrals2 ]':
            break
        try:
            if(line2.split()[0] != ";"):
                #pat = re.compile("^\S(.*\S)?$")
                line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[1]+" "," "+str(int(line2.split()[1])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[2]+" "," "+str(int(line2.split()[2])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[3]+" "," "+str(int(line2.split()[3])+int(atoms_final_count)),1)
                line2 = line2.lstrip()
                initial_text_content += "    "+line2
                topology_file_dihedrals_content+= "    "+line2
            else:
                initial_text_content += line2
                topology_file_dihedrals_content+=line2
        except IndexError:
            pass 


with open("UNL.itp","r+") as itp_file:
    empty_line = "      \n  \r  \t   "
    for line2 in itp_file:
        if line2.strip() == '[ dihedrals2 ]':
            initial_text_content += "\n"+line2
            break
        
    for line2 in itp_file:
        if line2.isspace():
            break
        try:
            if(line2.split()[0] != ";"):
                #pat = re.compile("^\S(.*\S)?$")
                line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[1]+" "," "+str(int(line2.split()[1])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[2]+" "," "+str(int(line2.split()[2])+int(atoms_final_count)),1)
                line2 = line2.replace(" "+line2.split()[3]+" "," "+str(int(line2.split()[3])+int(atoms_final_count)),1)
                line2 = line2.lstrip()
                initial_text_content += "    "+line2
                topology_file_dihedrals_content+= "    "+line2
            else:
                initial_text_content += line2
                topology_file_dihedrals_content+=line2
        except IndexError:
            pass         

#print initial_text_content

with open("UNL_new.itp","w+") as new_itp_file:
    new_itp_file.write(initial_text_content)

'''
#write respective contents to topology file
topology_content_atoms = ""
topology_content_bonds = ""
topology_content_pairs = ""
topology_content_angles = ""
topology_content_dihedrals = ""
topology_initial_content = ""
with open("topol_Protein_chain_A_back.top","r+") as topology_bak_file:
    for line2 in topology_bak_file:
        if line2.strip() == '[ atoms ]':
            topology_content_atoms += line2
            break
        topology_initial_content+=line2
    for line2 in topology_bak_file:
        if re.search(r"\[(\s\w+\s)\]",line2):
            #topology_bak_file.write("-------bonds--------")
            break
        try:
            if(line2.split()[0] != ";"):
                #line2 = line2.replace(line2.split()[0],str(int(line2.split()[0])+int(atoms_final_count)),1)
                #line2 = line2.lstrip()
                topology_content_atoms += "    "+line2
            else:
                topology_content_atoms += line2
        except IndexError:
            pass 
        
#bonds content        
with open("topol_Protein_chain_A_back.top","r+") as topology_bak_file:
    for line2 in topology_bak_file:
        if line2.strip() == '[ bonds ]':
            topology_content_bonds += line2
            break
        
    for line2 in topology_bak_file:
        if re.search(r"\[(\s\w+\s)\]",line2):
            break
        try:
            if(line2.split()[0] != ";"):
                topology_content_bonds += "    "+line2
            else:
                topology_content_bonds += line2
        except IndexError:
            pass 
    

#pairs content        
with open("topol_Protein_chain_A_back.top","r+") as topology_bak_file:
    for line2 in topology_bak_file:
        if line2.strip() == '[ pairs ]':
            topology_content_pairs += line2
            break
        
    for line2 in topology_bak_file:
        if re.search(r"\[(\s\w+\s)\]",line2):
            break
        try:
            if(line2.split()[0] != ";"):
                topology_content_pairs += "    "+line2
            else:
                topology_content_pairs += line2
        except IndexError:
            pass
        
#angles content        
with open("topol_Protein_chain_A_back.top","r+") as topology_bak_file:
    for line2 in topology_bak_file:
        if line2.strip() == '[ pairs ]':
            topology_content_angles += line2
            break
        
    for line2 in topology_bak_file:
        if re.search(r"\[(\s\w+\s)\]",line2):
            break
        try:
            if(line2.split()[0] != ";"):
                topology_content_angles += "    "+line2
            else:
                topology_content_angles += line2
        except IndexError:
            pass
        
#dihedrals content        
with open("topol_Protein_chain_A_back.top","r+") as topology_bak_file:
    for line2 in topology_bak_file:
        if line2.strip() == '[ dihedrals ]':
            topology_content_dihedrals += line2
            break
        
    for line2 in topology_bak_file:
        if line2.strip() == "\n":
            break
        try:
            if(line2.split()[0] != ";"):
                topology_content_dihedrals += "    "+line2
            else:
                topology_content_dihedrals += line2
        except IndexError:
            pass

print (topology_content_atoms)        
with open("S:/python projects/topol_back_new.top","w+") as new_topology_file:
    new_topology_file.write(topology_initial_content +"\n"+
    topology_content_atoms+topology_file_atoms_content+"\n"+
                            topology_content_bonds+topology_file_bonds_content+"\n"+
                            topology_content_pairs+topology_file_pairs_content+"\n"+
                            topology_content_angles+topology_file_angles_content+"\n"+
                            topology_content_dihedrals+topology_file_dihedrals_content
)

'''
