#include <stdio.h>
#include <cmp1.h>

#include "cmp2.h"

void cmp2_func() {
  printf("It's me, cmp2 func\r\n!");
  printf("I am now calling my friend cmp1\r\n");
  cmp1_func();
}

int main(int argc, char** argv)
{
	cmp2_func();
}
