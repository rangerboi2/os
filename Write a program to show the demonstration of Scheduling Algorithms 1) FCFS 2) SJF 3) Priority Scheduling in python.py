def fcfs_scheduling(processes):
    print("\n--- FCFS Scheduling ---")
    processes.sort(key=lambda x: x['arrival'])  # Sort by arrival time
    time = 0
    for p in processes:
        if time < p['arrival']:
            time = p['arrival']
        p['start'] = time
        p['waiting'] = time - p['arrival']
        time += p['burst']
        p['turnaround'] = p['waiting'] + p['burst']

    print_table(processes)


def sjf_scheduling(processes):
    print("\n--- SJF Scheduling ---")
    time = 0
    done = []
    while len(done) < len(processes):
        available = [p for p in processes if p['arrival'] <= time and p not in done]
        if not available:
            time += 1
            continue
        p = min(available, key=lambda x: x['burst'])  # Choose shortest job
        p['start'] = time
        p['waiting'] = time - p['arrival']
        time += p['burst']
        p['turnaround'] = p['waiting'] + p['burst']
        done.append(p)

    print_table(done)


def priority_scheduling(processes):
    print("\n--- Priority Scheduling ---")
    time = 0
    done = []
    while len(done) < len(processes):
        available = [p for p in processes if p['arrival'] <= time and p not in done]
        if not available:
            time += 1
            continue
        p = min(available, key=lambda x: x['priority'])  # Choose highest priority
        p['start'] = time
        p['waiting'] = time - p['arrival']
        time += p['burst']
        p['turnaround'] = p['waiting'] + p['burst']
        done.append(p)

    print_table(done)


def print_table(processes):
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'WT':<5}{'TAT':<5}")
    for p in processes:
        print(f"{p['pid']:<5}{p['arrival']:<5}{p['burst']:<5}{p['priority']:<5}{p['waiting']:<5}{p['turnaround']:<5}")


# Input Section
def get_input():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        print(f"\nProcess {i+1}")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        priority = int(input("Priority (lower number = higher priority): "))
        processes.append({
            'pid': f'P{i+1}',
            'arrival': arrival,
            'burst': burst,
            'priority': priority
        })
    return processes


# Main Menu
def main():
    processes = get_input()
    fcfs_scheduling([p.copy() for p in processes])
    sjf_scheduling([p.copy() for p in processes])
    priority_scheduling([p.copy() for p in processes])


if __name__ == "__main__":
    main()
