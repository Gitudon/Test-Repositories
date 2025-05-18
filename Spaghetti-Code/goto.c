#include <stdio.h>

int main() {
    int x = 0;

start:
    printf("Start of the program.\n");
    x++;

    if (x < 3) {
        goto middle;
    } else {
        goto end;
    }

middle:
    printf("In the middle of the program. x = %d\n", x);
    goto start;

end:
    printf("End of the program. x = %d\n", x);
    return 0;
}