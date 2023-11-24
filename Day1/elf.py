from dataclasses import dataclass, field


@dataclass
class Elf:
    food_list: list[int] = field(default_factory=list)

    def get_calories(self):
        return sum(self.food_list)


def calculate_calories_per_elf(calories_input):
    elves = []
    current_elf = Elf()
    for line in calories_input.splitlines():
        if line == "":
            elves.append(current_elf)
            current_elf = Elf()
        else:
            current_elf.food_list.append(int(line))
    elves.append(current_elf)
    calories_list = [elf.get_calories() for elf in elves]
    return calories_list

def elf_with_max_calories(calories_input):
    calories_list = calculate_calories_per_elf(calories_input)
    return max(calories_list)


def top3_elves_with_max_calories(calories_input):
    calories_list = calculate_calories_per_elf(calories_input)
    calories_list.sort(reverse=True)
    return sum(calories_list[:3])


if __name__ == "__main__":
    with open("puzzle_input.txt") as f:
        calories_input = f.read()
    print(elf_with_max_calories(calories_input))
