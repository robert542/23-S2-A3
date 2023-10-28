from island import Island
from data_structures.heap import MaxHeap


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = islands
        self.crew = crew
        self.heap = MaxHeap.heapify(self.islands)


    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        # temp_crew = self.crew
        # self.heap.save_state()
        # result = []
        # while temp_crew > 0:
        #     island = self.heap.remove_max()
        #     if island.marines <= temp_crew:
        #         result.append((island, island.marines))
        #         temp_crew -= island.marines
        # self.heap.restore_state()
        # return result

        temp_crew = self.crew
        result = []
        index = 1  # Starting at the root of the heap
        
        while temp_crew > 0 and index <= self.heap.length:
            island = self.heap.the_array[index]
            
            if island.marines <= temp_crew:
                result.append((island, island.marines))
                temp_crew -= island.marines
            
            # Determine which child to go to next
            left_child = 2 * index
            right_child = 2 * index + 1
            
            # Move to the larger of the two children
            if right_child <= self.heap.length and self.heap.the_array[right_child] > self.heap.the_array[left_child]:
                index = right_child
            else:
                index = left_child



        return result


    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        return [self.select_islands_from_crew_number(crew) for crew in crew_numbers]

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        # Step 1: Locate the Island
        island_index = self.heap.mapping[island]
        
        # Step 2: Update Values
        self.heap[island_index].money = new_money
        self.heap[island_index].marines = new_marines

        # Step 3: Re-Heapify
        self.heap.rise(island_index)
        island_index = self.heap.mapping[island]
        self.heap.sink(island_index)
