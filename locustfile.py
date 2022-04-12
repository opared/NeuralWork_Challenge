import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    @task
    def region(self):
        self.client.post("filtro-region/", json={"region":"Turin"})
    
    @task
    def hora(self):
        self.client.post("filtro-hora/", json={ "hora" : "5:00" })
    
    @task
    def fuente(self):
        self.client.post("filtro-fuente/", json={ "source" : "bad_diesel_vehicles" })


    @task
    def coordenadas(self):
        self.client.post("filtro-coordenadas/",
         json={ "coor_up" : "45" ,"coor_down" : "44", "coor_right" : "8","coor_left" : "7", "columna" : "origin_coord"  })