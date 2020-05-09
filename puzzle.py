class Puzzle:
    puzzle_amount = 0
    
    def __init__(self, description="N/A", elements_count=None, box_width=None, box_height=None,
                 producer_country="Ukraine", production_year=2020, price_in_UAH=None):
        self._description = description
        self._elements_count = elements_count
        self._box_width = box_width
        self._box_height = box_height
        self._producer_country = producer_country
        self._production_year = production_year
        self._price_in_UAH = price_in_UAH
        Puzzle.puzzle_amount +=1
        
    def __del__(self):
        print("Puzzle deleted.")

    def __str__(self):
        return self._description + ', ' + str(self._elements_count) + \
        ', ' + str(self._box_width) + ', ' + str(self._box_height) + \
        ', ' + self._producer_country + ', ' + str(self._production_year) + \
        ', ' + str(self._price_in_UAH)

    @staticmethod
    def get_puzzle_amount():
        return  Puzzle.puzzle_amount


if __name__ == "__main__":
    first_puzzle = Puzzle('city', 600, 20.5, 38.5, 'Poland', 2018, 499)
    second_puzzle = Puzzle('animals', 450)
    third_puzzle = Puzzle()

    print('First puzzle:', first_puzzle)
    print('Second puzzle:', second_puzzle)
    print('Third puzzle:', third_puzzle)
    print('\nAmount of puzzles:', Puzzle.get_puzzle_amount())















