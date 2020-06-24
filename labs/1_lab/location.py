class Location:
	def __init__(self,name,lat,lon):
		self.name=name
		self.lat=lat
		self.lon=lon
	def __eq__(self,other):
		return self.name==other.name and self.lat==other.lat and self.lon==other.lon
	def __repr__(self):
		return f"Location('{self.name}', {self.lat}, {self.lon})"

def main():
	loc1 = Location("SLO", 35.3, -120.7)
	loc2 = Location("Paris", 48.9, 2.4)
	loc3 = Location("SLO", 35.3, -120.7)
	loc4 = loc1
	
	print("Location 1:",loc1)
	print("Location 2:",loc2)
	print("Location 3:",loc3)
	print("Location 4:",loc4)
	
	print("\nLocation 1 equals Location 2:",loc1==loc2)
	print("Location 1 equals Location 3:",loc1==loc3)
	print("Location 1 equals Location 4:",loc1==loc4)
	
	locations = [loc1, loc2]
	print(loc1 in locations)
	print(loc2 in locations)
	print(loc3 in locations)
	print(loc4 in locations)


if __name__ == "__main__":
	main()
