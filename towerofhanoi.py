def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi problem and print the steps.

    :param n: Number of disks
    :param source: The source peg
    :param auxiliary: The auxiliary peg
    :param target: The target peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
if __name__ == "__main__":
    n = 3  # Number of disks
    tower_of_hanoi(n, 'A', 'B', 'C')
