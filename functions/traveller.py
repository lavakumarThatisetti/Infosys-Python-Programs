def traveler():
    traveller_id = 1001
    traveller_name = "jim"
    print(traveller_id,traveller_name,end=",")

def check_baggage(baggage_weight):
    if baggage_weight>=0 and baggage_weight<=40:
        return True;
    else:
        return False;
def check_immigration(expiry_year):
    if(expiry_year>=2001 and expiry_year<=2025):
        return True
    else:
        return False
def check_secuirty(noc_status):
    if(noc_status in {"VALID", "valid"}):
        return True
    else:
        return False
baggage_weight=35
expiry_year=2019
noc_status="VALID"
ck_baggage=check_baggage(baggage_weight)
ck_imm=check_immigration(expiry_year)
ck_sec=check_secuirty(noc_status)
if(ck_baggage==ck_imm==ck_sec):
    traveler();
    print("Allow Traveler to Fly!")
else:
    traveler();
    print("Detain Traveler for Rechekcing")

