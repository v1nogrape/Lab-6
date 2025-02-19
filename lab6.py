class Building:
    className = 'Building'
    objectsCount = 0

    def __init__(self, area, cost_per_sqm, residents):
        self._area = area
        self._cost_per_sqm = cost_per_sqm
        self._residents = residents
        Building.objectsCount += 1

    def get_area(self):
        return self._area

    def set_area(self, area):
        if area > 0:
            self._area = area
        else:
            self._area = 1

    def get_cost_per_sqm(self):
        return self._cost_per_sqm

    def set_cost_per_sqm(self, cost):
        if cost > 0:
            self._cost_per_sqm = cost
        else:
            self._cost_per_sqm = 1

    def get_residents(self):
        return self._residents

    def set_residents(self, residents):
        if residents > 0:
            self._residents = residents
        else:
            self._residents = 1

    def info(self):
        print(f'Площадь здания: {self._area} кв. м')
        print(f'Стоимость одного квадратного метра: {self._cost_per_sqm}')
        print(f'Количество проживающих: {self._residents}')

    def total_cost(self):
        return self._area * self._cost_per_sqm

    def cost_per_resident(self):
        return self._cost_per_sqm * self._area / self._residents


class VillageHouse(Building):
    className = 'VillageHouse'

    def __init__(self, area, cost_per_sqm, residents, garden_area):
        super().__init__(area, cost_per_sqm, residents)
        self._garden_area = garden_area

    def get_garden_area(self):
        return self._garden_area

    def set_garden_area(self, garden_area):
        if garden_area >= 0:
            self._garden_area = garden_area
        else:
            self._garden_area = 0

    def info(self):
        super().info()
        print(f'Площадь сада: {self._garden_area} кв. м')

    def total_cost(self):
        return super().total_cost()

    def cost_per_resident(self):
        return super().cost_per_resident()


class ApartmentBuilding(Building):
    className = 'ApartmentBuilding'

    def __init__(self, area, cost_per_sqm, residents, num_apartments):
        super().__init__(area, cost_per_sqm, residents)
        self._num_apartments = num_apartments

    def get_num_apartments(self):
        return self._num_apartments

    def set_num_apartments(self, num_apartments):
        if num_apartments > 0:
            self._num_apartments = num_apartments
        else:
            self._num_apartments = 1

    def info(self):
        super().info()
        print(f'Количество квартир: {self._num_apartments}')

    def total_cost(self):
        return super().total_cost()

    def cost_per_resident(self):
        return super().cost_per_resident()


vh = VillageHouse(100, 1500, 4, 50)
ab = ApartmentBuilding(2000, 2000, 500, 50)

#print(f'Общая стоимость деревенского дома: {vh.total_cost()}')
print(f'Общая стоимость многоквартирного дома: {ab.total_cost()}')

#print(f'Стоимость на одного жителя в деревенском доме: {vh.cost_per_resident()}')
print(f'Стоимость на одного жителя в многоквартирном доме: {ab.cost_per_resident()}')

#vh.info()
ab.info()
