#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

// Function to create a zombie process
void zombie_process() {
    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed for zombie");
    } else if (pid == 0) {
        printf("[ZOMBIE] Child (PID=%d) exiting...\n", getpid());
        exit(0); // Child exits immediately
    } else {
        printf("[ZOMBIE] Parent (PID=%d) sleeping to create zombie child (PID=%d)...\n", getpid(), pid);
        sleep(10); // Delay wait() so child remains zombie for a while
        wait(NULL); // Clean up zombie
        printf("[ZOMBIE] Parent collected zombie child\n");
    }
}

// Function to create an orphan process
void orphan_process() {
    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed for orphan");
    } else if (pid == 0) {
        sleep(5); // Wait so parent exits first
        printf("[ORPHAN] Child (PID=%d, PPID=%d) is now orphan\n", getpid(), getppid());
        exit(0);
    } else {
        printf("[ORPHAN] Parent (PID=%d) exiting so child becomes orphan (PID=%d)...\n", getpid(), pid);
        exit(0);
    }
}

// Function to demonstrate execve()
void execve_demo() {
    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed for execve");
    } else if (pid == 0) {
        printf("[EXECVE] Child (PID=%d) executing /bin/ls using execve()\n", getpid());
        char *args[] = {"/bin/ls", "-l", NULL};
        execve("/bin/ls", args, NULL);
        perror("execve failed"); // This line runs only if execve fails
        exit(1);
    } else {
        wait(NULL);
        printf("[EXECVE] Parent (PID=%d) finished waiting for execve() child\n", getpid());
    }
}

int main() {
    printf("\n=== Process Control Demo (fork, execve, wait, zombie, orphan) ===\n");

    zombie_process();  // Show zombie state
    sleep(2);

    // Fork again to avoid mixing process trees
    pid_t p = fork();
    if (p == 0) {
        orphan_process(); // Orphan child created in a new process
    } else {
        wait(NULL);
    }

    sleep(2);
    execve_demo();     // Show execve usage

    return 0;
}