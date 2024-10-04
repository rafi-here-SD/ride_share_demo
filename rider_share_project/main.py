# from ride import Ride, RideResquest, RiderMatching, RiderSharing
# from users import Rider , Driver
# from vehicle import Car, Bike 

# niye_jao = RiderSharing("Niye_jao")
# rahim = Rider("Rahim Uddin", "rahim@gamil.com",1234,"mohakhali",1200)
# niye_jao.add_rider(rahim)
# kolimuddin = Driver("kolim Uddin", "kolimuddin@gmail.com",1256,"Gulshan")
# niye_jao.add_drivers(kolimuddin)

# rahim.request_ride(niye_jao,"Uttara","car")
# rahim.show_current_ride()
# kolimuddin.reach_destination(rahim.current_ride)
# print(niye_jao)

from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

TGS = RideSharing("TGS")
rahim = Rider("Rahim Uddin", "rahim@gmail.com", 1234, "Mohakhali", 1200)
TGS.add_rider(rahim)
kolimuddin = Driver("Kolim Uddin", "kolim@gmail.com", 1256, "Gulshan")
TGS.add_driver(kolimuddin)
rahim.request_ride(TGS, "Uttara", "car")
kolimuddin.reach_destination(rahim.current_ride)
rahim.show_current_ride()
print(TGS)
