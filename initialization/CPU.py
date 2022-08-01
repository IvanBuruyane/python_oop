from typing import List


class CPU:

    def __init__(self, name: str, fr: int) -> None:
        self.name = name
        self.fr = fr


class Memory:

    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume


class MotherBoard:
    total_mem_slots = 4

    def __init__(self, name: str, cpu: CPU, *mems: Memory) -> None:
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(mems)

    def get_config(self) -> List:
        mem_str = "Память: "
        for mem_slot in self.mem_slots:
            mem_str += f"{mem_slot.name} - {mem_slot.volume};"
        config = [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
            mem_str[:-1]
        ]
        return config

cpu1 = CPU("Intel", 3600)
mem1 = Memory("Nvidia DDR4", 8)
mem2 = Memory("Nvidia DDR5", 16)
mb = MotherBoard("MSI", cpu1, mem1, mem2)

print(mb.mem_slots)
