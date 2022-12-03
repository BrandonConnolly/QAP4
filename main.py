#QAP 4
#Author Brandon Connolly



f = open("OSICDef.dat", "r")
PolNum = int(f.readline())
BasPre = float(f.readline())
AddDis = float(f.readline())
ExtLiab = float(f.readline())
GlaCov = float(f.readline())
LoanCov = float(f.readline())
HSTRate = float(f.readline())
ProFee = float(f.readline())
f.close()

#inputs
while True:
    NewPolicy = input("Would You Like To Enter A New Policy? (END to Quit): ").upper()
    if NewPolicy == "END":
        break
    while True:
        CustFirstName = input("Enter Customer First Name: ").title()
        if CustFirstName == "":
            print("Customer name cannot be blank.")
        else:
         break

    while True:
        CustLastName = input("Enter Customer Last Name: ").title()
        if CustLastName == "":
            print("Customer last name cannot be blank.")
        else:
            break

    Addr = input("Enter Customers Street Address: ")
    City = input("Enter Customers City: ")
    Prov = input("Enter Customers Province: ")


    allowed_num = set("0123456789")
    allowed_let = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while True:
        PosCod = input("Enter Postal Code(X#X#X#): ").upper()
        if len(PosCod) != 6:
            print("Plate number must be 6 digits - Please re-enter.")
        elif not set(PosCod[0:1]).issubset(allowed_let) or not set(PosCod[1:2]).issubset(allowed_num) or not set(PosCod[2:3]).issubset(allowed_let) or not set(PosCod[3:4]).issubset(allowed_num) or not set(PosCod[4:5]).issubset(allowed_let) or not set(PosCod[5:6]).issubset(allowed_num):
            print("Postal Code contains invalid characters.Please re - enter.")
        else:
            break

    allowed_char = set("0123456789")
    while True:
        CustPhone = input("Enter Customer Phone Number(#########): ") #10 digits/must enter
        if len(CustPhone) != 10:
                print("Phone number must be 10 digits - Please re-enter.")
        elif set(CustPhone).issubset(allowed_char) == False:  # elif CCNum.isdigit() == False
                print("Phone number contains invalid characters.Please re - enter.")
        else:
            break

#NumCarIn will have to be - from total number of cars for discount
    NumCarIn = int(input("Enter the number of vehicles being insured: "))

    Extra = input("Would Customer Like Extra Liability? (Y or N): ").upper()
    if Extra == "N":
        ExtLiab = 0

    Glass = input("Would Customer Like Glass Coverage? (Y or N): ").upper()
    if Glass == "N":
        GlaCov = 0
    
    Loaner = input("Would Customer Like A Loaner Car? (Y or N): ").upper()
    if Loaner == "N":
        LoanCov = 0

    MonFul = input("Would Customer Like To Pay In Full Or Monthly Payments? (F or M): ").upper()
    if MonFul == "F":
        ProFee = 0

#Calculations

    ExtraCar = (NumCarIn - 1)
    DisAmo = (ExtraCar * BasPre) * AddDis
    CarCost = (NumCarIn * BasPre) - DisAmo
    ExtraCov = (ProFee + LoanCov + GlaCov + ExtLiab) * NumCarIn
    HST = (ExtraCov + CarCost) * HSTRate
    TotalCost = (ExtraCov + CarCost + HST)
    MonthlyCost = (TotalCost + ProFee) / 8

#Printed Bill

    print("     One Stop Insurance Company ")
    print("      Insurance Policy Receipt")
    print("-"*39)
    print("Client Name and Address: ")
    print(f"{CustFirstName} {CustLastName}")
    print(Addr)
    print(f"{City:<10s}, {Prov:<2s}, {PosCod:<6s}")
    print()
    print("Phone:" f"{CustPhone} ")
    print()
    print("Number of Car Insured:            "f"{NumCarIn:>3d}")
    print("Extra Liability:                   "f"{Extra:>2s}")
    print("Glass Coverage:                   "f"{Glass:>3s}")
    print("Loaner Car Coverage:              "f"{Loaner:>3s}")
    print("                              ----------")

    CarCost = "${:,.2f}".format(CarCost)
    print("Insurance Premium:             "f"{CarCost:>5s}")
    ExtraCov = "${:,.2f}".format(ExtraCov)
    print("Extra Coverages:                 "f"{ExtraCov:>5s}")
    HST = "${:,.2f}".format(HST)
    print("Sales Tax (HST):                 "f"{HST:>5s}")
    TotalCost = "${:,.2f}".format(TotalCost)
    print ("Total Insurance Cost:          "f"{TotalCost:>5s}")
    print("                              ----------")

    if MonFul == "M":
        ProFee = "${:,.2f}".format(ProFee)
        print("Total Processing Fees:            "f"{ProFee:>5s}")
        MonthlyCost = "${:,.2f}".format(MonthlyCost)
        print ("Total Monthly Fee:               "f"{MonthlyCost:>5s}")

    print("-"*40)

    f = open("Policies.dat", "a")

    f.write("{}, ".format(str(PolNum)))
    f.write("{}, ".format(str(CustFirstName)))
    f.write("{}, ".format(str(CustLastName)))
    f.write("{}, ".format(str(Addr)))
    f.write("{}, ".format(str(City)))
    f.write("{}, ".format(str(Prov)))
    f.write("{}, ".format(str(PosCod)))
    f.write("{}, ".format(str(CustPhone)))
    f.write("{}, ".format(int(NumCarIn)))
    f.write("{}, ".format(str(Extra)))
    f.write("{}, ".format(str(Glass)))
    f.write("{}, ".format(str(Loaner)))
    f.write("{}, ".format(str(MonFul)))
    f.write("{}\n".format(str(TotalCost)))
    f.close()
    print()
    print("Customer information successfully saved.")
    PolNum += 1
        
f = open("OSICDef.dat", "w")
f.write("{}\n".format(int(PolNum)))
f.write("{}\n".format(float(BasPre)))
f.write("{}\n".format(float(AddDis)))   
f.write("{}\n".format(float(ExtLiab)))
f.write("{}\n".format(float(GlaCov)))
f.write("{}\n".format(float(LoanCov)))
f.write("{}\n".format(float(HSTRate)))
f.write("{}\n".format(str(ProFee)))
f.close()


