push    ebp
mov     ebp, esp
sub     esp, 24
and     esp, 4294967280
mov     eax, 0
sub     esp, eax
mov     [ebp+var_4], 73319
mov     [ebp+var_8], 5968496
mov     [ebp+var_10], 6
sub     esp, 12
push    offset format   ; "Type cd-key: "
call    _printf
add     esp, 16
sub     esp, 8
lea     eax, [ebp+var_C]
push    eax
push    offset aD       ; "%d"
call    _scanf
add     esp, 16
mov     eax, [ebp+var_8]
cmp     eax, [ebp+var_C]
jnz     short loc_8048432
mov     edx, [ebp+var_10]
lea     eax, [ebp+var_4]
xor     [eax], edx
sub     esp, 8
push    [ebp+var_4]
push    offset aD_0     ; "%d\n"
call    _printf
add     esp, 16
jmp     short loc_8048442