class Car:
    def __init__(self,year,make,model,num_doors,roof):
        self.year=year
        self.make=make
        self.model=model
        self.num_doors= num_doors
        self.roof=roof

    def give_intel(self):
        print(f" Your car's \nyear:{self.year}")
        print(f" Your car's \nmake:{self.make}")
        print(f" Your car's \nmodel:{self.model}")
        print(f"Your car's \nnum_doors:{self.num_doors}")
        print(f"Your car's \nroof:{self.roof}")


mycar=Car(2024,"Mazda","CX-5",4,"none")
mycar()