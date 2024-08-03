section .data
    prompt db 'Enter the first number: ', 0
    prompt2 db 'Enter the second number: ', 0
    prompt3 db 'Enter the third number: ', 0
    largest_msg db 'The largest number is: ', 0
    smallest_msg db 'The smallest number is: ', 0
    equal_msg db 'All numbers are equal.', 0

section .bss
    num1 resb 10
    num2 resb 10
    num3 resb 10
    largest resb 10
    smallest resb 10

section .text
    global _start

_start:
    mov rsi, prompt
    call print_string
    call read_input
    mov rsi, num1
    call atoi

    mov rsi, prompt2
    call print_string
    call read_input
    mov rsi, num2
    call atoi

    mov rsi, prompt3
    call print_string
    call read_input
    mov rsi, num3
    call atoi

    mov rsi, num1
    mov rdi, num2
    call compare_numbers
    mov rsi, num1
    mov rdi, num3
    call compare_numbers
    mov rsi, num2
    mov rdi, num3
    call compare_numbers

    mov rsi, largest_msg
    call print_string
    mov rsi, largest
    call print_string
    mov rsi, smallest_msg
    call print_string
    mov rsi, smallest
    call print_string

    mov rax, 60     
    xor rdi, rdi    
    syscall

print_string:
    mov rax, 0x1      
    mov rdi, 0x1      
    mov rdx, 0xFFFFFFFF  
    syscall
    ret

read_input:
    mov rax, 0         
    mov rdi, 0        
    mov rdx, 10       
    syscall
    ret

atoi:
    xor rcx, rcx     
    xor rax, rax      
atoi_loop:
    movzx rdx, byte [rsi + rcx]  
    test rdx, rdx       
    jz atoi_done      
    sub rdx, '0'      
    imul rax, rax, 10   
    add rax, rdx        
    inc rcx             
    jmp atoi_loop       
atoi_done:
    ret

compare_numbers:
    mov rax, 0
    mov rdx, 0
    movzx rax, byte [rsi]
    movzx rdx, byte [rdi]
    cmp rax, rdx
    jg greater
    jl smaller
    jmp equal

greater:
    mov rsi, rdi
    mov rdi, largest
    mov rax, rdx
    call itoa
    jmp done

smaller:
    mov rdi, smallest
    mov rax, rdx
    call itoa
    jmp done

equal:
    mov rsi, equal_msg
    call print_string
    jmp exit

done:
    mov rax, 0
    mov rdx, 0
    movzx rax, byte [rsi]
    movzx rdx, byte [rdi]
    call itoa
    jmp exit

exit:
    ret

itoa:
    xor rcx, rcx       
    mov rbx, 10       
itoa_loop:
    xor rdx, rdx      
    div rbx            
    add dl, '0'      
    push rdx         
    test rax, rax      
    jnz itoa_loop      
itoa_done:
    mov rcx, rdi     
itoa_poploop:
    pop rax           
    mov [rcx], al    
    inc rcx          
    test rax, rax     
    jnz itoa_poploop  
    mov byte [rcx], 0  
    ret
