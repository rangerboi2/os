import threading
import time
import random

# Buffer and its capacity
buffer = []
BUFFER_SIZE = 5

# Synchronization primitives
mutex = threading.Lock()
empty_slots = threading.Semaphore(BUFFER_SIZE)  # Initially, all slots are empty
filled_slots = threading.Semaphore(0)           # Initially, no slots are filled

# Producer thread
def producer():
    for i in range(10):
        item = random.randint(1, 100)
        empty_slots.acquire()        # Wait for an empty slot
        mutex.acquire()              # Lock access to the buffer

        buffer.append(item)
        print(f"[Producer] Produced: {item} | Buffer: {buffer}")

        mutex.release()              # Unlock buffer
        filled_slots.release()       # Signal that there's a new filled slot
        time.sleep(random.uniform(0.5, 1.5))

# Consumer thread
def consumer():
    for i in range(10):
        filled_slots.acquire()       # Wait for a filled slot
        mutex.acquire()              # Lock access to the buffer

        item = buffer.pop(0)
        print(f"[Consumer] Consumed: {item} | Buffer: {buffer}")

        mutex.release()              # Unlock buffer
        empty_slots.release()        # Signal that a slot is empty
        time.sleep(random.uniform(0.5, 1.5))

# Main
def main():
    prod_thread = threading.Thread(target=producer)
    cons_thread = threading.Thread(target=consumer)

    prod_thread.start()
    cons_thread.start()

    prod_thread.join()
    cons_thread.join()

    print("\n[Main] Producer and Consumer have finished execution.")

if __name__ == "__main__":
    main()
