class Car:
    def __init__(self,year,make,model,num_doors,roof):
        self.year=year
        self.make=make
        self.model=model
        self.num_doors= num_doors
        self.roof=roof

    def give_intel(self):
        print(f" Your car's \nyear:{self.year}\n")
        print(f" Your car's \nmake:{self.make}\n")
        print(f" Your car's \nmodel:{self.model}\n")
        print(f"Your car's \nnum_doors:{self.num_doors}\n")
        print(f"Your car's \nroof:{self.roof}\n")
        
        
while True:
    try:
        yr=int(input("year of your car-->"))
        mk= input("Make -->")
        md=input("Model -->")
        doors=int(input("amount of doors"))
        roof = input("Roof?")
        mycar=Car(yr,mk,md,doors,roof)
        mycar.give_intel()
        break
    except:
        continue
