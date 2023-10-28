from island import Island
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_pirates = n_pirates
        self.heap = None

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        if self.heap is None:
            self.heap = MaxHeap.heapify(islands)
        else:
            self.heap = MaxHeap.heapify(list(self.heap.mapping.keys()) + islands)

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        #intantiate a list of pirate actions in which no island is chosen and non crew is sent
        removed = []
        action_list = [(None, 0)] * self.n_pirates
        #if the island heap is empty, return the pirate action list
        if self.heap is None:
            return action_list
        #for each pirate, get the max value island from the heap
        for pirate in range(self.n_pirates):
            island = self.heap.get_max()
            removed.append(island)
        # if the island value is greater thant 2*crew, update the pirate action list with the island and crew
            if island.value() > 2:
                action_list[pirate] = (island, crew)
                # send the maximum crew numbers and update the island money and marines
                if island.marines > crew:
                    island.money -= int((crew/island.marines)*island.money)
                    island.marines -= crew
                else:
                    island.money = 0
                    island.marines = 0
            else:
                break
        self.add_islands(removed)
        return action_list

        # if it is ever less or equal to the crew, add back the popped island and return the pirate action list
