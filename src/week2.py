class Week2:
    @staticmethod
    def imperial_to_kg(stones: int, pounds: int, ounces: int) -> float:
        """Converts imperial weight to kg"""
        return ((stones * 14 + pounds) * 16 + ounces) * 0.02835

    @staticmethod
    def kg_to_imperial(kg: float) -> tuple[int, int, int]:
        """Converts kg to imperial weight"""
        stones = kg / 6.35029
        whole_stones = stones // 1

        pounds = (stones % 1) * 14
        whole_pounds = pounds // 1

        ounces = (pounds % 1) * 16
        whole_ounces = ounces // 1
        return int(whole_stones), int(whole_pounds), int(whole_ounces)

    @staticmethod
    def run_conversion() -> None:
        """Runs the conversion"""
        to_kg = input("Convert to kg? [y/n] ")
        if to_kg.lower() == "y":
            stones = int(input("Number of stones: "))
            pounds = int(input("Number of pounds: "))
            ounces = int(input("Number of ounces: "))
            kg = Week2.imperial_to_kg(stones, pounds, ounces)
            print(f"The weight is {kg} kg")
        else:
            kg = float(input("Weight in kg: "))
            stones, pounds, ounces = Week2.kg_to_imperial(kg)
            print(f"The weight is {stones} stones, {pounds} pounds, {ounces} ounces")

    @staticmethod
    def banana_cost(amount: int) -> int:
        """Returns the cost of the given amount of kilos of bananas"""
        BANANA_KILO = 300
        DELIVERY_COST = 499
        REDUCED_DELIVERY = DELIVERY_COST - 150

        cost = amount * BANANA_KILO
        if cost > 5000:
            return cost + REDUCED_DELIVERY
        else:
            return cost + DELIVERY_COST

    @staticmethod
    def order_bananas() -> None:
        """Orders bananas"""
        amount = int(input("How many kilos of bananas do you want? "))
        cost = Week2.banana_cost(amount)
        print(f"The cost is £{cost}")

    @staticmethod
    def find_training_zone(age: int, rate: int) -> None:
        """Finds the training zone"""
        maximum = 208 - 0.7 * age

        match rate:
            case rate if rate >= 0.9 * maximum:
                zone = "Interval training"
            case rate if 0.7 * maximum <= rate < 0.9 * maximum:
                zone = "Threshold training"
            case rate if 0.5 * maximum <= rate < 0.7 * maximum:
                zone = "Aerobic training"
            case _:
                zone = "Couch potato"

        print(f"Training zone: '{zone}'")

    @staticmethod
    def herons_formula(a: int, b: int, c: int) -> None:
        """Calculates the herons formula"""
        s = (a + b + c) / 2
        print(f"Triangle Area: {(s * (s - a) * (s - b) * (s - c)) ** 0.5}")
