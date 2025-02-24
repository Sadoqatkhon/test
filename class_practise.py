class Car():
    __num__=0
    def __init__(self, nomi, model, narx, masofa=0) :
        self.nomi=nomi
        self.model=model
        self.narx=narx
        self.__masofa=masofa
        Car.__num__+=1
    

    def get_info(self):
        car_dict={"nomi":self.nomi,
                 "model":self.model,
                 "narx":self.narx,
                 "masofa":self.__masofa}
        return car_dict
    def __str__(self):
        return self.model
    @classmethod
    def avto_soni(cls):
        return cls.__num__
    
avto=Car("Spark","jn",narx=70000)
avto1=Car("Spark","jn",narx=70000)
avto2=Car("Spark","jn",narx=70000)
avto3=Car("Spark","jn",narx=70000)


print(avto1.avto_soni())
