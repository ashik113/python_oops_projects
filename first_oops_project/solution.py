class Solution:
    @staticmethod
    def get_price_by_disease(medicines, disease):
        price = []
        for medicine in medicines:
            if medicine.disease == disease:
                price.append(medicine.price)
        return price
