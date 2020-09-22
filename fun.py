def printNumero(num):
    if num>=0:
        strNum=str(num)
        strAux=""
        for i in range(5):
            for j in strNum:
                if i==0:
                    if j=="1":
                        strAux+="  # "
                    elif j=="4":
                        strAux+="# # "
                    else:
                        strAux+="### "
                elif i==1:
                    if j in "1237":
                        strAux+="  # "
                    elif j in "56":
                        strAux+="#   "
                    elif j in "4890":
                        strAux+="# # "
                elif i==2:
                    if j in "17":
                        strAux+="  # "
                    elif j in "0":
                        strAux+="# # "
                    else:
                        strAux+="### "
                elif i==3:
                    if j in "134579":
                        strAux+="  # "
                    elif j in "2":
                        strAux+="#   "
                    elif j in "068":
                        strAux+="# # "
                elif i==4:
                    if j in "147":
                        strAux+="  # "
                    else:
                        strAux+="### "   
            print(strAux)
            strAux=""


printNumero(int(input("Ingresa el número que deseas mostrar: ")))
