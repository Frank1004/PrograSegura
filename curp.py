import re
import sys

def ValidC(curp):
    valido = curp
    if re.match('^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$',valido):
        print('La Curp es Correcta')
    else:
        print('La Curp no es correcta')



if __name__ == '__main__':
    curp = sys.argv[1]
    
    ValidC(curp)

    


