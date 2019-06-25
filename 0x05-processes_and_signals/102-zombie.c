#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 *infinite_while - infinity loop.
 *
 *Return: 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 *main - create zombie process.
 *
 *Return: 0(success)
 */
int main(void)
{
	int i;
	pid_t child, zombie_pid;

	for (i = 1; i <= 5; i++)
	{
		child = fork();
		zombie_pid = getpid();
		if (child == 0)
		{
			printf("Zombie process created, PID: %d\n", zombie_pid);
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
