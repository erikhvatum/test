#include <TESTHEADER.h>

#ifndef correct_header_found
#error we got the TESTHEADER.h from the system path and not our -I which should ALWAYS COME BEFORE the system -I parameters
#endif

#include <stdio.h>

int test()
{
    printf("native test func ran!\n");
    return 42;
}
